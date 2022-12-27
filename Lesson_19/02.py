import networkx as nx

with open('cities.csv', 'r') as file:
    cities = file.readlines()

cities_replace = [i.replace('\n', '') for i in cities]
cities_split = [i.split(';') for i in cities_replace]
cities_int = [[int(j) if j.isdigit() else j for j in i] for i in cities_split]

g = nx.Graph()

for edge in cities_int:
    g.add_edge(edge[0], edge[1], weight = edge[2])

def min_path(graph, start, end):
    path = nx.shortest_path(graph, start, end, weight='weight')
    len_path = nx.shortest_path_length(graph, start, end, weight='weight')
    print(f"From {start} to {end} shortest path will take: \n"
          f"- {len_path} km \n"
          f"- your path is: {path}")
    return path, len_path

min_path(g, 'Kyiv', 'Lviv')
