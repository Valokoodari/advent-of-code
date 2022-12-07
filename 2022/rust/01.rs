//usr/bin/true; rustc -o "/tmp/$0.bin" 1>&2 "$0" && "/tmp/$0.bin" "$@"; exit $?
use std::fs;

fn main() {
    let mut cs = fs
        ::read_to_string("../inputs/01.txt")
        .unwrap()
        .trim()
        .split("\n\n")
        .map(|p| {
            p.split("\n")
                .map(|n| n.parse::<u64>().unwrap())
                .sum::<u64>()
        })
        .collect::<Vec<u64>>();

    cs.sort_by(|a, b| b.cmp(a));

    println!("Part 1: {}", cs[0]);
    println!("Part 2: {}", cs.iter().take(3).sum::<u64>())
}