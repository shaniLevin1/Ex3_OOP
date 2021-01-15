In this project we implemented weighted directed graph.

when vertex implemented by class called NodeData, which implements the properties and saves the information: each node has:
dictionary (behaves similar to HashMap) of all the connected nodes that going out and coming in to the specific node,
tag, key (specific id) and location.
Each node's location is defined class Position.
the location is defined by x, y, and z values.
Weighted Directed Graph is implemented by class DiGraph.
each graph has dictionary of all the nodes, and extends NodeData class- so each graph has also all the information about the edges in the graph, and supports adding node to the graph, removing node from the graph, ,adding edge, and removing edge as well.
class GraphAlgo implements the algorithms and operations on weighted directed graph.
shortest_path->this method checks what is the shortest way to get from one vertex in the graph to another and returns list of all the nodes in that path.
connected_components->this method finds all the Strongly Connected Component(SCC) in the graph. If the graph is connected the function returns a list of all nodes in the graph.
connected_components(key)->Finds the Strongly Connected Component(SCC) that the first node is a part of by using DFS function; which that goes deep from each node in the graph and checks if any node can reach any other node, then transposes the graph and checks the other direction, splits to component lists if needed, and returns a list of all reachable nodes from the given node.
save_to_json->Saves the graph in JSON format to a file
load_from_json->Loads a graph from a json file.

In order to implement the SCC (Strongly Connected Component) 
