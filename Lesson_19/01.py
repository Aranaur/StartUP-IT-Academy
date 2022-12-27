import networkx as nx
import matplotlib.pyplot as plt

with open('cities.csv', 'r') as file:
    cities = file.readlines()

cities_replace = [i.replace('\n', '') for i in cities]
cities_split = [i.split(';') for i in cities_replace]
cities_int = [[int(j) if j.isdigit() else j for j in i] for i in cities_split]

g = nx.Graph()

for edge in cities_int:
    g.add_edge(edge[0], edge[1], weight = edge[2])

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos, node_size = 50, font_size = 6)
plt.title("Ukraine Graph")
plt.show()
