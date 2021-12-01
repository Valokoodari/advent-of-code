fn main() {
    let ns: Vec<u32> = std::fs::read_to_string("../inputs/01.in")
        .unwrap()
        .split_whitespace()
        .map(|x| x.parse::<u32>().unwrap())
        .collect();

    println!("Part 1: {}", ns.windows(2).filter(|n| n[1] > n[0]).count());
    println!("Part 2: {}", ns.windows(4).filter(|n| n[3] > n[0]).count());
}