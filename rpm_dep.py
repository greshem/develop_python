
from operator import itemgetter
import networkx as nx
from networkx import *

import matplotlib.pyplot as plt

G=nx.Graph()

#G.add_edge('a','b')
#G.add_edge('a','c')
#G.add_edge('c','d')
#G.add_edge('c','e')
#G.add_edge('c','f')
#G.add_edge('a','d')

#tmpt 来自  /root/bin/q_rpm_depends_as4.sh   里面的 关系部分,  数据部分自己 处理一下. 

file_object = open('tmpt')
try:
    lines = file_object.readlines()
    for line in lines:
       # print type(lines)   
        line=line.strip();
        words = line.split(' ')
        if len(words) <2:
            continue
        #emotionDictionary[words[0]] = words[1]
        G.add_edge(words[0], words[1])
finally:
    file_object.close( )


pathlengths=[]

node_and_degree=G.degree()
print("source vertex {target:length, }")
for v in G.nodes():
    spl=single_source_shortest_path_length(G,v)
    #./networkx/algorithms/shortest_paths/generic.py:                paths=nx.
    spl2=single_source_shortest_path(G,v);
    #print('%s|->| %s' % (v,spl))
    print('%s|->| %s' % (v,spl2))
    #print('%s' % (v))
    for p in spl.values():
        pathlengths.append(p)

print('')
print("average shortest path length %s" % (sum(pathlengths)/len(pathlengths)))



#(largest_hub,degree)=sorted(node_and_degree.items(),key=itemgetter(1))[-1]
# Create ego graph of main hub
#hub_ego=nx.ego_graph(G,largest_hub)
# Draw graph
#pos=nx.spring_layout(hub_ego)
#nx.draw(hub_ego,pos,node_color='b',node_size=50,with_labels=False)
# Draw ego as large and red
#nx.draw_networkx_nodes(hub_ego,pos,nodelist=[largest_hub],node_size=300,node_color='r')
#plt.savefig('ego_graph.png')
#plt.show()
