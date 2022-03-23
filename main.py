import heapq
from tkinter import *
from queue import PriorityQueue
from heapq import heappush, heappop
from itertools import count
from tkinter import font

import networkx as nx
import matplotlib.pyplot as plt
from networkx.algorithms.shortest_paths.weighted import _weight_function




# declaration of directed and undirected graphs
G = nx.Graph()
Gi = nx.DiGraph()


# declaration of variables
node1 = " "  # node_from
node2 = " "  # node_to
node3 = " "  # node_with_heuristic
heur_dic = {}  # heuristic_dictionary
edge = 0
output_bfs = " "
output_dfs = " "
output_ucs = " "
output_greedy = " "
output_Astar = " "
output_bfs_directed = " "
output_dfs_directed = " "
output_ucs_directed = " "
output_greedy_directed = " "
output_Astar_directed = " "
heuristic = " "
node = " "
index = " "
start_node = " "
goal_node = []
edge_weight = {}
edge_weight_directed = {}
main_window = Tk()

myFont = font.Font(family='Helvetica', size=15, weight='bold')
# Labels
Label(main_window, text=" Add node start: ", font=myFont).grid(row=1, column=0)
Label(main_window, text=" Path is:  ", font=myFont).grid(row=1, column=7)
Label(main_window, text=" Add node end: ", font=myFont).grid(row=2, column=0)
Label(main_window, text=" Add weight: ",font=myFont).grid(row=3, column=0)
Label(main_window, text=" Add start of graph: ", font=myFont).grid(row=4, column=0)
Label(main_window, text=" Add goals of graph:  ", font=myFont).grid(row=5, column=0)
Label(main_window, text=" Add node_heuristic: ",font=myFont ).grid(row=6, column=0)
Label(main_window, text=" Add heuristic: ",font=myFont).grid(row=7, column=0)
Label(main_window, text=" UnDirected Graph ",font=myFont).grid(row=12, column=0)
Label(main_window, text=" Choose method of search:  ").grid(row=10, column=0)
Label(main_window, text=" Directed Graph ",font=myFont).grid(row=8, column=0)
Label(main_window, text=" Choose method of search:  ").grid(row=14, column=0)

# Text Input Entry
e1 = Entry(main_window, width=15, borderwidth=3)
e1.grid(row=1, column=1, columnspan=4, padx=30)

e2 = Entry(main_window, width=15, borderwidth=3)
e2.grid(row=2, column=1, columnspan=4, padx=30)

e3 = Entry(main_window, width=15, borderwidth=3)
e3.grid(row=3, column=1, columnspan=4, padx=30)

e4 = Entry(main_window, width=15, borderwidth=3)
e4.grid(row=4, column=1, columnspan=4, padx=30)

e5 = Entry(main_window, width=15, borderwidth=3)
e5.grid(row=5, column=1, columnspan=4, padx=30)

e6 = Entry(main_window, width=15, borderwidth=3)
e6.grid(row=6, column=1, columnspan=4, padx=30)

e7 = Entry(main_window, width=15, borderwidth=3)
e7.grid(row=7, column=1, columnspan=4, padx=30)


# function to input node_from and node_to and the weight on the edge between them for directed and undirected graph
def nodestart_input():
    global node1, node2, weight, edge_weight, edge_weight_directed
    node1 = e1.get()
    e1.delete(0, END)
    node2 = e2.get()
    e2.delete(0, END)
    weight = e3.get()
    e3.delete(0, END)
    Gi.add_weighted_edges_from([(node1, node2, weight)])
    G.add_weighted_edges_from([(node1, node2, weight)])
    edge_weight[node1 + node2] = weight
    edge_weight[node2 + node1] = weight
    edge_weight_directed[node1 + node2] = weight
    print(edge_weight)


