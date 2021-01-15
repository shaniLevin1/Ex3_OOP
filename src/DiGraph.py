from NodeData import NodeData
from GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    """
    This class represents a directed weighted graph with all it properties.
    """
    def __init__(self):
        """"
        constructor->init new weighted directed graph
        """
        self.nodes = {}
        self.MC_counter = 0
        self.Edge_counter = 0

    def v_size(self) -> int:
        """"
        :return the number of nodes in the graph.
        """
        return len(self.nodes)  # return the length of dictionary nodes

    def e_size(self) -> int:
        """"
        :return the number of edges in the graph.
        """
        return self.Edge_counter

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        """
        This function add a vertex to the given graph
        :param node_id: the key of the node
        :param pos: the location of the node
        :return: boolean->true if the node was added to the graph, else false
        """
        if node_id in self.nodes.keys():  # if the given node_id is in the graph return false
            return False
        self.MC_counter += 1
        v = NodeData(node_id, pos)  # defining new vertex
        self.nodes[node_id] = v  # update add the given key to the dictionary vertices and if it exist
        return True

    def get_vertex(self, key):
        """
        this function return the node by giving key
        :param key->the key of the node
        :return the node
        """
        try:
            return self.nodes[key]
        except KeyError:
            return None

    def __contains__(self, key):
        """
        this function check if a node is in the graph
        :param key: the key of the node we check
        :return: boolean-> true if the given node is in the graph, else false
        """
        return key in self.nodes.keys()

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        """
        this function add an edge between to nodes in the graph
        :param id1: key of the src node
        :param id2: key of the dest node
        :param weight: the weihgt of the new edge
        :return: boolean-> true if the edge was added, else false
        """
        if (self.__contains__(id1)) & (self.__contains__(id2)):
            if (id1 not in self.all_in_edges_of_node(id2).keys()) & (id2 not in self.all_out_edges_of_node(id1).keys()):
                if id1 is not id2:
                    if weight >= 0:
                        self.MC_counter += 1
                        self.Edge_counter += 1
                        self.nodes[id1].outEdges[id2] = weight
                        self.nodes[id2].inEdges[id1] = weight
                        return True
        return False

    def get_mc(self) -> int:
        """
        :return: the number of changes were done in the graph
        """
        return self.MC_counter

    def get_all_v(self) -> dict:
        """
        :return: the dictionary of all the nodes in the graph
        """
        return self.nodes

    def all_out_edges_of_node(self, id1: int) -> dict:
        """
        :return: the dictionary of all the nodes that going out from the given node
        """
        return self.get_vertex(id1).outEdges

    def all_in_edges_of_node(self, id1: int) -> dict:
        """
        :return: the dictionary of all the nodes that going in to the given node
        """
        return self.get_vertex(id1).inEdges

    def remove_node(self, node_id: int) -> bool:
        """
        this function remove a node from the graph
        :param node_id: the key of the given node
        :return: boolean-> return true if the node was removed from the graph, else false
        """
        if node_id not in self.nodes.keys():
            return False
        for e in self.all_in_edges_of_node(node_id).keys():
            del self.nodes[e].outEdges[node_id]
            self.Edge_counter -= 1
        for e in self.all_out_edges_of_node(node_id).keys():
            del self.nodes[e].inEdges[node_id]
            self.Edge_counter -= 1
        del self.nodes[node_id]
        self.MC_counter += 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        """
        this function remove an edge between two given nodes from the graph
        :param node_id1: key of the src node
        :param node_id2: key of the dest node
        :return: boolean-> return true if the edge was removed from the graph, else false
        """
        if (not self.__contains__(node_id1)) | (not self.__contains__(node_id2)) | (
                node_id2 not in self.all_out_edges_of_node(node_id1)):
            return False
        del self.nodes.get(node_id1).outEdges[node_id2]
        del self.nodes.get(node_id2).inEdges[node_id1]
        self.Edge_counter -= 1
        self.MC_counter += 1
        return True

