"""
General drawing methods for graphs using Bokeh.
"""

from bokeh.io import show, output_file
from bokeh.plotting import figure
from bokeh.models import (GraphRenderer, StaticLayoutProvider, Oval, Circle, LabelSet,
                          ColumnDataSource, LinearColorMapper)
import math
from bokeh.palettes import Spectral8
from bokeh.transform import linear_cmap
from random import choices, randint, randrange, random
from itertools import cycle
from decimal import Decimal


class BokehGraph:
    """Class that takes a graph and exposes drawing methods."""
    def __init__(self, graph):
        self.graph = graph

    node_indices = list(self.graph.vertices.keys())
    N = len(node_indices)

    edges = []
    for i in node_indices:
        l = list(self.graph.vertices[i])
        edges.extend(list(zip(l, cycle([i])) if len(l) > len([i]) else zip(cycle(l), [i])))
    print(edges)

    graph = GraphRenderer()

    graph.node_renderer.data_source.add(node_indices, 'index')
    graph.node_renderer.data_source.add(Spectral8, 'color')

    color_dict = {}
    for i in node_indices:
        color_dict[i] = 'red'
    graph.node_renderer.glyph = Oval(height=N*0.02, width=N*0.02, fill_color='color')

    graph.edge_renderer.data_source.data = dict(
        start=[i[0] for i in edges],
        end=[i[1] for i in edges])
    print(graph.edge_renderer.data_source.data)

    x = [random()*10 for _ in range(0, N)]
    y = [random()*10 for _ in range(0, N)]

    plot = figure(title='Graph Layout Demonstration', x_range=(min(x)-1, max(x)+1), y_range=(min(y)-1, max(y)+1),
                  tools='', toolbar_location=None)

    graph_layout = dict(zip(node_indices, zip(x, y)))
    graph.layout_provider = StaticLayoutProvider(graph_layout=graph_layout)

    plot.renderers.append(graph)
    
    def show_graph():
      output_file('graph.html')
      show(plot)