# function to input the heuristic of each node and push it into a heuristic dictionary to save this data
def node_heruristic():
    global node3, heuristic
    node3 = e6.get()
    e6.delete(0, END)
    heuristic = e7.get()
    e7.delete(0, END)
    heur_dic[node3] = int(heuristic)
    print(heur_dic)


# function to take the start node of the search
def add_start_node():
    global start_node
    start_node = e4.get()
    e4.delete(0, END)


# function to take the goal nodes of the Search
def add_goal_node():
    global goal_node
    goal_node.append(e5.get())
    e5.delete(0, END)


# function to draw the  undirected graph
def drawgraph():
    # nx.draw_networkx_nodes(G, node_size=400)
    # nx.draw_networkx_edges(G, edgelist=G.edges(), edge_color='black')
    # plt.show()
    for node in G.nodes():
        print(node)
        print(edge)

    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=400)
    nx.draw_networkx_edges(G, pos, edgelist=G.edges, edge_color='black')
    nx.draw_networkx_labels(G, pos)
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()


# function to draw the  directed graph
def drawgraph_directed():
    # nx.draw_networkx_nodes(G, node_size=400)
    # nx.draw_networkx_edges(G, edgelist=G.edges(), edge_color='black')
    # plt.show()
    for node in Gi.nodes():
        print(node)
        print(edge)

    pos = nx.spring_layout(Gi)
    nx.draw_networkx_nodes(Gi, pos, node_size=400)
    nx.draw_networkx_edges(Gi, pos, edgelist=Gi.edges, edge_color='black')
    nx.draw_networkx_labels(Gi, pos)
    labels = nx.get_edge_attributes(Gi, "weight")
    nx.draw_networkx_edge_labels(Gi, pos, edge_labels=labels)
    plt.show()


def bfs():  # function for BFS
    global output_bfs, start_node, goal_node
    visited = {node: False for node in G.nodes}  # List for visited nodes and set them as false
    queue = [start_node]  # push the first node in the queue
    visited[start_node] = True  # mark the first node in the queue as visited

    while queue:  # Creating loop to visit each node
        outt = queue.pop(0)  # pop the first node from the queue
        output_bfs = output_bfs + outt

        for i in goal_node:  # check if the node current is the goal or not
            if outt == i:
                lb = Label(main_window, text=output_bfs).grid(row=7, column=7)  # if yes then print the path
                return

        for node in G.neighbors(outt):  # loop on the neighboors of this current node
            if not visited[node]:  # check if they are vistied
                visited[node] = True
                queue.append(node)  # if yes , then mark them as visited and push them in the queue


def bfs_directed():  # function for BFS
    global output_bfs_directed, start_node, goal_node
    visited = {node: False for node in Gi.nodes}  # List for visited nodes.
    queue = [start_node]
    visited[start_node] = True

    while queue:  # Creating loop to visit each node
        outt = queue.pop(0)
        output_bfs_directed = output_bfs_directed + outt

        for i in goal_node:
            if outt == i:
                lb = Label(main_window, text=output_bfs_directed).grid(row=2, column=7)
                return

        for node in Gi.successors(outt):
            if not visited[node]:
                visited[node] = True
                queue.append(node)


def dfs():
    global output_dfs, start_node, goal_node
    visited = {node: False for node in G.nodes}  # firstly mark all the visited nodes as false
    stack = [start_node]  # push the start node in the stack

    while len(stack):  # checking on the length of the stack to be not empty
        s = stack[-1]
        stack.pop()  # pop the node from the stack and put in the path
        output_dfs = output_dfs + s

        for i in goal_node:  # loop on the list of goals and check if the popped node is a goal node or not
            if s == i:  # and if it is a goal node print it and stop
                lb2 = Label(main_window, text=output_dfs).grid(row=8, column=7)
                return

        if not visited[s]:
            visited[s] = True

        for nextt in G.neighbors(s):
            if not visited[nextt]:
                stack.append(nextt)


