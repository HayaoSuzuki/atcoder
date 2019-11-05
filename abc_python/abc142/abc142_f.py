import enum
import collections


class Status(enum.Enum):
    NEW = enum.auto()
    ACTIVE = enum.auto()
    FINISHED = enum.auto()


N, M = tuple(map(int, input().split(" ")))
vertices = dict((v, Status.NEW) for v in range(1, N + 1))
edges = []
for _ in range(M):
    edges.append(tuple(map(int, input().split(" "))))


def is_acyclic(V: dict):
    for v, status in V.items():
        if status == Status.NEW:
            if is_acyclic_dfs(v) is False:
                return False
    return True


def is_acyclic_dfs(v):
    vertices[v] = Status.ACTIVE
    for e in edges:
        if vertices[e[1]] == Status.ACTIVE:
            print(vertices)
            print(e)
            return False
        elif vertices[e[1]] == Status.NEW:
            if is_acyclic_dfs(e[1]) is False:
                return False
    vertices[v] = Status.FINISHED
    return True


# print(vertices)
# print(edges)
print(is_acyclic(vertices))
# print(vertices)
