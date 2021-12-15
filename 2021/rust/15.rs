use std::cmp::Reverse;
use std::collections::BinaryHeap;

fn fds(cs: &Vec<Vec<u8>>) -> u32 {
    let mut ms = vec![vec![u32::MAX; cs[0].len()]; cs.len()];
    let mut ts = BinaryHeap::new();
    ts.push(Reverse((0, (0, 0))));

    while let Some(Reverse((r, (x, y)))) = ts.pop() {
        if x + 1 == cs.len() as i32 && y + 1 == cs[0].len() as i32 {
            return r;
        }

        for (dx, dy) in [(0, 1), (0, -1), (1, 0), (-1, 0)] {
            if 0 <= x + dx && x + dx < cs.len() as i32 && 0 <= y + dy && y + dy < cs[0].len() as i32 {
                let nr = r + cs[(x + dx) as usize][(y + dy) as usize] as u32;
                if nr < ms[(x + dx) as usize][(y + dy) as usize] {
                    ms[(x + dx) as usize][(y + dy) as usize] = nr;
                    ts.push(Reverse((nr, (x + dx, y + dy))));
                }
            }
        }
    }

    0
}

fn main() {
    let cs: Vec<Vec<u8>> = std::fs::read_to_string("inputs/15.in")
        .unwrap()
        .lines()
        .map(|l| l.bytes().map(|b| b - b'0').collect())
        .collect();

    println!("Part 1: {}", fds(&cs));

    let mut ncs = vec![vec![0; cs[0].len() * 5]; cs.len() * 5];
    for i in 0..cs.len() * 5 {
        for j in 0..cs[0].len() * 5 {
            ncs[i][j] = cs[i % cs.len()][j % cs[0].len()] + (i / cs.len()) as u8 + (j / cs[0].len()) as u8;
            if ncs[i][j] > 9 {
                ncs[i][j] -= 9;
            }
        }
    }

    println!("Part 2: {}", fds(&ncs));
}
