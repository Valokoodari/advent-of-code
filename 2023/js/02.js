const LS = new Map([
  ["red", 12],
  ["green", 13],
  ["blue", 14],
]);

let input = await Bun.file("../../inputs/2023/02/input.txt").text();
input = input.trimEnd().replaceAll(";", ",");
let [a, b] = [0, 0];

input.split("\n").forEach((line) => {
  let cs = new Map([
    ["red", 0],
    ["green", 0],
    ["blue", 0],
  ]);
  let [g, ss] = line.split(": ");
  let v = true;
  ss.split(", ").forEach((s) => {
    let [n, c] = s.split(" ");
    cs.set(c, Math.max(cs.get(c), parseInt(n)));
    if (LS.get(c) < parseInt(n)) {
      v = false;
    }
  });
  a += v ? parseInt(g.split(" ")[1]) : 0;
  b += cs.get("red") * cs.get("green") * cs.get("blue");
});

console.log("Day 2: Cube Conundrum");
console.log("  Part 1:", a);
console.log("  Part 2:", b);
