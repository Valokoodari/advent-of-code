pub fn part_1(input: &str) -> String {
    input.lines().map(|l| {
        let mut words = l.split_whitespace().collect::<Vec<&str>>();
        let len = words.len();
        words.sort();
        words.dedup();
        (len == words.len()) as u32
    }).sum::<u32>().to_string()
}

pub fn part_2(input: &str) -> String {
    input.lines().map(|l| {
        let mut words = l.split_whitespace().map(|s| s.to_string()).collect::<Vec<String>>();
        let len = words.len();
        for i in 0..len {
            words[i] = {
                let mut chars = words[i].chars().collect::<Vec<char>>();
                chars.sort();
                chars.into_iter().collect::<String>()
            };
        }
        words.sort();
        words.dedup();
        (len == words.len()) as u32
    }).sum::<u32>().to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const EX_0: &str = "\
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa";

    const EX_1: &str = "\
abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio";

    #[test]
    fn part_1_test() {
        assert_eq!(part_1(EX_0), "2");
    }

    #[test]
    fn part_2_test() {
        assert_eq!(part_2(EX_1), "3");
    }
}