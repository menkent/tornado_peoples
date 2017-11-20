# -*- coding: utf-8 -*-

import logging.config
logging.config.fileConfig("logging.conf")
log = logging.getLogger(__name__)

import tornado.httpserver
import tornado.ioloop
import tornado.web

from handlers.add_user import AddUserHandler
from handlers.find_users import FindUsersHandler


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", FindUsersHandler),
            (r"/add", AddUserHandler),
        ]


        tornado.web.Application.__init__(self, handlers)

        try:
            pass
        except:
            log.error('')

        log.info('TORNADO PEOPLE SERVICE STARTED')


def main():
    app = Application()
    app.listen(12385)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()
