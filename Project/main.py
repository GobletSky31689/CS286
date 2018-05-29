import igraph as ig
import numpy as np
import random
import matplotlib.pyplot as plt

# g = ig.Graph.Read_Ncol("DataSets/netscience.txt")
# g = ig.Graph.Read_Ncol("DataSets/email.txt")
g = ig.Graph.Read_Ncol("DataSets/example.txt", directed=False)

# print g.summary()

n_values = {}
q_values = {}
l_values = {}
for n in g.vs:
    x = set()
    for i in n.neighbors():
        x.add(i)
        for j in i.neighbors():
            x.add(j)
    x.add(n)
    x.remove(n)
    n_values[n.index] = len(x)
for n in g.vs:
    q_values[n.index] = 0
    for i in n.neighbors():
        q_values[n.index] += n_values[i.index]
for n in g.vs:
    l_values[n.index] = 0
    for i in n.neighbors():
        l_values[n.index] += q_values[i.index]
# print l_values

tmp = [0] * len(g.vs)
for k in n_values:
    tmp[k] = n_values[k]
g.vs["n_value"] = tmp

tmp = [0] * len(g.vs)
for k in q_values:
    tmp[k] = q_values[k]
g.vs["q_value"] = tmp

tmp = [0] * len(g.vs)
for k in l_values:
    tmp[k] = l_values[k]
g.vs["l_value"] = tmp


g.write_gml('example.gml')


# def local_central(node):
#     return l_values[node["name"]]
#
#
# local = []
# for item in g.vs:
#     item["name"] = item.index
#     local.append(item)
# local.sort(key=local_central)
#
#
# def sir_model2(starting_node):
#     k = np.mean(g.degree())
#     is_infected = {}
#     for node in g.vs:
#         is_infected[node] = False
#     infected = []
#     recovered = []
#     infected.append(starting_node)
#     t = 0
#     # print 'Time Tick:', t, 'Infected:', len(infected), 'Recovered', len(recovered)
#     while len(infected) != 0 and t <= 10:
#         new_infected = set()
#         for infected_node in infected:
#             n = [i for i in infected_node.neighbors() if not is_infected[i]]
#             if len(n) != 0:
#                 x = random.choice(n)
#                 new_infected.add(x)
#                 # is_infected[x] = True
#                 # infected.append(x)
#             if random.random() <= 1.0/k:
#                 recovered.append(infected_node)
#                 infected.remove(infected_node)
#         for n_node in new_infected:
#             is_infected[n_node] = True
#             infected.append(n_node)
#         t += 1
#         # print 'Time Tick:', t, 'Infected:', len(infected), 'Recovered', len(recovered)
#     # print 'Node:', starting_node["name"], 'Total time:', t, 'F(t):', len(recovered)
#     return len(set(recovered)) + len(set(infected))
#
#
# f_s = []
# l_s = []
# d_s = []
# c_s = []
# b_s = []
# for item in local:
#     f = 0.0
#     trials = 100
#     for i in range(trials):
#         f += sir_model2(item)
#     print 'Node:', item["name"], 'F(t):', f/trials, 'L-Cent:', l_values[item["name"]]
#     f_s.append(f/trials)
#     l_s.append(l_values[item["name"]])
#     d_s.append(item.degree())
#     c_s.append(item.closeness())
#     b_s.append(item.betweenness())
#
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))
# ax1.scatter(x=l_s, y=f_s, marker='o', c='r', edgecolor='b')
# ax1.set_xlabel('$Local Centrality$')
# ax1.set_yscale('log')
# ax1.set_xscale('log')
# ax1.set_ylabel('$F(t)$')
#
# ax2.scatter(x=d_s, y=f_s, marker='o', c='r', edgecolor='b')
# ax2.set_xlabel('$Degree Centrality$')
# ax2.set_yscale('log')
# ax2.set_xscale('log')
# ax2.set_ylabel('$F(t)$')
#
# ax3.scatter(x=c_s, y=f_s, marker='o', c='r', edgecolor='b')
# ax3.set_xlabel('$Closeness Centrality$')
# ax3.set_yscale('log')
# ax3.set_xscale('log')
# ax3.set_ylabel('$F(t)$')
#
# ax4.scatter(x=b_s, y=f_s, marker='o', c='r', edgecolor='b')
# ax4.set_xlabel('$Betweenness Centrality$')
# ax4.set_yscale('log')
# ax4.set_xscale('log')
# ax4.set_ylabel('$F(t)$')
# ax4.set_xlim([1, 100000])
#
# fig.tight_layout()
#
# plt.show()
