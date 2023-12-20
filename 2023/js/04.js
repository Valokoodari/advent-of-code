let input = await Bun.file("../../inputs/2023/04/input.txt").text();
input = input.trimEnd().replaceAll(/\ +/g, " ");
let [a, ss] = [0, new Object()];

input.split("\n").map((r) => {
  let [g, ns] = r.split(": ");
  g = parseInt(g.split(" ")[1]);
  let [ws, os] = ns
    .split(" | ")
    .map((s) => new Set(s.split(" ").map((n) => parseInt(n))));
  let h = ws.intersection(os).size;
  if (h > 0) a += 2 ** (h - 1);
  if (!(g in ss)) ss[g] = 1;
  for (let i = 1; i <= h; i++) {
    if (!(g + i in ss)) ss[g + i] = 1;
    ss[g + i] += ss[g];
  }
});

console.log("Day 4 - Scratchcards");
console.log("  Part 1:", a);
console.log(
  "  Part 2:",
  Object.values(ss).reduce((a, b) => a + b, 0)
);
