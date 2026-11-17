# Traditional Method (Baseline)

## Idea

Just think of a number from 1 to n. No algorithm, no tricks.

This is the baseline. Every other method gets compared against it.

## Steps

1. Pick the range (here: 1 to 9).
2. Think of a number in that range and type the first one that comes to mind into a file.
3. Repeat until I have N numbers.

## Source and mapping

- **Source:** my own intuition
- **Mapping:** none

## How the data was collected

Two runs, each N = 100 numbers, range 1 to 9.

- **Run 1** (`data/traditional.txt`): about 6:30 pm. I had just been told that people tend to favor 3 and 7 and rarely repeat, which may have influenced me.
- **Run 2** (`data/traditional2.txt`): about 10:30 pm, tired after coding. I deliberately tried not to type too many 3s and 7s, and tried not to repeat much.
- **Both runs:** I was in front of my laptop typing the numbers as I went, so I could see the number keys. That may have acted as a visual cue, so these runs are not purely mental.

## Results

| Test | Run 1 | Run 2 | Combined (N = 200) | Aim |
|------|-------|-------|--------------------|-----|
| Chi-square | 4.22 | 4.76 | 3.31 | about 8 (df = 8) |
| P-value | 0.84 | 0.78 | 0.91 | above 0.05 |
| Repeat rate | 0.07 | 0.04 | 0.06 | about 0.11 |
| Entropy (bits) | 3.14 | 3.13 | 3.16 | about 3.11 to 3.17 |

Charts: `visualizations/traditional.png`, `visualizations/traditional2.png`, `visualizations/traditional-1-and-2.png`

## What the results show

- **How often each number appeared looks fine.** All p-values are well above 0.05, so there's no evidence of bias toward particular numbers. Entropy is in the expected range every time. No number stood out in both runs.
- **Repeats are where my bias showed up.** All three repeat rates are below the expected 0.11. In run 1 I made about 7 repeats out of 99 pairs, where about 11 is expected (a normal range is roughly 5 to 17). In run 2 it was about 4, just below that range, which fits with me deliberately avoiding repeats. Combined, it was about 11 repeats out of 199 pairs, where about 22 is expected (normal range roughly 13 to 31).
- **The combined chi-square (3.31) is lower than the typical value of about 8.** That means the counts are a bit flatter than pure chance usually produces. It's not conclusive, but it fits with me trying to balance my numbers, especially in run 2.

## Limitations

- One person, two runs.
- Run 1 was influenced by what I had just heard, and run 2 was deliberate and done while tired, so the runs weren't under the same conditions.
- I could see the keyboard's number keys while typing.
- N = 100 is small, so a mild bias in how often numbers appear could be hidden.
- The combined file joins two runs, which counts one extra pair at the boundary.

## Takeaway

When I just thought of a number, my picks were spread out evenly, but I repeated less than chance would. Frequency looks fine, and order is where human bias appeared. This sets the bar that other methods need to beat, especially on repeat rate.

## Next time

- Record numbers without looking at the keys (for example, say them aloud or write them down) so the baseline is purely mental.
- Do the runs at the same time of day and without having just read about human randomness.
- Have another person use this method, and record the results