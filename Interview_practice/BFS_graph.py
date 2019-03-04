from collections import deque


def bfs(graph, start, end):
    if start not in graph:
        raise Exception('Start node not in graph')

    if end not in graph:
        raise Exception('End node not in graph')

    visited = {start: None}
    node_to_visit = deque()
    node_to_visit.append(start)

    while node_to_visit:
        cur = node_to_visit.popleft()

        if cur == end:
            return path(visited, start, end)

        for neighbor in graph[cur]:
            if neighbor not in visited:
                node_to_visit.append(neighbor)
                visited[neighbor] = cur

    return None


def path(visited, start, end):
    short_path = []

    cur = end

    while cur:
        short_path.append(cur)
        cur = visited[cur]

    short_path.reverse()
    return short_path


