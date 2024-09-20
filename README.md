# BallotCoverage

In 2024, someone said:
> This is the first election since 1976 without a Bush, Clinton, or Biden on the ballot.

This Python script analyzes U.S. presidential election data to find the smallest set of surnames that have appeared on every ballot since a given year.

## How It Works

The script finds the smallest group of surnames that appear in every election since the year you specify. Here's how it does this:

1. It looks at all the elections from your chosen year up to 2024.
2. It makes a list of all the different surnames that appear in these elections.
3. It uses a combination of two methods to find the smallest set of surnames:
   - First, it tries a quick "greedy" approach that often finds a good solution.
   - Then, it carefully checks if there's an even smaller set of surnames that works.
4. It stops when it's sure it has found the smallest possible group of surnames.
5. Finally, it tells you these surnames in the order they first appeared.

## Usage

```
python main.py <year> [verbose]
```

- Replace `<year>` with a year between 1789 and 2024.
- Add `verbose` as a second argument to see detailed information about the script's execution.

## Examples

1. Basic usage:
   ```
   python main.py 1980
   ```
   This will output the smallest set of surnames that have appeared on every presidential ballot since 1980.

2. Verbose output:
   ```
   python main.py 1980 verbose
   ```
   This will show detailed information about the relevant elections, candidates considered, the solution process, and the final result.

## Output

The script will output a sentence describing the smallest set of surnames. For example:

```
Since 1980, at least one of these surnames has appeared on every presidential ballot (in chronological order of first appearance): Bush, Clinton, or Trump.
```

In verbose mode, you'll see additional information about how the script found this answer.

## Requirements

- Python 3.x

No additional libraries are required; the script uses only Python's standard library.

## Notes

- The script's election data currently goes up to 2024.
- The analysis is based on surnames only and includes both presidential and vice-presidential nominees.
- The script now uses a faster method to find the answer, but it still checks to make sure it's the best possible answer.
- It can take a very long time to find the optimal solution, especially when searching back over 100 years. Press 'Enter' to return the current best solution during a long search.
