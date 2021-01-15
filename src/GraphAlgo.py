import math
from typing import List
from GraphInterface import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
import json
import matplotlib.pyplot as plt
from src.Position import Position
import networkx as nx
import random


def DFS(id1: int, graph: GraphInterface):
    """
    returns a list of all the keys associated with reachable nodes from a required node
    the function goes deep and keeps the tracked nodes, help function for SCC
    :param id1: the node to check which nodes are reachable from
    :param graph: the graph to be focused on
    :return: list of keys
    """
    visited = {}
    stack = [graph.get_vertex(id1)]
    visited.update({id1: [-1, 0]})
    while len(stack) > 0:
        start = stack.pop()
        if start is not None:
            for n in start.outEdges:
                if n not in visited:
                    visited.update({n: [start.key, visited[start.key][1] + start.outEdges[n]]})
                    stack.append(graph.get_vertex(n))
    l = []
    for i in visited.keys():
        l.append(i)
    return l


class GraphAlgo(GraphAlgoInterface):
    """
    this class represents directed weighted graph with all its algorithms
    """

    def __init__(self, graph: DiGraph = None):
        """
        inits the graph - creates a new graph
        :param graph: the graph to be created
        """
        self.graph = DiGraph()
        if graph is not None:
            self.graph = graph

    def get_graph(self) -> GraphInterface:
        """
         :return: the directed graph on which the algorithm works on
        """
        return self.graph

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        """
        visited = {}
        stack = []
        if (len(self.graph.nodes) == 0) | (id1 not in self.graph.get_all_v().keys()) | (
                id2 not in self.graph.get_all_v().keys()):
            return math.inf, []
        stack.append(self.graph.get_vertex(id1))
        visited.update({id1: [-1, 0]})  # {id:[prev,weight]}

        while len(stack) > 0:
            start = stack.pop()

            for n in start.outEdges:
                if n in visited.keys():
                    i = visited[n][0]  # 0[0]-(1)->1[1]-(4)->4[5]=5, 0[-1]-(1)->2[1]-(2)->4[3]=3
                    if i != -1:
                        if visited[n][1] > visited[start.key][1] + start.outEdges[n]:  # 5>1+2
                            visited.update({n: [start.key, visited[start.key][1] + start.outEdges[n]]})
                            stack.append(self.graph.get_vertex(n))
                elif n not in visited:
                    visited.update({n: [start.key, visited[start.key][1] + start.outEdges[n]]})
                    stack.append(self.graph.get_vertex(n))

        if id2 in visited.keys():
            l = list()
            n = id2
            while n != id1:
                l.append(n)
                n = visited[n][0]
            l.append(id1)
            l.reverse()
            return visited[id2][1], l
        return math.inf, []

    def connected_components(self) -> List[list]:
        """
        Finds all the Strongly Connected Component(SCC) in the graph.
        @return: The list all SCC
        """
        vertexList = list(self.graph.get_all_v().keys())
        ans = []
        while len(vertexList) != 0:
            transposedGraph = self.trans()
            DFSList = list(DFS(vertexList[0], self.graph))
            while len(DFSList) > 0:
                transposedDfsList = list(DFS(DFSList[0], transposedGraph))
                temp_list = []
                for x in transposedDfsList:
                    if x in DFSList:
                        temp_list.append(x)
                transposedDfsList = temp_list
                ans.append(transposedDfsList)
                temp_list = []
                for x in DFSList:
                    if (x not in transposedDfsList) & (x in vertexList):
                        temp_list.append(x)
                DFSList = temp_list
                temp_list = []
                for x in vertexList:
                    if x not in transposedDfsList:
                        temp_list.append(x)
                vertexList = temp_list
        return ans

    def connected_component(self, id1: int) -> list:
        """
        Finds the Strongly Connected Component(SCC) that node id1 is a part of using DFS function
        that goes deep and returns a list of all reachable nodes from node id1
        @param id1: The node id
        @return: The list of nodes in the SCC
        """
        if self.graph.get_vertex(id1) is None:
            return []
        pylist = self.connected_components()
        for i in pylist:
            if id1 in i:
                return i

    def trans(self) -> DiGraph:
        """
        transposes a given graph , Re-directs all the edges' directions
        :return: transposed graph
        """
        trans_graph = DiGraph()
        for n in self.graph.nodes:
            trans_graph.add_node(n)
            trans_graph.get_vertex(n).tag = self.graph.get_vertex(n).tag
        for n in self.graph.nodes.keys():
            for e in self.graph.all_out_edges_of_node(n).keys():
                trans_graph.add_edge(e, n, self.graph.all_out_edges_of_node(n).get(e))
        return trans_graph

    def load_from_json(self, file_name: str) -> bool:
        """
       Loads a graph from a json file.
       @param file_name: The path to the json file
       @returns True if the loading was successful, False o.w.
       """
        try:
            with open(file_name, 'r') as file1:
                data1 = json.load(file1)
            for node in data1['Nodes']:
                if "pos" in node:
                    pos1 = node["pos"]
                    p = str(pos1)
                    p = p.replace("[", "")
                    p = p.replace("'", "")
                    p = p.replace("]", "")
                    p = p.replace("'", "")
                    p = tuple(p.split(","))
                    pos = Position(p)
                    self.graph.add_node(node['id'], pos)
                else:
                    self.graph.add_node(node['id'])
                for edge in data1['Edges']:
                    self.graph.add_edge(edge["src"], edge["dest"], edge["w"])
            return True

        except IOError as e:
            raise e
            return False

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
        """
        data1 = {}
        try:
            data1["Edges"] = []
            data1["Nodes"] = []
            for key1 in self.graph.get_all_v().keys():
                pos = str(self.graph.get_vertex(key1).pos)
                if pos is not None:
                    pos = str(pos)
                    pos = pos.replace("\'", "")
                    data1["Nodes"].append({"pos": pos, "id": key1})
                else:
                    data1["Nodes"].append({"id": key1})
                for key2 in self.graph.all_out_edges_of_node(key1):
                    weight = self.graph.all_out_edges_of_node(key1).get(key2)
                    data1["Edges"].append({"src": key1, "w": weight, "dest": key2})
            data = data1.__str__()
            data = data.replace(" ", "")
            data = data.replace("'", "\"")
            data = data.replace("(", "")
            data = data.replace(")", "")
            with open(file_name, "w") as file2:
                file2.write(data)
                return True

        except FileNotFoundError:
            raise FileNotFoundError
            return False

    def plot_graph(self) -> None:
        """
        this function plot a graph by the matplotlib of python.
        it plot the nodes according the positions, and if the node has no position the function choose random
        position according an algorithm, we wrote.
        """
        x1_vals = []
        y1_vals = []
        ax = plt.axes()
        plt.title("Graph")
        for key1 in self.graph.get_all_v().keys():
            pos1 = self.graph.get_vertex(key1).pos
            if pos1 is not None:  # if pos isn't exist
                x1 = pos1[0]
                y1 = pos1[1]
                x1_vals.append(float(x1))
                y1_vals.append(float(y1))

        for key1 in self.graph.get_all_v().keys():
            pos1 = self.graph.get_vertex(key1).pos
            if pos1 is None:
                list1 = []
                list2 = []
                if len(x1_vals) < 2 and len(y1_vals) < 2:  # if there is no bounding box
                    x1 = random.uniform(32.000, 33.000)
                    while x1 in list1:
                        x1 = random.uniform(32.000, 33.000)
                    list1.append(x1)
                    y1 = random.uniform(35.000, 36.000)
                    while y1 in list2:
                        y1 = random.uniform(35.000, 36.000)
                    list2.append(y1)
                    x1_vals.append(x1)
                    y1_vals.append(y1)
                else:
                    x1, y1 = self.pos_avr(x1_vals, y1_vals)
                    x1_vals.append(x1)
                    y1_vals.append(y1)
                pos4 = x1, y1, 0.0
                self.graph.get_vertex(key1).pos = Position(pos4)

        for i in range(len(x1_vals)):
            plt.plot(x1_vals[i], y1_vals[i], 'o', markersize=4, color='pink',
                     markerfacecolor='blue')  # TODO:SHOULD check implement
            print(x1_vals[i])
            print(y1_vals[i])

        for key1 in self.graph.get_all_v().keys():
            pos = self.graph.get_vertex(key1).pos
            x1 = pos[0]
            y1 = pos[1]
            for key2 in self.graph.all_out_edges_of_node(key1):
                if self.graph.get_vertex(key2) is not None:
                    pos1 = self.graph.get_vertex(key2).pos
                    x2 = pos1[0]
                    y2 = pos1[1]
                    plt.arrow(float(x1), float(y1), float(x2) - float(x1), float(y2) - float(y1),
                              width=0.00002, head_width=0.0001, linewidth=0.1)
        n = []
        for key in self.graph.get_all_v().keys():
            n.append(key)

        for i, txt in enumerate(n):
            ax.annotate(n[i], (x1_vals[i], y1_vals[i]))
        plt.show()

    def pos_avr(self, x1_vals: list, y1_vals: list):  # return pos
        """
        this function choose x and y for the new position of the node
        :param x1_vals: list of the x values of the position nodes in the graph
        :param y1_vals: list of the y values of the position nodes in the graph
        :return: x and y
        """
        maxX = self.max_posX(x1_vals)
        maxY = self.max_posY(y1_vals)
        minX = self.min_posX(x1_vals)
        minY = self.min_posY(y1_vals)
        rand1 = random.uniform(minX, maxX)
        rand2 = random.uniform(minY, maxY)
        return rand1, rand2

    def max_posX(self, x1_vals: list):
        """
        :param x1_vals: list
        :return: the max value in the given list
        """
        max1 = x1_vals[0]
        for x in x1_vals:
            if x > max1:
                max1 = x
        return max1

    def max_posY(self, y1_vals: list):
        """
        :param y1_vals: list
        :return: the max value in the given list
        """
        max2 = y1_vals[0]
        for y in y1_vals:
            if y > max2:
                max2 = y
        return max2

    def min_posX(self, x1_vals: list):
        """
        :param x1_vals: list
        :return: the min value in the given list
        """
        if x1_vals is None:
            return -1
        min1 = x1_vals[0]
        for x in x1_vals:
            if x < min1:
                min1 = x
        return min1

    def min_posY(self, y1_vals: list):
        """
        :param y1_vals: list
        :return: the min value in the given list
        """
        if y1_vals is None:
            return -1
        min2 = y1_vals[0]
        for y in y1_vals:
            if y < min2:
                min2 = y
        return min2
