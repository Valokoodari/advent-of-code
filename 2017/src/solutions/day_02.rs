pub fn part_1(input: &str) -> String {
    "0".to_string()
}

pub fn part_2(input: &str) -> String {
    "0".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX_0: &str = "\
5 1 9 5
7 5 3
2 4 6 8";

    const EX_1: &str = "\
5 9 2 8
9 4 7 3
3 8 6 5";

    #[test]
    fn part_1_test() {
        assert_eq!(part_1(EX_0), "18");
    }

    #[test]
    fn part_2_test() {
        assert_eq!(part_2(EX_1), "9");
    }
}