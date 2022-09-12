from collections import deque

def bfs(graph, start, visited):   
    queue = deque([start])                #while에서 큐가 빌때까지 진행 > 한개 넣어줌
    visited[start] = True                 #방문 표시
    while queue:
        v = queue.popleft()               #제일 처음꺼 빼서 넣기
        print(v, end=' ')                 #프린트
        for i in graph[v]:                #연결노드 가서
            if not visited[i]:            #방문 안했으면 다 큐에 챙기기
                queue.append(i)
                visited[i] = True

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False] * 9

bfs(graph, 1, visited)