# By starting at the top of the triangle below
# and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
# Find the maximum total from top to bottom of the triangle below:
# (see input file)
import sys
import queue


class Node:
    def __init__(self, value):
        self.value = -int(value)
        self.distance = 0
        self.adjacent = []

    def print_node(self):
        print('node value: {}'.format(self.value))
        for node in self.adjacent:
            print('adjacent value: {}'.format(node.value))


def read_file(path, nodes):
    file = open(path, 'r')
    for i, line in enumerate(file):
        nodes.append([])
        numbers = line.split()
        for number in numbers:
            nodes[i].append(Node(number))


def max_weight_path(nodes):
    while nodes:
        temp = nodes.pop()


def main():
    nodes = []
    nodeQueue = queue.PriorityQueue()
    read_file(sys.argv[1], nodes)
    nodes[0][0].distance = 75
    for i, row in enumerate(nodes):     # these loops set up all the adjacencies
        for j, node in enumerate(row):  # between nodes
            try:
                node.adjacent.append(nodes[i+1][j])
                node.adjacent.append(nodes[i+1][j+1])
            except IndexError:
                pass
            nodeQueue.put(nodes[i][j])
    max_weight_path(nodes)
    while nodeQueue.not_empty:
        print(nodeQueue.get().value)
if __name__ == '__main__':
    main()