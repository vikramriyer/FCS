#!/usr/bin/python

#init
GRAPH =  [[0, 1, 0, 1, 1],
          [0, 0, 1, 0, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0]]

#global vars
NROWS = len(GRAPH)
NCOLS = len(GRAPH[0])
VISITED = [[0]*NROWS]*NCOLS
GROUP = {}
POSSIBLE_NODES = [(i,j) for i in range(NROWS) for j in range(NCOLS)]

#functions
def get_possible_nodes(i, j):
  adjacent_nodes = [(i-1,j-1),  (i, j-1),  (i+1, j-1),  (i-1, j),  (i+1, j),  (i-1, j+1),  (i, j+1),  (i+1, j+1)]
  final_adjacent_nodes = []
  for tuple in adjacent_nodes:
    if tuple in POSSIBLE_NODES:
      final_adjacent_nodes.append(tuple)

  return final_adjacent_nodes

def get_adjacent_nodes(i, j):
  #return {1: [i-1,j-1], 2: [i, j-1], 3: [i+1, j-1], 4: [i-1, j], 5: [i+1, j], 6: [i-1, j+1], 7: [i, j+1], 8: [i+1, j+1]}  
  local_group = []
  if GRAPH[i][j] == 1: #if the current node is 1, then only search for adjacent nodes
    adjacent_nodes = get_possible_nodes(i, j)
    for node in adjacent_nodes:
      if GRAPH[node[0]][node[1]] == 1 and not is_visited(node[0],node[1]): #1 in graph and not yet visited
        mark_visited(node[0],node[1])



def is_visited(i, j):
  if VISITED[i, j] == 1
    return True
  return False

def mark_visited(i, j):
  VISITED[i][j] = 1

def get_total_connected_components(row, col):
  adjacent_nodes = get_adjacent_nodes(row, col)

#driver code
for row in range(NROWS):
  for col in range(NCOLS):
    get_total_connected_components(row, col)
    #print "Total connected components are: {}".format(get_total_connected_components(row, col))
