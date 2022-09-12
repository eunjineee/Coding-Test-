def dfs(graph, v, visited):   
    visited[v] = True                 #방문 표시
    print(v, end=' ')                 #프린트
    for i in graph[v]:                #연결노드 가서
        if not visited[i]:            #False이면
            dfs(graph, i, visited)    #다시 함수 속으로..

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

dfs(graph, 1, visited)