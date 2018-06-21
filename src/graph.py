import random


class Edge:
  def __init__(self, destination, weight='1'):
    self.destination = destination
    self.weight = weight

class Vertex:
  def __init__(self, value='default', **pos):
    self.value = value
    self.color = 'white'
    self.pos = pos
    self.edges = []

class Graph:
  def __init__(self):
    self.vertexes = []

  def debug_create_test_data(self):
    debug_vertex_1 = Vertex('t1', x=100, y=120)
    debug_vertex_2 = Vertex('t2', x=120, y=140)
    debug_vertex_3 = Vertex('t3', x=400, y=40)

    debug_edge_1 = Edge(debug_vertex_2)
    debug_edge_2 = Edge(debug_vertex_3)
    debug_vertex_1.edges.append(debug_edge_1)
    debug_vertex_2.edges.append(debug_edge_2)

    self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3])

  def bfs(self, start):
    random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])

    queue = []
    found = []

    queue.append(start)
    found.append(start)

    start.color = random_color

    while len(queue) > 0:
      v = queue[0]
      for edge in v.edges:
        if edge.destination not in found:
          found.append(edge.destination)
          queue.append(edge.destination)
          edge.destination.color = random_color
      queue.pop(0)

    return found

  def randomize(self, width, height, size, probability):
    def connectVerts(v0, v1):
      v0.edges.append(Edge(v1))
      v1.edges.append(Edge(v0))

    count = 0
    buffer_size = 30

    for y in range(buffer_size, height - buffer_size, size):
      for x in range(buffer_size, width - buffer_size, size):
          if random.randint(0, 315) < probability * 100:
            value = "v" + str(count)
            new_vert = Vertex(
              value,
              x=x,
              y=y,
              )
            self.vertexes.append(new_vert)
            count+= 1
    
    for v in self.vertexes:
      # Connect randomly
        if random.randint(0, 14) < probability * 100:
          index = self.vertexes.index(v)
          nums = list(range(0,index - 1)) + list(range(index + 1, len(self.vertexes)))
          random_destination = random.choice(nums)
          connectVerts(v, self.vertexes[random_destination])

  def connect_components(self, graph):
    searched = []

    for v in graph.vertexes:
      if v not in searched:
        subgraph = self.bfs(v)
        for ver in subgraph:
          searched.append(ver)

