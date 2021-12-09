fn main() {
    let mut ns: Vec<i32> = std::fs::read_to_string("inputs/07.in")
        .unwrap()
        .split(",")
        .map(|n| n.parse::<i32>().unwrap())
        .collect();
    ns.sort();

    let m = ns.iter().sum::<i32>() / ns.len() as i32;

    println!(
        "Part 1: {}\nPart 2: {}",
        ns.iter()
            .copied()
            .map(|n| i32::abs(n - ns[ns.len() / 2]))
            .sum::<i32>(),
        ns.iter()
            .copied()
            .map(|n| (0..(i32::abs(n - m) + 1)).sum::<i32>())
            .sum::<i32>()
    )
}
