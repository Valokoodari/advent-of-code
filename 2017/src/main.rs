use std::fs;

mod solutions;

const NAMES: [&str; 4] = [
    "Inverse Captcha",
    "Corruption Checksum",
    "Spiral Memory",
    "High-Entropy Passphrases",
];

fn main() {
    for day in 1..NAMES.len()+1 {
        let input = fs::read_to_string(format!("../inputs/2017/{:02}.txt", day)).unwrap();

        let result = match day {
            1 => (solutions::day_01::part_1(&input), solutions::day_01::part_2(&input)),
            2 => (solutions::day_02::part_1(&input), solutions::day_02::part_2(&input)),
            3 => (solutions::day_03::part_1(&input), solutions::day_03::part_2(&input)),
            4 => (solutions::day_04::part_1(&input), solutions::day_04::part_2(&input)),
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