def dfs_directed():
    global output_dfs_directed, start_node, goal_node
    visited = {node: False for node in Gi.nodes}
    stack = [start_node]

    while len(stack):
        s = stack[-1]
        stack.pop()
        output_dfs_directed = output_dfs_directed + s

        for i in goal_node:
            if s == i:
                lb2 = Label(main_window, text=output_dfs_directed).grid(row=3, column=7)
                return

        if not visited[s]:
            visited[s] = True

        for nextt in Gi.successors(s):
            if not visited[nextt]:
                stack.append(nextt)


def ucs():
    global start_node, goal_node, edge_weight, output_ucs
    visited = []
    queue = PriorityQueue()  # define a Priority queue to ascend the variables in ascending order
    queue.put((0, start_node))  # put the first node in it

    while not queue.empty():  # loop if the queue is not empty
        item = queue.get()
        nextt = item[1]  # name the node next
        output_ucs = output_ucs + nextt  # add the next node to the path

        for i in goal_node:  # check if the node is in the goal list
            if nextt == i:  # if it is in the list
                lb3 = Label(main_window, text=output_ucs).grid(row=9, column=7)
                queue.queue.clear()  # if yes then clear the queue
                return

        visited.append(nextt)

        for neighbour in G.neighbors(nextt):  # check on the neighbours of the node
            if neighbour not in visited:  # if not visited, mark them as visited and put them in the queue with weight
                queue.put((edge_weight[nextt + neighbour], neighbour))


def ucs_directed():
    global start_node, goal_node, edge_weight_directed, output_ucs_directed
    visited = []
    queue = PriorityQueue()
    queue.put((0, start_node))

    while not queue.empty():
        item = queue.get()
        nextt = item[1]
        output_ucs_directed = output_ucs_directed + nextt

        for i in goal_node:
            if nextt == i:
                lb3 = Label(main_window, text=output_ucs_directed).grid(row=4, column=7)
                queue.queue.clear()
                return

        visited.append(nextt)

        for neighbour in Gi.successors(nextt):
            if neighbour not in visited:
                queue.put((edge_weight_directed[nextt + neighbour], neighbour))


def greedy():
    global start_node, goal_node, heur_dic, output_greedy
    visited = []
    queue = PriorityQueue()  # define a Priority queue to ascend the variables in ascending order
    queue.put((heur_dic[start_node], start_node))  # put the first node in it with its heuristic

    while not queue.empty():  # loop if the queue is not empty
        item = queue.get()
        nextt = item[1]  # name the node next
        output_greedy = output_greedy + nextt  # add the next node to the path

        for i in goal_node:  # check if the node is in the goal list
            if nextt == i:  # if it is in the list
                lb4 = Label(main_window, text=output_greedy).grid(row=10, column=7)
                queue.queue.clear()  # if yes then clear the queue
                return

        visited.append(nextt)

        for neighbour in G.neighbors(nextt):  # check on the neighbours of the node
            if neighbour not in visited:  # if not visited, mark them as visited and put the next in the queue
                queue.put((heur_dic[neighbour], neighbour))  # and also put the heuristic of the next with it


def greedy_directed():
    global start_node, goal_node, heur_dic, output_greedy_directed
    visited = []
    queue = PriorityQueue()
    queue.put((heur_dic[start_node], start_node))

    while not queue.empty():
        item = queue.get()
        nextt = item[1]
        output_greedy_directed = output_greedy_directed + nextt

        for i in goal_node:
            if nextt == i:
                lb4 = Label(main_window, text=output_greedy_directed).grid(row=5, column=7)
                queue.queue.clear()
                return

        visited.append(nextt)

        for neighbour in Gi.successors(nextt):
            if neighbour not in visited:
                queue.put((heur_dic[neighbour], neighbour))


