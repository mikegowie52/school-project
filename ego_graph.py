from operator import  itemgetter
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    n = 1000
    m = 2
    g = nx.generators.barabasi_albert_graph(n,m)
    node_and_degree = G.degree
    largest_hub,degree=sorted(node_and_degree.items().key=itemgetter(1))[-1]
