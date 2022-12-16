use std::fs;

mod solutions;

const NAMES: [&str; 2] = [
    "Inverse Captcha",
    "Corruption Checksum",
];

fn main() {
    for day in 1..3 {
        let input = fs::read_to_string(format!("../inputs/2017/{:02}.txt", day)).unwrap();

        let result = match day {
            1 => (solutions::day_01::part_1(&input), solutions::day_01::part_2(&input)),
            2 => (solutions::day_02::part_1(&input), solutions::day_02::part_2(&input)),
            _ => panic!("Invalid day"),
        };

        println!("Day {}: {} ({})", day, NAMES[day as usize - 1], "TODO");
        println!("  Part 1: {}", result.0);
        println!("  Part 2: {}", result.1);
        println!("  ({}) [{} / {}]\n", "TODO", "TODO", "TODO");
    }

    println!("Time:");
    println!("  sum: {} ms", "TODO");
    println!("  avg: {} ms", "TODO");
}