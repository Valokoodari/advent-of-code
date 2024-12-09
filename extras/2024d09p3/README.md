# 2024 Day 9 Part 3

After running the improved hard drive compacter just once, you notice that there are still large gaps left between some of the files. It's clear that some the
gaps are still large enough for files after them on the hard drive to fit in them so you should probably run the compacter a couple more times.

On the first example a second run would still move one more file resulting in larger contiguous free space:
```
00992111777.44.333....5555.6666.....8888..
00992111777.44.33388885555.6666...........
```
A third run however would not do anything so just **2 runs** of the compacter are required.

After the second run the **index of last used block** on the hard drive is **30**.

**Multiplying** the index of the last used block by **100** and **adding** the amount of **runs** required for optimal compaction on the first example gives
the result of `30 * 100 + 2 = 3002`.

Compacting the amphipod's hard drive until no more changes are made, **what is the index of the last used block on the hard drive? And how many times does the
hard drive compacter need to be run?**

Answer should be given as last used index times 100 + how many runs are required.
