import math

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import GraphRenderer, StaticLayoutProvider, Oval, LabelSet, ColumnDataSource
from bokeh.palettes import Spectral8

from graph import *

graph_data = Graph()
graph_data.debug_create_test_data()

N = len(graph_data.vertexes)
node_indices = list(range(N))

color_list = []
for vertex in graph_data.vertexes:
  color_list.append(vertex.color)


plot = figure(title='Graph Layout Demonstration', x_range=(0, 500), y_range=(0, 500),
              tools='', toolbar_location=None)

graph = GraphRenderer()

graph.node_renderer.data_source.add(node_indices, 'index')
graph.node_renderer.data_source.add(color_list, 'color')
graph.node_renderer.glyph = Oval(height=10, width=10, fill_color='color')

# This is drawing edges from start to end
verts = [vertex for vertex in graph_data.vertexes]
for i in verts:
 start = []
 end = []

for vert in verts:
  for edge in vert.edges:
    start.append(verts.index(vert))
    end.append(verts.index(edge.destination))

graph.edge_renderer.data_source.data = dict(
  start=start,
  end=end)

### start of layout code
x = [v.pos['x'] for v in graph_data.vertexes]
y = [v.pos['y'] for v in graph_data.vertexes]

graph_layout = dict(zip(node_indices, zip(x, y)))
graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

## labels
x = []
y = []
values = []

for vert in verts:
      x.append(vert.pos['x'])
      y.append(vert.pos['y'])
      values.append(vert.value)

source = ColumnDataSource(data=dict(x=x,
                                    y=y,
                                    values=values))

labels = LabelSet(x='x', y='y', text='values', level='glyph',
  x_offset=5, y_offset=5, source=source)

plot.add_layout(labels)

plot.renderers.append(graph)

output_file('graph.html')
show(plot)
