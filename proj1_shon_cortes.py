import copy

# ENPM 661 - Planning for Autonomous Robots: 
# Project 1 - Slide puzzle challange
# Shon Cortes

puzzle_size = [4, 4] # MxN grid size

# Test Case 1 "123456089a7cdebf"
test_case_1 = [[1, 2, 3, 4], [5, 6, 0, 8], [9, 'a', 7, 'c'], ['d', 'e', 'b', 'f']]

# Test Case 2 "1034527896abdefc"
test_case_2 = [[1, 0, 3, 4], [5, 2, 7, 8], [9, 6, 'a', 'b'], ['d', 'e', 'f', 'c']]

# Test Case 3 "0234157896bcdaef"
test_case_3 = [[0, 2, 3, 4], [1, 5, 7, 8], [9, 6, 'b', 'c'], ['d', 'a', 'e', 'f']]

# Test Case 4 "162395740ab8defc"
test_case_4 = [[5, 1, 2, 3],[0, 6, 7, 4], [9, 'a', 'b', 8] , ['d', 'e', 'f', 'c']]

# Test Case 5 "162395740ab8defc"
test_case_5 = [[1, 6, 2, 3], [9, 5, 7, 4], [0, 'a', 'b', 8] , ['d', 'e', 'f', 'c']]

goal_state = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 'a', 'b', 'c'], ['d', 'e', 'f', 0]]

def check_blank_pos(node): # Find the x and y position of the "0" space
    y = 0
    x = 0

    for i in range(len(node)):
        for j in range(len(node[i])):
            if node[i][j] == 0:
                x = j
                y = i
    return x, y

def move_up(node, x_00, y_00): # Move blank space up. Takes current puzzle state, x and y positions of the blank space
    x_1 = x_00
    y_1 = y_00-1
    return x_1, y_1

def move_down(node, x_00, y_00): # Move blank space down. Takes current puzzle state, x and y positions of the blank space
    x_1 = x_00
    y_1 = y_00+1
    return x_1, y_1

def move_left(node, x_00, y_00): # blank space left. Takes current puzzle state, x and y positions of the blank space
    x_1 = x_00-1
    y_1 = y_00
    return x_1, y_1

def move_right(node, x_00, y_00): # Move blank space right. Takes current puzzle state, x and y positions of the blank space
    x_1 = x_00+1
    y_1 = y_00
    return x_1, y_1

# Create row-wise string of node
def str_state(node):
    x = ""
    for i in range(len(node)):
        for j in range (len(node[i])):
            x += str(node[i][j])
    return x

# Create column-wise string of node
# def col_print(node):
#     x = ""
#     for i in range(len(node)):
#         for j in range (len(node[i])):
#             x += str(node[j][i])
#     return x

def move_check(node, x_0, y_0, x_1, y_1): # Check if the move is allowed. If it is, add the child node to the visited_list and children_nodes list
    child_node = copy.deepcopy(node)

    # Check if move is possible
    try:
        child_node[y_0][x_0] = child_node[y_1][x_1]
        child_node[y_1][x_1] = 0
    except IndexError:
        return

    # Check if out of puzzle boundary
    if x_1<0 or x_1>puzzle_size[1] or y_1<0 or y_1>puzzle_size[0]:
        return

    # Check if child node has been visited before
    try:
        visited_list.index(str_state(child_node))
    except ValueError:
        visited_list.append(str_state(child_node))
        children_nodes.append(child_node)
    else:
        return

def solve(node): # Solve for the possible paths to the maze
    global parent_nodes
    count = 0 # Number of times the loop is ran
    while len(parent_nodes)!=0:
        
        count+=1

        for i in range(len(parent_nodes)): # Generate children of a parent node

            node = parent_nodes.pop()

            # Check Blank position
            x_0, y_0 = check_blank_pos(node)
            # Try to move up
            x_1 , y_1 = move_up(node, x_0, y_0)
            move_check(node, x_0, y_0, x_1, y_1)
            # Try to move down
            x_1 , y_1 = move_down(node, x_0, y_0)
            move_check(node, x_0, y_0, x_1, y_1)
            # Try to move left
            x_1 , y_1 = move_left(node, x_0, y_0)
            move_check(node, x_0, y_0, x_1, y_1)
            # Try to move right
            x_1, y_1 = move_right(node, x_0, y_0)
            move_check(node, x_0, y_0, x_1, y_1)

        try:
            visited_list.index(str_state(goal_state))
        except ValueError:
            for i in range(len(children_nodes)):
                parent_nodes.append(children_nodes.pop())
        else:
            print("Goal state found!")
            break     

    print("Done Solving")
    print(count)
    

if __name__ == "__main__":

    parent_nodes = []
    children_nodes = []
    
    # Chose initial state from test_case_1 - test_case_5
    test_case = test_case_5
    file = open("nodePath" + "_test_case_5" + ".txt", "a")

    node = copy.deepcopy(test_case)
    parent_nodes.append(node)
    visited_list = [str_state(copy.deepcopy(node))]

    # Call DFS solve function
    solve(node)

    # Generate Output .txt file
    node_path = []
    i = visited_list.index(str_state(goal_state))
    for x in range(i+1):
        node_path.append(visited_list[x])
        
    file.write("Name: nodePath.txt\n")
    file.write("Node explored:\n")
    for element in node_path:
        file.write(element)
        file.write('\n')