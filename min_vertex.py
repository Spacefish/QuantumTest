import networkx as nx
import dwave_networkx as dnx
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

mygraph = nx.star_graph(4)

sampler = EmbeddingComposite(DWaveSampler())
result = dnx.min_vertex_cover(mygraph, sampler)

print(result)
