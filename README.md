# Ex3_OOP:
## In this project we implemented weighted directed graph and algorithms.
Each graph has vertexes, that implemented by class Node_Data, and each vertex has position which implemented by class Position which defined by 3 values-x,y,z.

## Classes:

## NodeData
The vertex implemented by class called NodeData, which implements the properties and saves the information: each node has:
dictionary (behaves similar to HashMap) of all the connected nodes that going out and coming in to the specific node,
tag, key (specific id) and location.

## Position
Each node's location is defined class Position.
the location is defined by x, y, and z values.

## DiGraph
Weighted Directed Graph is implemented by class DiGraph.
Each graph has dictionary of all the nodes, and extends NodeData class- so each graph has also all the information about the edges in the graph, and supports adding node to the graph, removing node from the graph, ,adding edge, and removing edge as well.

## GraphAlgo
class GraphAlgo implements the algorithms and operations on weighted directed graph.
#### shortest_path->
This method checks what is the shortest way to get from one vertex in the graph to another one, and returns list of all the nodes in that path. That function uses Dijkastra algorithm-
the idea of that algorithm is:
first treats to all the nodes as unvisited, then starts with putting the first node in a stack and in the list to be return –
then pops the first element from the stack, and while the stack is not empty the function does:
if the poped item has edges out from it – considers which "choice" is the best- by asking the question which neighbor's weight + the road's distance that the node has until now is the shortest one and adds it to a list, puts the neighbors in the stack and repeats the process until the stack is empty.
#### connected_components->
this method finds all the Strongly Connected Component(SCC) in the graph. If the graph is connected the function returns a list of all nodes in the graph.### connected_components(key)->
Finds the Strongly Connected Component(SCC) that the first node is a part of by using DFS function; which that goes deep from each node in the graph and checks if any node can reach any other node, then transposes the graph and checks the other direction, splits to component lists if needed, and returns a list of all reachable nodes from the given node.
#### connected_component(key)->
Finds the Strongly Connected Component(SCC) that the first node is a part of by using DFS function, which that goes deep from each node in the graph and checks if any node can reach any other node, then transposes the graph and checks the other direction, in order to make sure which nodes can reach others and all the way back, then splits to component lists if needed,(by checking which nodes are also in the list of the regular DFS list, so it means that they could be reached one way and now the path back is been checked),
then returns a list of all reachable nodes from the given node(using inclusion exclusion principle in order not to repeat elements).

#### save_to_json->
Saves the graph in JSON format to a file
#### load_from_json->
Loads a graph from a json file.

#### plot_graph->
In this function we use matplotlib in order to draw the graph according the positions of the nodes, and the edges we draw as arrows from src to dest of the edge.
If there is a a node with no position there is an algorithm that define new random position according the range of the max and min positions in the graph.


