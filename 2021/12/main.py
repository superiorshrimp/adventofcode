from copy import deepcopy

class Vertex:
    def __init__(self, name, edges):
        self.name = name
        self.edges = edges

def ex1(vertices, visited, v):
    if v.name == 'end':
        return 1
    elif visited[v.name]:
        if v.name[0].islower() or v.name == 'start':
            return 0
    s = 0
    for edge in v.edges:
        vis_cpy = deepcopy(visited)
        vis_cpy[v.name] = True
        s += ex1(vertices, vis_cpy, edge)
    return s

def ex2(vertices, visited, v, chosen):
    if v.name == 'end':
        return 1
    elif v.name == 'start' and visited[v.name]:
        return 0
    elif v.name[0].islower() and visited[v.name]:
        if chosen is None:
            chosen = v
        else:
            return 0
    visited[v.name] = True
    s = 0
    for edge in v.edges:
        vis = deepcopy(visited)
        s += ex2(vertices, vis, edge, chosen)
    return s

with open("./12/data.txt", "r") as f:
    edges = f.read().splitlines()
    edges = [edge.split('-') for edge in edges]
    vertices = {}
    visited = {}
    vis = {}
    for (v1,v2) in edges:
        if v1 not in vertices.keys():
            vertices[v1] = Vertex(v1, [])
            visited[v1] = False
            vis[v1] = False
        if v2 not in vertices.keys():
            vertices[v2] = Vertex(v2, [])
            visited[v2] = False
            vis[v2] = False
        vertices[v1].edges.append(vertices[v2])
        vertices[v2].edges.append(vertices[v1])

#i assume there are no 2 big caves connected to one another
print(ex1(vertices, visited, vertices['start']))
print(ex2(vertices, vis, vertices['start'], None))
