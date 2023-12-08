from functools import reduce

with open('2023/input_day8.txt', 'r') as f:
    lines = f.read().splitlines()

directions = lines[0]
num_directions = len(directions)

maps = {}
for node in lines[2:]:
    parent_node = node[:3]
    left_node = node[7:10]
    right_node = node[12:-1]
    maps[parent_node] = (left_node, right_node)

current_node = "AAA"
steps = 0
while current_node!="ZZZ":
    left_node, right_node = maps[current_node]
    current_node = left_node if directions[steps % num_directions] == "L" else right_node
    steps+=1
        
print(steps)


# Part 2
def get_num_steps(node):
    steps = 0
    while not node.endswith("Z"):
        left_node, right_node = maps[node]
        node = left_node if directions[steps % num_directions] == "L" else right_node
        steps+=1
    return steps

current_nodes = [node for node in maps.keys() if node.endswith("A")]
steps_nodes = [get_num_steps(node) for node in current_nodes]

def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a) 
  
def lcm(a,b): 
    return (a // gcd(a,b))* b 

print(reduce(lambda a,b: lcm(a,b), steps_nodes))