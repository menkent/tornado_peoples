# -*- coding: utf-8 -*-

import logging

log = logging.getLogger(__name__)

from tornado.web import RequestHandler


class MainHandler(RequestHandler):
    def get(self):
        self.xsrf_token

        find_x = self.get_argument("find_x", None)
        find_y = self.get_argument("find_y", None)
        neighbors = []
        if find_x and find_y:
            try:
                x = float(find_x)
                y = float(find_y)
                neighbors = self.application.find_near_neighbor(x=x, y=y)
            except:
                log.warning("Bad coords: %s, %s", find_x, find_y)
        self.render('../templates/main_template.html', neighbors=neighbors)

    def post(self):
        user_name = self.get_argument("user_name", None)
        coord_x = float(self.get_argument("coord_x", None))
        coord_y = float(self.get_argument("coord_y", None))
        self.application.add_neighbor(user_name, coord_x, coord_y)
        self.finish('User Added')


class AddUsersHandler(RequestHandler):
    def get(self):
        from random import randrange
        from datetime import datetime
        count = int(self.get_argument("count", 10))
        for x in xrange(0, count):
            self.application.add_neighbor(
                "random_un_{}".format(datetime.now().microsecond),
                randrange(-180, 180), randrange(-90, 90))  # ограничения lat/lng
        self.redirect("/")


