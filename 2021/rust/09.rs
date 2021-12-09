use std::collections::HashMap;

fn fbs(x: usize, y: usize, ps: &Vec<Vec<u8>>) -> (usize, usize) {
    if x > 0 && ps[x][y] > ps[x - 1][y] {
        fbs(x - 1, y, ps)
    } else if x < ps.len() - 1 && ps[x][y] > ps[x + 1][y] {
        fbs(x + 1, y, ps)
    } else if y > 0 && ps[x][y] > ps[x][y - 1] {
        fbs(x, y - 1, ps)
    } else if y < ps[x].len() - 1 && ps[x][y] > ps[x][y + 1] {
        fbs(x, y + 1, ps)
    } else {
        (x, y)
    }
}

fn main() {
    let ps: Vec<Vec<u8>> = std::fs::read_to_string("inputs/09.in")
        .unwrap()
        .lines()
        .map(|l| l.as_bytes().into_iter().map(|&b| b - b'0').collect())
        .collect();

    let mut bs: HashMap<(usize, usize), u32> = HashMap::new();

    for x in 0..ps.len() {
        for y in 0..ps[x].len() {
            if ps[x][y] == 9 {
                continue;
            }
            *bs.entry(fbs(x, y, &ps)).or_insert(0) += 1;
        }
    }

    let mut ss: Vec<u32> = bs.values().cloned().collect();
    ss.sort();

    println!(
        "Part 1: {}",
        bs.keys()
            .cloned()
            .into_iter()
            .map(|(x, y)| ps[x][y] as u32 + 1)
            .sum::<u32>()
    );
    println!("Part 2: {}", ss.into_iter().rev().take(3).product::<u32>());
}
