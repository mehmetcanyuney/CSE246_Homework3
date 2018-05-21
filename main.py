class Node:
    # initiliazing
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    # basic writing function for testing
    def classp(self):
        print(self.id, end=" ")
        print(self.x, end=" ")
        print(self.y, end=" ")
        print()

    # calculating distance between two node : Euclidian distance
    def distance(self, node):
        dist_x = pow((self.x - node.x), 2)
        dist_y = pow((self.y - node.y), 2)
        result = round(pow(dist_x + dist_y, (1/2)))
        return result


def compute_distance(node1, node2):
    dist_x = pow((node1.x - node2.x), 2)
    dist_y = pow((node1.y - node2.y), 2)
    result = round(pow(dist_x + dist_y, (1 / 2)))
    return result


def greedy_algorithm(nodes):
    solution = []
    free_nodes = nodes[:]
    n = free_nodes[0]
    free_nodes.remove(n)
    solution.append(n)
    total_travel = 0
    while len(free_nodes) > 0:
        min_lenght = None
        min_node = None
        for i in free_nodes:
            lenght = n.distance(i)
            if min_lenght is None:
                min_lenght = lenght
                min_node = i
            elif lenght < min_lenght:
                min_lenght = lenght
                min_node = i
        total_travel += min_lenght
        solution.append(min_node)
        free_nodes.remove(min_node)
        n = min_node
    return solution, total_travel


def opt2(nodes, solution):
    best = 0
    best_move = None
    numberofnodes = len(nodes)

    for first in range(0, numberofnodes):
        for second in range(0, numberofnodes):
            third = (first + 1) % numberofnodes
            fourth = (second + 1) % numberofnodes

            f1 = solution[first]
            s2 = solution[second]
            t3 = solution[third]
            f4 = solution[fourth]

            f1_s2 = compute_distance(f1, s2)
            t3_f4 = compute_distance(t3, f4)
            f1_t3 = compute_distance(f1, t3)
            s2_f4 = compute_distance(s2, f4)

            if second != first and second != third:
                gain = (f1_s2 + t3_f4) - (f1_t3 + s2_f4)
                if gain < best:
                    best_move = (first, third, second, fourth)
                    best = gain

    if best_move is not None:
        (first, third, second, fourth) = best_move
        new_solution = [0 for x in range(numberofnodes)]
        new_solution[0] = solution[first]

        n = 1
        while second != third:
            new_solution[n] = solution[second]
            n = n + 1
            second = (second - 1) % numberofnodes
        new_solution[n] = solution[third]

        n = n + 1
        while first != fourth:
            new_solution[n] = solution[fourth]
            n = n + 1
            fourth = (fourth + 1) % numberofnodes

        return True, new_solution
    else:
        return False, solution


def do_opt2(nodes):
    control = True
    greedy_sol, temp = greedy_algorithm(nodes)
    solution = greedy_sol

    while control:
        control, solution = opt2(nodes, solution)
    return solution


fh = open('Texts\example-input-3.txt', 'r')
rec = fh.readline().rstrip("\n")
temp = 0
nodes = []
while rec != "":
    temp1 = 0
    temp2 = 0
    temp = Node(0, 0, 0)
    for i in range(0, len(rec)):
        if rec[i] == " " or i == len(rec) - 1:
            if temp2 == 0:
                temp.id = int(rec[temp1:i + 1])
                temp1 = i + 1
                temp2 = 1
            elif temp2 == 1:
                temp.x = int(rec[temp1:i + 1])
                temp1 = i + 1
                temp2 = 2
            else:
                temp.y = int(rec[temp1:i + 1])
                temp1 = i + 1
    rec = fh.readline().rstrip("\n")
    nodes.append(temp)

greedy_sol, greedy_total = greedy_algorithm(nodes)

file = open('Texts\greedy_solution1.txt', 'w')
file.write(str(greedy_total) + "\n")

for i in range(0, len(greedy_sol)):
    file.write(str(greedy_sol[i].id) + "\n")


opt2_sol = do_opt2(nodes)

opt2_total = 0
for j in range(0, len(opt2_sol) - 1):
    opt2_total = opt2_total + compute_distance(opt2_sol[j], opt2_sol[j + 1])
opt2_total = opt2_total + compute_distance(opt2_sol[len(opt2_sol)-1], opt2_sol[0])

file = open('Texts\opt2_solution1.txt', 'w')
file.write(str(opt2_total) + "\n")

for i in range(0, len(greedy_sol)):
    file.write(str(opt2_sol[i].id) + "\n")