def A_star():
    global start_node, goal_node, heur_dic, output_Astar, edge_weight
    visited = []
    queue = PriorityQueue()  # define a Priority queue to ascend the variables in ascending order
    queue.put((heur_dic[start_node], start_node))  # put the first node in it with its heuristic and weight of the edge

    while not queue.empty():  # loop if the queue is not empty
        item = queue.get()
        nextt = item[1]  # name the node next
        output_Astar = output_Astar + nextt  # add the next node to the path

        for i in goal_node:  # check if the node is in the goal list
            if nextt == i:  # if it is in the list
                lb4 = Label(main_window, text=output_Astar).grid(row=11, column=7)
                queue.queue.clear()  # if yes then clear the queue
                return

        visited.append(nextt)

        for neighbour in G.neighbors(nextt):  # check on the neighbours of the node
            if neighbour not in visited:  # if not visited, mark them as visited and put the next in the queue
                cost = int(heur_dic[neighbour]) + int(edge_weight[nextt + neighbour])
                queue.put((cost, neighbour))  # define the total cost as heuristic + weighted edge
                # place the cost at the queue


def A_star_directed():
    global start_node, goal_node, heur_dic, output_Astar_directed, edge_weight_directed
    visited = []
    queue = PriorityQueue()
    queue.put((heur_dic[start_node], start_node))

    while not queue.empty():
        item = queue.get()
        nextt = item[1]
        output_Astar_directed = output_Astar_directed + nextt

        for i in goal_node:
            if nextt == i:
                lb4 = Label(main_window, text=output_Astar_directed).grid(row=6, column=7)
                queue.queue.clear()
                return

        visited.append(nextt)

        for neighbour in Gi.successors(nextt):
            if neighbour not in visited:
                cost = int(heur_dic[neighbour]) + int(edge_weight_directed[nextt + neighbour])
                queue.put((cost, neighbour))


# buttons addnode,addweight,addheuristic
addweight = Button(main_window, text="Add", padx=20, pady=20, command=lambda: nodestart_input()).grid(row=2, column=4)
addstart = Button(main_window, text="Add", padx=20, pady=20, command=lambda: add_start_node()).grid(row=4, column=4)
addgoal = Button(main_window, text="Add", padx=20, pady=20, command=lambda: add_goal_node()).grid(row=5, column=4)
addheuristic = Button(main_window, text="Add", padx=20, pady=20, command=lambda: node_heruristic()).grid(row=6,
                                                                                                         column=4)

# buttons to draw the graph either directed or undirected
draw = Button(main_window, text="Draw_undirected", padx=20, pady=20, command=lambda: drawgraph()).grid(row=12, column=2)
draw_directed = Button(main_window, text="Draw_directed", padx=20, pady=20, command=lambda: drawgraph_directed()).grid(
    row=8, column=2)

# buttons to choose the algorithms made for undirected graph
bfs = Button(main_window, text="bfs", padx=20, pady=20, command=bfs).grid(row=14, column=2)
dfs = Button(main_window, text="dfs", padx=20, pady=20, command=dfs).grid(row=14, column=3)
ucs = Button(main_window, text="ucs", padx=20, pady=20, command=ucs).grid(row=14, column=4)
A_star = Button(main_window, text="A*", padx=20, pady=20, command=A_star).grid(row=14, column=6)
greedy = Button(main_window, text="Greedy", padx=20, pady=20, command=greedy).grid(row=14, column=5)

# buttons to choose the algorithms made for directed graph
bfs_directed = Button(main_window, text="bfs", padx=20, pady=20, command=bfs_directed).grid(row=10, column=2)
dfs_directed = Button(main_window, text="dfs", padx=20, pady=20, command=dfs_directed).grid(row=10, column=3)
ucs_directed = Button(main_window, text="ucs", padx=20, pady=20, command=ucs_directed).grid(row=10, column=4)
A_star_directed = Button(main_window, text="A*", padx=20, pady=20, command=A_star_directed).grid(row=10, column=6)
greedy_directed = Button(main_window, text="Greedy", padx=20, pady=20, command=greedy_directed).grid(row=10, column=5)

main_window.mainloop()
