//usr/bin/true; rustc -o "/tmp/$0.bin" 1>&2 "$0" && "/tmp/$0.bin" "$@"; exit $?
use std::fs;

fn main() {
    let mut path = Vec::new();
    let mut dirs = std::collections::HashMap::new();

    fs::read_to_string("../inputs/07.txt")
        .unwrap()
        .trim()
        .split("\n")
        .for_each(|l| {
            match l.split(" ").collect::<Vec<&str>>()[..] {
                ["$", "cd", "/"] => {
                    path = Vec::new();
                }
                ["$", "cd", ".."] => {
                    path.pop();
                }
                ["$", "cd", dir] => path.push(dir),
                ["$" | "dir", ..] => (),
                [size, _] => {
                    (0..path.len() + 1).for_each(|i| {
                        *dirs.entry(path[..i].join("/")).or_insert(0) += size
                            .parse::<u64>()
                            .unwrap();
                    });
                }
                _ => (),
            }
        });

    println!(
        "Part 1: {}",
        dirs
            .values()
            .filter(|&&s| s <= 100_000)
            .sum::<u64>()
    );

    println!(
        "Part 2: {}",
        dirs
            .values()
            .filter(|&&s| 70_000_000 - dirs.values().max().unwrap() + s >= 30_000_000)
            .min()
            .unwrap()
    );
}