# -*- coding: utf-8 -*-

import logging

log = logging.getLogger(__name__)

from tornado.web import RequestHandler


class AddUserHandler(RequestHandler):
    def get(self):
        self.render()