#bonus
import networkx as nx
import matplotlib.pyplot as plt
#G = nx.barabasi_albert_graph(1000, 4)
G = nx.erdos_renyi_graph(100,0.5)
nx.draw(G, with_labels=True)
plt.savefig("graph.png")
# разбираемся с хабами
dict_hub = {}
for node in G.nodes:
	number_edges = G.degree(node)
	dict_hub[node] = number_edges
dict_hub = sorted(list(dict_hub.items()), key = lambda x: x[1])
for i in dict_hub[-1:-10:-1]:
	print(i)
print('----')
# greedy algorithm by Charikar
density_subgraph_list = []
def density_subgraph(graph):
	return len(graph.edges)/(len(graph.nodes))
for i in dict_hub[:-1]:
	G.remove_node(i[0])
	H_i = G.copy()	
	density_subgraph_list.append((H_i, density_subgraph(H_i)))
density_subgraph_list = sorted(density_subgraph_list, key = lambda x: x[1], reverse = True)
for g in density_subgraph_list[:10]:
	print(g)