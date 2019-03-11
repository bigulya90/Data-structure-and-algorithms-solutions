class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict


# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

dfs(gdict, 'a')


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

dfs(graph, 'C') # {'E', 'D', 'F', 'A', 'C', 'B'}


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


dfs(graph, 'A') # {'E', 'D', 'F', 'A', 'C', 'B'}


def canVisitAllRooms(self, rooms):
    """
    :type rooms: List[List[int]]
    :rtype: bool
    """
    if not rooms:
        return False

    # dictionary to hold all the visited rooms
    visited = {}

    # set first room to visited
    visited[0] = True

    # maintain a stack to hold all the rooms to be visited
    stack = []
    stack.append(0)

    while stack:
        curr = stack.pop()
        # for each key in a room, append in stack if that room is not already visited
        for i in rooms[curr]:
            if i not in visited:
                visited[i] = True
                stack.append(i)
    return len(visited) == len(rooms)
