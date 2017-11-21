# -*- coding: utf-8 -*-

import logging.config
logging.config.fileConfig("logging.conf")
log = logging.getLogger(__name__)

import tornado.httpserver
import tornado.ioloop
import tornado.web

from pymongo import MongoClient
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
            self.mongo_client = MongoClient()
            self.db = self.mongo_client.test_neighbor
            self.neighbors = self.db["neighbors"]
            self.neighbors.ensure_index([("position", "2dsphere")])
        except:
            log.error('')

        log.info('TORNADO PEOPLE SERVICE STARTED')

    def add_neighbor(self, name, x, y):
        Neighbor(name=name, x=x, y=y).save(collection=self.neighbors)

    def find_near_neighbor(self, x, y, limit=100):
        res = self.neighbors.find({"position": SON([("$near", {"$geometry": SON([("type", "Point"), ("coordinates", [x, y])])})])}).limit(limit)
        for d in res:
            yield Neighbor.from_mongo(d)


def main():
    app = Application()
    app.listen(12385)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
