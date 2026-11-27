export function shortestPath(grid, start, goal) {
  const key = (p) => `${p.r},${p.c}`;
  const queue = [start], previous = new Map([[key(start), null]]);
  while (queue.length) {
    const p = queue.shift();
    if (p.r === goal.r && p.c === goal.c) break;
    for (const [dr, dc] of [[1,0],[-1,0],[0,1],[0,-1]]) {
      const n = { r: p.r + dr, c: p.c + dc }, cell = grid[n.r]?.[n.c];
      if (!cell || !['lane','entrance','exit','slot'].includes(cell.type) || previous.has(key(n))) continue;
      previous.set(key(n), key(p)); queue.push(n);
    }
  }
  if (!previous.has(key(goal))) return [];
  const path = []; let at = key(goal);
  while (at) { const [r,c] = at.split(',').map(Number); path.unshift({r,c}); at = previous.get(at); }
  return path;
}
