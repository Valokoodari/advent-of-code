let d = await Bun.file("../../inputs/2023/03.txt").text();
let gs = d.trimEnd().split("\n");

const isDigit = (c) => c >= "0" && c <= "9";

const NS = [
  [-1, -1],
  [-1, 0],
  [-1, 1],
  [0, -1],
  [0, 1],
  [1, -1],
  [1, 0],
  [1, 1],
];

let [a1, a2, vs] = [0, 0, new Set()];
for (let r = 0; r < gs.length; r++) {
  for (let c = 0; c < gs[r].length; c++) {
    if (gs[r][c] != "." && !isDigit(gs[r][c])) {
      let [nc, m] = [0, 1];
      NS.forEach(([dr, dc]) => {
        if (
          0 <= r + dr &&
          r + dr < gs.length &&
          0 <= c + dc &&
          c + dc < gs[r].length &&
          isDigit(gs[r + dr][c + dc]) &&
          !vs.has((r + dr) * 1000 + c + dc)
        ) {
          vs.add((r + dr) * 1000 + c + dc);
          nc += 1;
          let [pv, nv, n] = [true, true, [gs[r + dr][c + dc]]];
          for (let i = 1; i < 3; i++) {
            if (nv && isDigit(gs[r + dr][c + dc - i])) {
              vs.add((r + dr) * 1000 + c + dc - i);
              n = [gs[r + dr][c + dc - i]].concat(n);
            } else {
              nv = false;
            }
            if (pv && isDigit(gs[r + dr][c + dc + i])) {
              vs.add((r + dr) * 1000 + c + dc + i);
              n = n.concat([gs[r + dr][c + dc + i]]);
            } else {
              pv = false;
            }
          }
          a1 += parseInt(n.join(""));
          m *= parseInt(n.join(""));
        }
      });
      if (gs[r][c] == "*" && nc == 2) {
        a2 += m;
      }
    }
  }
}

console.log("Day 3: Gear Ratios");
console.log("  Part 1:", a1);
console.log("  Part 2:", a2);
