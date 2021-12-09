use std::collections::HashMap;

fn fbs(x: usize, y: usize, ps: &Vec<Vec<u8>>, ms: &mut Vec<Vec<(usize, usize)>>) -> (usize, usize) {
    if ms[x][y] != (usize::MAX, usize::MAX) {
        return ms[x][y];
    }

    let mut lp = (x, y);
    if x > 0 && ps[x][y] > ps[x - 1][y] {
        lp = fbs(x - 1, y, ps, ms);
    } else if x < ps.len() - 1 && ps[x][y] > ps[x + 1][y] {
        lp = fbs(x + 1, y, ps, ms);
    } else if y > 0 && ps[x][y] > ps[x][y - 1] {
        lp = fbs(x, y - 1, ps, ms);
    } else if y < ps[x].len() - 1 && ps[x][y] > ps[x][y + 1] {
        lp = fbs(x, y + 1, ps, ms);
    }

    ms[x][y] = lp;
    lp
}

fn main() {
    let ps: Vec<Vec<u8>> = std::fs::read_to_string("inputs/09.in")
        .unwrap()
        .lines()
        .map(|l| l.as_bytes().into_iter().map(|&b| b - b'0').collect())
        .collect();

    let mut bs: HashMap<(usize, usize), u32> = HashMap::new();
    let mut ms: Vec<Vec<(usize, usize)>> =
        vec![vec![(usize::MAX, usize::MAX); ps[0].len()]; ps.len()];

    for x in 0..ps.len() {
        for y in 0..ps[x].len() {
            if ps[x][y] == 9 {
                continue;
            }
            *bs.entry(fbs(x, y, &ps, &mut ms)).or_insert(0) += 1;
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
