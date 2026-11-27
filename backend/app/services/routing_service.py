from collections import deque

def shortest_path(grid, start, goal):
    queue = deque([start]); previous = {start: None}
    while queue:
        point = queue.popleft()
        if point == goal: break
        r, c = point
        for nxt in ((r+1,c),(r-1,c),(r,c+1),(r,c-1)):
            nr, nc = nxt
            if nr < 0 or nc < 0 or nr >= len(grid) or nc >= len(grid[nr]) or nxt in previous: continue
            if grid[nr][nc].get("type") not in {"lane", "entrance", "exit", "slot"}: continue
            previous[nxt] = point; queue.append(nxt)
    if goal not in previous: return []
    path=[]; point=goal
    while point is not None: path.append(point); point=previous[point]
    return list(reversed(path))
