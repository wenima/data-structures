
def build_graph(d, weight=0):
    weighted_g = Graph()
    for k, v in d.items():
        for edge in v:
            weighted_g.add_edge(k, edge, randint(1, 10))
    return weighted_g

def find_shortest_path(source):
    distances[source] = 0
    for step in range(len(g.nodes()) -1):
        for n in g._nodes:
            for v in g._nodes[n]:
                relax(n, v)
    check_neg_weight(g)

def relax(source, edge):
    t, w = edge
    alt = distances[source] + w
    if distances[t] > alt:
        distances[t] = alt
        parents[t] = source
        return True
    return False

def check_neg_weight(g):
    for k, v in g._nodes.items():
        t, w = v
        if distance[t] > distance[k] + w:
            raise ValueError("negative cycle detected") as e
    return e

def path(source, target):
    t = target
    s = source
    if s == t:
        return [s]
    elif parents[t] is None:
        raise ValueError("no path to target")
    else:
        return path(s, parents[t]) + [t]

simple_graph_scaffold = {
                        'A': ['B', 'C'],
                        'B': ['C', 'D'],
                        'C': ['D'],
                        'D': ['E'],
                        'E': ['F'],
                        'F': ['D']
                        }

from random import randint

g = build_graph(simple_graph_scaffold)
parents = {node: None for node in g._nodes}
distances = {node: float("inf") for node in g._nodes}
source = None
