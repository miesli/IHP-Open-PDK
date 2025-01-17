########################################################################
#
# Copyright 2023 IHP PDK Authors
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#    https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
########################################################################

import pya

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.point = pya.DPoint(x, y)

    @classmethod
    def areColinearPoints(cls, p1, p2, p3):
        raise Exception("Not implemented yet!")

    def copy(self):
        raise Exception("Not implemented yet!")

    def getCoord(self, dir):
        raise Exception("Not implemented yet!")

    def getSpacing(self, dir, refPoint):
        raise Exception("Not implemented yet!")

    def getX(self):
        return self.point.x

    def getY(self):
        return self.point.y

    def invalid(self):
        raise Exception("Not implemented yet!")

    def isBetween(self, a, b):
        raise Exception("Not implemented yet!")

    def isValid(self, ):
        raise Exception("Not implemented yet!")

    def place(self, dir, refPoint, distance, align = True):
        raise Exception("Not implemented yet!")

    def set(self, p):
        raise Exception("Not implemented yet!")

    def set(self, _x, _y):
        raise Exception("Not implemented yet!")

    def setCoord(self, dir, coord):
        raise Exception("Not implemented yet!")

    def setX(self, x):
        self.point.x = x

    def setY(self, y):
        self.point.y = y

    def snap(self, grid, snapType=None):
        raise Exception("Not implemented yet!")

    def snapX(self, grid, snapType=None):
        raise Exception("Not implemented yet!")

    def snapY(self, grid, snapType=None):
        raise Exception("Not implemented yet!")

    def snapTowards(self, grid, dir):
        raise Exception("Not implemented yet!")

    def toDiagAxes(self):
        raise Exception("Not implemented yet!")

    def toOrthogAxes(self):
        raise Exception("Not implemented yet!")

    def transform(self, trans):
        raise Exception("Not implemented yet!")

