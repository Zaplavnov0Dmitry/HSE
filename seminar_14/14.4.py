#Zaplavnov 14.4
import networkx as nx
from tqdm import tqdm
vertexes = 10
N = 100000
euler_graph = 0
for i in tqdm(range(N)):
	graph = nx.gnp_random_graph(vertexes, 0.5)
	if nx.is_eulerian(graph):
		euler_graph += 1
print(euler_graph/N)