# AI Log

A running record of how I used AI (Claude, by Anthropic) on this project:
what I asked, what it contributed, what I kept or rejected, and what I verified myself.

## Entry 1: Project scoping (2026-11-08)

**My contribution**
- Came up with the project idea: finding a way to generate a random number using only my mind.
- Redirected the project when the first framing (studying human randomness in general) didn't match what I wanted to explore.

**What Claude contributed**
- Background on related work: research on how poorly humans generate random sequences, entropy sources and extractors in cryptography, and von Neumann's methods.
- Drafted the initial repo structure.

**What I decided**
- Using a plain README for now and staying flexible instead of following a fixed roadmap.

## Entry 2: Baseline, and analysis code (2026-11-16)
 
**My contribution**
- Collected the baseline ("traditional" method: just think of a number) in two runs of 100, range 1 to 9.
- Wrote my own analysis and visualizer scripts (chi-square, repeat rate, entropy, histogram) and my scripts use a structure Claude suggested (a shared reader, paths built from the script’s location), but I wrote and adapted the code myself.
- When Claude rewrote my code, I said I wanted to write it myself and learn. Since then I've asked Claude to review and point out bugs instead.
- Spotted confounds in my own data and documented them: I could see the keyboard's number keys, run 1 was influenced by what Claude had just told me, and run 2 was done tired with deliberate avoidance of 3s, 7s and repeats.
- Decided to report both runs and the combined data instead of choosing one.
- Wrote down the data format and project structure.

**What Claude contributed**
- Explained what each statistic measures and its formula, and corrected my targets: I thought chi-square should be 0 and the p-value 1.0, but a truly random source gives chi-square near its degrees of freedom and a p-value that could be anywhere above about 0.05.
- Reviewed my code and found bugs: the repeat-rate loop wrapped around and compared the first and last draws, the entropy aim was missing a factor of ln 2, string comparison was being used to find the maximum, the count of values wasn't checked against the header, and the chart was saving to the wrong folder.
- Wrote analyze.py (an unrequested rewrite of my script), and later reader.py, analysis.py, and visualizer.py when I asked. I used the suggested structure (a shared reader, paths built from the script’s location) but adapted the code myself so I can explain it.
- Drafted `methods/traditional.md` from my results and notes.

**What I verified myself**
- My scripts' output (chi-square 4.22 and 4.76) matched Claude's hand calculations from the charts.
- A small test file suggested by Claude, with the expected answer worked out by hand, matched my script’s output
 