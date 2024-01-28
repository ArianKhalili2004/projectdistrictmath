import networkx as nx
import matplotlib.pyplot as plt
def hamilton_path(moves, start, path=None):
  # Initialize the path with the start vertex
  if path is None:
    path = [start]
  # Check if the path is complete
  if len(path) == len(moves):
    return path
  # Try each possible next move
  for next_move in moves[start]:
    # Skip the move if it is already in the path
    if next_move in path:
      continue
    # Extend the path with the move and recurse
    extended_path = hamilton_path(moves, next_move, path + [next_move])
    # Return the extended path if it is valid
    if extended_path:
      return extended_path
  # Return None if no valid path is found
  return None

# Create a graph with 5 vertices and some edges
G = nx.Graph()
x = int(input("please enter the number of vertices: "))
verticesList = []
for i in range(x):
  verticesList.append(i)
# havel hakimi one
def is_valid(degree_sequence):
  # Make a copy of the sequence to avoid modifying the original
  sequence = degree_sequence.copy()
  # Loop until a stopping condition is met
  while True:
    # Sort the sequence in non-increasing order
    sequence.sort(reverse=True)
    # Check if all the elements are zero
    if all(x == 0 for x in sequence):
      # The sequence is valid
      return True
    # Get the first element
    k = sequence[0]
    # Remove the first element
    sequence.pop(0)
    # Check if there are enough elements left
    if k > len(sequence):
      # The sequence is invalid
      return False
    # Subtract one from the next k elements
    for i in range(k):
      # Check if the element is positive
      if sequence[i] > 0:
        # Decrement the element
        sequence[i] -= 1
      else:
        # The sequence is invalid
        return False
# print(verticesList)
G.add_nodes_from(verticesList)
y = int(input("please enter the number of edges: "))
edgesList = []
for j in range(y):
  t = (input("enter one of the edge out of "+str(y)+" edges you have: "))
  t = t.replace(" ", "")
  t = int(t)
  m = []
  if 0<t<10:
    m.append(0)
  elif t>=10:
    m.append(int((t-(t%10))/10))
  m.append(t%10)
  newOne = tuple(m)
  edgesList.append(newOne)
  newOne = ()
print(edgesList)
verticesListTwo = []
for i in range(len(verticesList)):
  count = 0
  for j in range(y):
    if edgesList[j][0]== i:
      count+=1
    elif edgesList[j][1] == i:
      count+=1
  verticesListTwo.append(count)
if is_valid(verticesListTwo):
  print("this graph is valid by havel hakimi algorithm!")
else:
  print("this graph is unValid by havel hakimi algorithm!")
G.add_edges_from(edgesList)
# Find a Hamiltonian path in the graph
moves = {node: list(G.neighbors(node)) for node in G.nodes()}
path = hamilton_path(moves, 0)

# Draw the graph and highlight the path
pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path) - 1)], width=8, alpha=0.5, edge_color='r')
plt.show()

