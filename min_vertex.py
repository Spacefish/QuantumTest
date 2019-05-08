import numpy as np
import networkx as nx
import dwave_networkx as dnx
import matplotlib.pyplot as plt
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

mygraph = nx.dense_gnm_random_graph(20,40)

pos=nx.circular_layout(mygraph)

sampler = EmbeddingComposite(DWaveSampler())
result = dnx.min_vertex_cover(mygraph, sampler)

print(result)

nx.draw_networkx_nodes(mygraph,pos, with_labels=True)
nx.draw_networkx_nodes(mygraph,pos, with_labels=True, node_color='r', nodelist=result)
nx.draw_networkx_edges(mygraph, pos)

plt.show()
