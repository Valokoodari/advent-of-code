pub fn part_1(input: &str) -> String {
    let input = input.trim().parse().unwrap();

    let mut layer = 0;
    while i64::pow(layer * 2 + 1, 2) < input {
        layer += 1;
    }

    let square = i64::pow(layer * 2 + 1, 2);

    let mut side = 0;
    while input < square - (side+1) * (layer*2) {
        side += 1;
    }

    (layer + (input - square + side * (layer*2) + layer).abs()).to_string()
}

pub fn part_2(input: &str) -> String {
    let input = input.trim().parse().unwrap();

    let (mut layer, mut side, mut dist) = (0, 3, 0);
    let mut grid = vec![vec![0; 1000]; 1000];
    let (mut x, mut y) = (500, 500);
    grid[x][y] = 1;

    let lenghts = [-1, 0, 0, 1];
    let moves = [(0, -1), (-1, 0), (0, 1), (1, 0)];
    let neighbors = [(0, -1), (-1, -1), (-1, 0), (-1, 1),
                     (0, 1), (1, 1), (1, 0), (1, -1)];

    while grid[x][y] <= input {
        x = (x as isize + moves[side].0) as usize;
        y = (y as isize + moves[side].1) as usize;

        dist += 1;
        if dist >= layer * 2 + lenghts[side] {
            side = (side + 1) % 4;
            dist = 0;
            if side == 0 {
                layer += 1;
            }
        }

        grid[x][y] = neighbors.iter().map(|&(dx, dy)| grid[(x as isize + dx) as usize][(y as isize + dy) as usize]).sum();
    }

    grid[x][y].to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part_1_test() {
        assert_eq!(part_1("1\n"), "0");
        assert_eq!(part_1("12\n"), "3");
        assert_eq!(part_1("23\n"), "2");
        assert_eq!(part_1("1024\n"), "31");
    }

    #[test]
    fn part_2_test() {
        assert_eq!(part_2("1\n"), "2");
        assert_eq!(part_2("57\n"), "59");
        assert_eq!(part_2("147\n"), "304");
        assert_eq!(part_2("760\n"), "806");
    }
}