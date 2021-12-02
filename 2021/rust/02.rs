use std::string::String;

fn main() {
    let cs: Vec<(String, u32)> = std::fs::read_to_string("../inputs/02.in")
        .unwrap()
        .lines()
        .map(|l| {
            let (c, x) = l.split_once(" ").unwrap();
            (c.to_string(), x.parse::<u32>().unwrap())
        })
        .collect();

    let (mut h, mut d, mut a) = (0, 0, 0);
    for (c, x) in cs {
        match &c as &str {
            "forward" => {
                h += x;
                d += a * x;
            }
            "down" => a += x,
            "up" => a -= x,
            _ => {}
        }
    }

    println!("Part 1: {}\nPart 2: {}", a * h, d * h);
}
