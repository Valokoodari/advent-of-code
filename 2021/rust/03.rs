fn fos(ns: &Vec<Vec<bool>>) -> Vec<usize> {
    let mut os = vec![0; ns[0].len()];
    for n in ns {
        for i in 0..n.len() {
            if n[i] {
                os[i] += 1;
            }
        }
    }
    os
}

fn ftn(os: &Vec<bool>) -> u32 {
    let mut n = 0;
    for v in os {
        n = (n << 1) + if *v { 1 } else { 0 };
    }
    n
}

fn main() {
    let ns: Vec<Vec<bool>> = std::fs::read_to_string("../../inputs/2021/03.txt")
        .unwrap()
        .lines()
        .map(|l| l.chars().map(|c| c == '1').collect())
        .collect();

    let os = fos(&ns);

    let (mut g, mut e) = (0, 0);

    for i in 0..os.len() {
        if os[i] > ns.len() / 2 {
            g = (g << 1) + 1;
            e <<= 1;
        } else {
            g <<= 1;
            e = (e << 1) + 1;
        }
    }

    let mut n1 = ns.clone();
    let mut n2 = ns.clone();
    for i in 0..os.len() {
        let (o1, o2) = (fos(&n1), fos(&n2));
        n1 = n1
            .iter()
            .cloned()
            .filter(|n| {
                n[i] == (o1[i]
                    >= if n1.len() % 2 == 1 {
                        n1.len() / 2 + 1
                    } else {
                        n1.len() / 2
                    })
                    || n1.len() == 1
            })
            .collect();
        n2 = n2
            .iter()
            .cloned()
            .filter(|n| {
                n[i] != (o2[i]
                    >= if n2.len() % 2 == 1 {
                        n2.len() / 2 + 1
                    } else {
                        n2.len() / 2
                    })
                    || n2.len() == 1
            })
            .collect();
    }

    println!("Part 1: {}\nPart 2: {}", g * e, ftn(&n1[0]) * ftn(&n2[0]));
}
