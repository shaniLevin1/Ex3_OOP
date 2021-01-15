from Position import Position


class NodeData(object):
    """
    This class represents a node in the graph with all it properties: id, Tag, Info, weight and location on the graph
    """

    def __init__(self, key: int, pos=None):
        """
        :param pos
        :param key
        constructor->init new node by giving key and position
        """
        self.key = key
        self.outEdges = {}
        self.inEdges = {}
        self.tag = 0
        if pos is not None:
            self.pos = Position(pos)
        else:
            self.pos = pos

    def setTag(self, tag):
        """
        :param tag
        set the value of the tag
        """
        self.tag = tag
