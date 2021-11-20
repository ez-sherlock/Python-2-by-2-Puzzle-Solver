initialState = [0, 3, 2, 1]
goalState = [1, 2, 3, 0]

queue = []
visited = []


def compareNodes(node1, node2):
    if node1 == node2:
        return True
    else:
        return False


def interChangeValues(node, interChangeValue1, interChangeValue2):
    temp = node[interChangeValue1]
    node[interChangeValue1] = 0
    node[interChangeValue2] = temp
    return node


def moveUp(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 2:
        return interChangeValues(nodeCopy, 0, 2)
    elif node.index(0) == 3:
        return interChangeValues(nodeCopy, 1, 3)


def moveDown(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 0:
        return interChangeValues(nodeCopy, 2, 0)
    elif node.index(0) == 1:
        return interChangeValues(nodeCopy, 3, 1)


def moveRight(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 0:
        return interChangeValues(nodeCopy, 1, 0)
    elif node.index(0) == 2:
        return interChangeValues(nodeCopy, 3, 2)


def moveLeft(node):
    nodeCopy = []
    for x in node:
        nodeCopy.append(x)
    if node.index(0) == 1:
        return interChangeValues(nodeCopy, 0, 1)
    elif node.index(0) == 3:
        return interChangeValues(nodeCopy, 2, 3)


def performOpoerations(queue, node, opr1, opr2):
    temp1 = opr1(node)
    temp2 = opr2(node)
    if temp1 not in visited:
        queue.append(temp1)
    if temp2 not in visited:
        queue.append(temp2)


def puzzle(queue, initialState, visited, goalState):
    queue.append(initialState)
    global found
    found = False
    while(queue):
        node = queue.pop(0)
        last = node
        visited.append(node)
        if compareNodes(node, goalState):
            found = True
            break
        else:
            indexOfZero = node.index(0)
            if indexOfZero == 0:
                performOpoerations(queue, node, moveDown, moveRight)
            elif indexOfZero == 1:
                performOpoerations(queue, node, moveLeft, moveDown)
            elif indexOfZero == 2:
                performOpoerations(queue, node, moveUp, moveRight)
            elif indexOfZero == 3:
                performOpoerations(queue, node, moveLeft, moveUp)


puzzle(queue, initialState, visited, goalState)
print(visited)

if found:
    lengthOfVisited = int(len(visited))
    print(lengthOfVisited)
    if lengthOfVisited % 2 == 0:
        print("---------")
        print("| {} | {} |".format(visited[0][0], visited[0][1]))
        print("| {} | {} |".format(visited[0][2], visited[0][3]))
        print("---------")
        print("\n")
        for x in range(1, lengthOfVisited, 2):
            print("---------")
            print("| {} | {} |".format(visited[x][0], visited[x][1]))
            print("| {} | {} |".format(visited[x][2], visited[x][3]))
            print("---------")
            print("\n")
    else:
        for x in range(0, lengthOfVisited, 2):
            print(" ---------")
            print("*| {} | {} |".format(visited[x][0], visited[x][1]))
            print(" | {} | {} |".format(visited[x][2], visited[x][3]))
            print(" ---------")
            print("\n")


else:
    print("The given pattern cannot be formed.")
