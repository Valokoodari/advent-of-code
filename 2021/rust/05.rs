fn main() {
    let cs: Vec<(i32, i32, i32, i32)> = std::fs::read_to_string("../../inputs/2021/05.txt")
        .unwrap()
        .lines()
        .map(|l| {
            let ps: Vec<i32> = l
                .replace(" -> ", ",")
                .split(",")
                .map(|x| x.parse::<i32>().unwrap())
                .collect();
            (ps[0], ps[1], ps[2], ps[3])
        })
        .collect();

    let max = cs
        .iter()
        .cloned()
        .map(|(a, b, c, d)| i32::max(a, i32::max(b, i32::max(c, d))))
        .max()
        .unwrap() as usize;

    let mut a1 = vec![vec![0; max + 1]; max + 1];
    let mut a2 = vec![vec![0; max + 1]; max + 1];

    for (ax, ay, bx, by) in cs {
        let mx = if (ax - bx) != 0 {
            (ax - bx) / i32::abs(ax - bx)
        } else {
            0
        };
        let my = if (ay - by) != 0 {
            (ay - by) / i32::abs(ay - by)
        } else {
            0
        };

        for i in 0..i32::max(i32::abs(ax - bx), i32::abs(ay - by)) + 1 {
            if mx == 0 || my == 0 {
                a1[(bx + i * mx) as usize][(by + i * my) as usize] += 1;
            }
            a2[(bx + i * mx) as usize][(by + i * my) as usize] += 1;
        }
    }

    println!(
        "Part 1: {}",
        a1.iter()
            .map(|r| r.iter().filter(|&n| *n > 1).count())
            .sum::<usize>()
    );
    println!(
        "Part 2: {}",
        a2.iter()
            .map(|r| r.iter().filter(|&n| *n > 1).count())
            .sum::<usize>()
    );
}
