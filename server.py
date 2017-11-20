# -*- coding: utf-8 -*-

import logging.config
logging.config.fileConfig("logging.conf")
log = logging.getLogger(__name__)

import os

import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.options import define, options
from datetime import datetime



class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            # (r"/", MainHandler),
            # (r"/admin", AdminHandler),
        ]


        tornado.web.Application.__init__(self, handlers)

        try:
            pass
        except:
            log.error('')

        log.info('TORNADO PEOPLE SERVICE STARTED')



def main():
    app = Application()
    # http_server_1 = tornado.httpserver.HTTPServer(app)
    # http_server_1.listen(12385)
    app.listen(12385)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == "__main__":
    main()