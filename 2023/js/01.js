let input = await Bun.file("../../inputs/2023/01.txt").text();
input = input.trimEnd();

const solve = (data) => {
  data = data.split("\n");
  let sum = 0;
  data.forEach((l) => {
    let ds = [];
    [...l].forEach((c) => {
      if (c >= "0" && c <= "9") {
        ds.push(c);
      }
    });
    sum += parseInt(ds[0] + ds.splice(-1));
  });
  return sum;
};

console.log("Day 1: Trebuchet?!");
console.log("  Part 1:", solve(input));

[
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine",
].forEach(
  (v, i) => (input = input.replaceAll(v, v[0] + (i + 1) + v.slice(-1)))
);
console.log("  Part 2:", solve(input));
