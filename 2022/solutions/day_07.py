def parse(data):
    path, dirs = [], {}
    for l in data.splitlines():
        match l.split():
            case ["$", "cd", "/"]:
                path = []
            case ["$", "cd", ".."]:
                path.pop()
            case ["$", "cd", n]:
                path.append(n)
            case ["$", _]:
                pass
            case ["dir", _]:
                pass
            case [s, _]:
                for i in range(len(path)+1):
                    dirs["/".join(path[:i])] = dirs.get("/".join(path[:i]), 0) + int(s)
    return dirs


def part_1(data):
    return sum(s for s in parse(data).values() if s <= 100000)

def part_2(data):
    return [sorted(s for s in ds.values() if 70000000 - ds[""] + s >= 30000000)[0] for ds in [parse(data)]][0]


EX_0 = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

def test():
    assert part_1(EX_0) == 95437
    assert part_2(EX_0) == 24933642


if __name__ == "__main__":
    test()
