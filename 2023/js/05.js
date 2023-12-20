let d = await Bun.file("../../inputs/2023/05/input.txt").text();
let ps = d.trimEnd().split("\n\n");
let ss = ps[0]
  .split(": ")[1]
  .split(" ")
  .map((n) => parseInt(n));
let ms = ps.slice(1).map((p) =>
  p
    .split("\n")
    .slice(1)
    .map((l) => l.split(" ").map((n) => parseInt(n)))
);
let rs = ss
  .reduce((r, _, i, a) => {
    if (i % 2 == 0) r.push(a.slice(i, i + 2));
    return r;
  }, [])
  .map((r) => [r[0], r[0] + r[1] - 1]);

let a1 = Math.min(
  ...ss.map((s) => {
    ms.forEach((m) => {
      for (let i = 0; i < m.length; i++) {
        if (m[i][1] <= s && s < m[i][1] + m[i][2]) {
          s += m[i][0] - m[i][1];
          break;
        }
      }
    });
    return s;
  })
);

ms.forEach((m) => {
  let [nrs, crs] = [[], []];
  m.forEach((v) => {
    crs = [];
    rs.forEach((r) => {
      if (!(r[0] >= v[1] + v[2] || r[1] < v[1])) {
        let [a, b] = [Math.max(v[1], r[0]), Math.min(v[1] + v[2] - 1, r[1])];
        nrs.push([a + v[0] - v[1], b + v[0] - v[1]]);
        if (r[0] < a) crs.push([r[0], a - 1]);
        if (r[1] > b) crs.push([b + 1, r[1]]);
      } else {
        crs.push(r);
      }
    });
    rs = crs;
  });
  rs = crs.concat(nrs);
});

console.log("Day 5: You Give A Seed A Fertilizer");
console.log("  Part 1:", a1);
console.log("  Part 2:", Math.min(...rs.map((r) => r[0])));
