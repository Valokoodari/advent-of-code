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
 17   00:05:29    168      0   01:26:53    677      0   01:21:24    509
 18   00:06:26    303      0   00:09:48    277      0   00:03:22    -26
 19   00:02:25    139      0   00:03:50    135      0   00:01:25     -4
 20   00:19:47    615      0   00:33:44    550      0   00:13:57    -65
-----------------------------------------------------------------------
Sum   02:21:02      -      0   05:33:21      -     26   03:12:19      -
Avg   00:08:49    713      0   00:20:50    494      2   00:12:01   -219

* Excluded from the sum and average

Total points: 26
Global rank: 845
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
 17   00:05:29   01:26:53   01:21:24
 18   00:06:26   00:09:48   00:03:22
 19   00:02:25   00:03:50   00:01:25
 20   00:19:47   00:33:44   00:13:57
------------------------------------
Sum   02:57:14   06:32:31   03:35:17
Avg   00:08:52   00:19:38   00:10:46

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
 17       2
 18      17
 19     431
 20    2074
-----------
Sum   25879
Avg    1294
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

### Day 17
The first attempt was to start the brute force option but it didn't take long to realize that the answer was somewhere
in the trillions and bruting would take years even with the correct range. It took quite a while before I realized that
the solution can be searched in octal digit by digit (nice? visualization underneath).
```python
# Minimum value for A to get right length:  35_184_372_088_832
# Maximum value for A to get right lenght: 281_474_976_710_655

# [2,4]   v
# [0,1,2] |       v
# [0,4,5] |       0   v
# [0,1]   |       |   0     v
# [2,6]   |       |   5 v   |
# [5,7]   |       |   | 6 v |
# [2,7]   |       |   | | 5 |   v
# [2,7]   |       |   | | | |   2   v
ns = [7,0,2,6,4,2,0,3,5,6,5,1,4,2,7,2]
```

### Day 18
**Part 1:** Dijkstra. **Part 2:** Binary search because I didn't create the grid at first and `if (x,y) in ms` is slow.
