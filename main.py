import random
class box():
    """A box class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given board"""

    # Create start and end node
    start_node = box(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = box(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    open_list = []
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    # Loop until you find the end
    while len(open_list) > 0:

        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] == 999:
                continue

            # Create new node
            new_node = box(current_node, node_position)

            # Append
            children.append(new_node)

        # Loop through children
        for child in children:

            # Child is on the closed list
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)



    ## CÓDIGO NOVO ###
listaNum = [1,3,6,999] #terrenos do mapa

l = 5 #variavel da quantidade de linhas do mapa
c = 5 #variavel da quantidade de colunas do mapa
maxBlock = 0 #variavel de limite de terrenos de bloqueio

#criando a matriz do mapa
linha = [0] * (c+2)
mapa = [l] * (l+2)
for i in range(l+2):
    linha = []
    for j in range(c+2):
        linha.append(999)
    mapa[i] = linha

#preenchendo o mapa com os terrenos (aleatoriamente)
for i in range(1,l+1):
    for j in range(1,c+1):
        mapa[i][j] = random.choice(listaNum)

mapa[1][1] = 1000 #definindo ponto inicial com valor 1000
mapa[l][c] = -1 #definindo ponto final com valor -1

#funcao que mostra na tela o mapa
def mostraMapa():
    for i in range(0,l+2):
        for j in range(0,c+2):
            print(f'[{mapa[i][j]:^5}]', end='')
        print()

def main():
    mostraMapa()
    board = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]

    start = (1, 1)
    end = (l, c)

    path = astar(mapa, start, end)
    print(path)


if __name__ == '__main__':
    main()