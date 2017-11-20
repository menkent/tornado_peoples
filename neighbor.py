# -*- coding: utf-8 -*-

import logging
log = logging.getLogger(__name__)


import uuid


class Position(complex):
    # info: для операций сложения, вычитания и abs
    x = complex.real
    y = complex.imag

    def as_dict(self):
        return dict(x=self.x, y=self.y)

    def __str__(self):
        "{}({:.2f}:{:.2f})".format(self.__class__.__name__, self.x, self.y)

    def __repr__(self):
        "{}({}:{})".format(self.__class__.__name__, self.x, self.y)

    def distance_to(self, target):
        return abs(target - self)



class Neighbor(object):
    def __init__(self, name, x, y):
        self.uid = uuid.UUID()
        self.name

    def get(self):
        self.render()