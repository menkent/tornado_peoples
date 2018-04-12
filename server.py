# -*- coding: utf-8 -*-

import logging.config
logging.config.fileConfig("logging.conf")
log = logging.getLogger(__name__)

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen

import motor
from bson.son import SON

from handlers.main_handler import MainHandler, AddUsersHandler

from neighbor import Neighbor


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/addtest", AddUsersHandler),
        ]

        tornado.web.Application.__init__(self, handlers)

        try:
            self.motor_client = motor.motor_tornado.MotorClient()
            self.db = self.motor_client["test_neighbor"]
            self.neighbors = self.db["neighbors"]
            self.neighbors.ensure_index([("position", "2dsphere")])
        except:
            log.error('')

        log.info('TORNADO PEOPLE SERVICE STARTED')

    @tornado.gen.coroutine
    def add_neighbor(self, name, x, y):
        yield Neighbor(name=name, x=x, y=y).save(collection=self.neighbors)

    @tornado.gen.coroutine
    def find_near_neighbor(self, x, y, limit=100):
        result_list = []
        cursor = self.neighbors.find({"position": SON([("$near", {"$geometry": SON([("type", "Point"), ("coordinates", [x, y])])})])}).limit(limit)
        while (yield cursor.fetch_next):
            result_list.append(Neighbor.from_mongo(cursor.next_object()))
        raise tornado.gen.Return(result_list)


def main():
    app = Application()
    app.listen(12385)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
