# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)
import tornado.gen

class Neighbor(object):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    @property
    def position(self):
        return [self.x, self.y]

    @tornado.gen.coroutine
    def save(self, collection):
        if self.x is None or self.y is None:
            log.warn("Bad coordinate: %s %s", self.x, self.y)
            raise tornado.gen.Return(None)
        res = yield collection.insert({'name': self.name, 'position': {'type': 'Point', 'coordinates': [self.x, self.y]}})
        raise tornado.gen.Return(res)

    @classmethod
    def from_mongo(cls, d):
        coords = d.get(u'position').get(u'coordinates')
        return cls(name=d.get(u'name'), x=coords[0], y=coords[1])