pub fn part_1(input: &str) -> String {
    input.lines().map(|l| {
        let mut sum = 0;
        for i in 0..l.len() {
            if l.chars().nth(i).unwrap() == l.chars().nth((i + 1) % l.len()).unwrap() {
                sum += l.chars().nth(i).unwrap().to_digit(10).unwrap();
            }
        }
        sum
    }).sum::<u32>().to_string()
}

pub fn part_2(input: &str) -> String {
    input.lines().map(|l| {
        let mut sum = 0;
        for i in 0..l.len() {
            if l.chars().nth(i).unwrap() == l.chars().nth((i + l.len() / 2) % l.len()).unwrap() {
                sum += l.chars().nth(i).unwrap().to_digit(10).unwrap();
            }
        }
        sum
    }).sum::<u32>().to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn part_1_test() {
        assert_eq!(part_1("1122"), "3");
        assert_eq!(part_1("1111"), "4");
        assert_eq!(part_1("1234"), "0");
        assert_eq!(part_1("91212129"), "9");
    }

    #[test]
    fn part_2_test() {
        assert_eq!(part_2("1212"), "6");
        assert_eq!(part_2("1221"), "0");
        assert_eq!(part_2("123425"), "4");
        assert_eq!(part_2("123123"), "12");
        assert_eq!(part_2("12131415"), "4");
    }
}