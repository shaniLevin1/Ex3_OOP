import math


class Position(tuple):
    """
    This class represent a position of node by x, y and z
    """

    def _init_(self, pos: tuple = None):
        """
        :param pos
        constructor->init new position by giving tuple of 3 parameters->x,y,z
        """
        self.x = pos[0]
        self.y = pos[1]
        self.z = pos[2]

    def distance(self, g):
        """
        :param g->pos
        :return the distance between two given pos
        """
        return math.sqrt(math.pow(self.x - g.x, 2) + math.pow(self.y - g.y) + math.pow(self.z - g.z, 2))
