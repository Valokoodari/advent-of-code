# Advent of Code 2024

This year I'll be solving the puzzles of [Advent of Code](https://adventofcode.com/2024) with Python 3.13 but I will
unfortunately not be able to compete this year due to work.  

## Personal Stats (AoC time)
```
      --------Part 1--------   --------Part 2--------   -----Delta-----
Day       Time   Rank  Score       Time   Rank  Score       Time   Rank
  1   00:04:30   1666      0   00:06:23   1316      0   00:01:53   -350
* 2   03:09:30  28421      0   03:18:17  19249      0   00:08:47  -9163
* 3   02:21:15  24794      0   02:25:31  19264      0   00:04:16  -5530
* 4   02:22:58  18267      0   02:27:36  15056      0   00:04:38  -3211
  5   00:09:19   1158      0   00:18:42   1368      0   00:09:23    210
  6   00:11:00   1379      0   00:20:11    746      0   00:09:11   -633
  7   00:07:11    840      0   00:08:45    572      0   00:01:34   -268
  8   00:11:00    871      0   00:15:20    690      0   00:04:20   -181
  9   00:12:21    725      0   00:22:23    273      0   00:10:02   -452
 10   00:06:00    406      0   00:07:52    341      0   00:01:52    -65
 11   00:06:15    931      0   00:08:59    254      0   00:02:44   -677
 12   00:03:19    170      0   00:21:18    195      0   00:17:59     25
*13   02:33:29  10309      0   02:38:46   6782      0   00:05:17  -3527
 14   00:08:37    451      0   00:14:35     75     26   00:05:58   -376
 15   00:24:39   1487      0   00:35:58    197      0   00:10:59  -1290
 16   00:02:44    102      0   00:19:00    242      0   00:16:16    140
-----------------------------------------------------------------------
Sum   01:46:55      -      0   03:19:06      -     26   01:31:11      -
Avg   00:08:55    849      0   00:16:36    522      2   00:07:41   -326

* Excluded from the sum and average

Total points: 26
Global rank: 759 (updated on 16th)
```

## Personal Stats (Solve time)
```
Day   -Part 1-   -Part 2-   --Delta-
  1   00:04:30   00:06:23   00:01:53
* 2   00:09:30   00:18:17   00:08:47
* 3   00:06:15   00:10:31   00:04:16
* 4   00:07:58   00:12:36   00:04:38
  5   00:09:19   00:18:42   00:09:23
  6   00:11:00   00:20:11   00:09:11
  7   00:07:11   00:08:45   00:01:34
  8   00:11:00   00:15:20   00:04:20
  9   00:12:21   00:22:23   00:10:02
 10   00:06:00   00:07:52   00:01:52
 11   00:06:15   00:08:59   00:02:44
 12   00:03:19   00:21:18   00:17:59
*13   00:12:29   00:17:46   00:05:17
 14   00:08:37   00:14:35   00:05:58
 15   00:24:39   00:35:38   00:10:59
 16   00:02:44   00:19:00   00:16:16
------------------------------------
Sum   02:23:07   04:18:16   01:55:09
Avg   00:08:57   00:16:09   00:07:12

* Adjusted by start time
```

## Execution time (milliseconds)
```
Day  Python
  1       6
  2       3
  3       1
  4      19
  5      23
  6    7627
  7    1990
  8       1
  9    4431
 10      13
 11      72
 12      40
 13       1
 14      11
 15    1042
 16    8075
-----------
Sum   23355
Avg    1460
```

Execution times measured on an M1 Max Mac Studio.


## How I solved it?

### Day 14, Part 2
Just printed the whole map and seconds elapsed in console and noticed that the robots bunch up on `t ≡ 2 mod 101` and
then changed the code to only show those until I saw the tree at `6668 = (2 + 66 * 101)` (your values may differ).
The solution included in the code just finds the first `t` where all of the robots are at an unique location as it
seems to always give the correct answer.

### Day 16
**Part 1:** Had dijkstra ready to go as just 9 hours earlier I had realized that I haven't seen it yet this year. Even
messaged a friend that maybe day 16 is going to finally require finding the shortest path. **Part 2:** Overthinking
killed it :'c (Although that overthinked version was a lot faster than the smaller one here)
