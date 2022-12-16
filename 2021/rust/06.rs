fn main() {
    let ns: Vec<usize> = std::fs::read_to_string("../../inputs/2021/06.txt")
        .unwrap()
        .split(",")
        .map(|n| n.parse::<usize>().unwrap())
        .collect();

    let mut fs = [0; 9];
    for i in 0..9 {
        fs[i] = ns.iter().filter(|&n| *n == i).count();
    }

    let mut nfs = [0; 9];
    for d in 0..256 {
        for i in 0..9 {
            nfs[i] = fs[(i + 1) % 9];
        }
        nfs[6] += nfs[8];
        fs = nfs;

        if d == 79 {
            println!("Part 1: {}", fs.iter().map(|n| *n as u32).sum::<u32>());
        }
    }

    println!("Part 2: {}", fs.iter().map(|n| *n as u64).sum::<u64>());
}
