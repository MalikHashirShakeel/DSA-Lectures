from directed_graph import Graph

# g1 = Graph(["A", "B", "C", "D", "E", "F", "G" ,"J" ,"K"])
# g1.add_edge((1 ,"A" ,"B"))
# g1.add_edge((1 ,"A" ,"C"))
# g1.add_edge((1 ,"A" ,"F"))
# g1.add_edge((1 ,"B" ,"C"))
# g1.add_edge((1 ,"B" ,"G"))
# g1.add_edge((1 ,"C" ,"F"))
# g1.add_edge((1 ,"D" ,"C"))
# g1.add_edge((1 ,"E" ,"C"))
# g1.add_edge((1 ,"E" ,"D"))
# g1.add_edge((1 ,"E" ,"J"))
# g1.add_edge((1 ,"F" ,"D"))
# g1.add_edge((1 ,"G" ,"C"))
# g1.add_edge((1 ,"G" ,"E"))
# g1.add_edge((1 ,"J" ,"D"))
# g1.add_edge((1 ,"J" ,"K"))
# g1.add_edge((1 ,"K" ,"E"))
# g1.add_edge((1 ,"K" ,"G"))
# g1.adj_mat()

# # g1.print_graph()
# g1.adj_mat()
# g1.make_adj_table()
# g1.print_adj_table()
# # print(g1.bfs("A" ,"J"))
# # g1.print_adj_table()
# print(g1.dfs("J"))

#-------------------------------------------------------------------------------------------------------------------------\

g2 = Graph(["R" ,"S" ,"T" ,"U"])
g2.add_edge((7 ,"R" ,"R"))
g2.add_edge((5 ,"R" ,"S"))
g2.add_edge((7 ,"S" ,"R"))
g2.add_edge((2 ,"S" ,"U"))
g2.add_edge((3 ,"T" ,"S"))
g2.add_edge((1 ,"U" ,"T"))
g2.add_edge((4 ,"U" ,"R"))

g2.adj_mat()
g2.weight_mat()
g2.path_mat()
g2.spa()
g2.display_shortest_paths()
