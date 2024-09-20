# BallotCoverage

In 2024, someone said:
> This is the first election since 1976 without a Bush, Clinton, or Biden on the ballot.

This Python script analyzes U.S. presidential election data to find the minimal set of surnames that have appeared on every ballot since a given year.

## How It Works

The script finds the smallest group of surnames that appear in every election since the year you specify. Here's how it does this:

1. It looks at all the elections from your chosen year up to 2024.
2. It makes a list of all the different surnames that appear in these elections.
3. Starting with just one surname, it checks if that surname appears in every election. If not, it tries combinations of two surnames, then three, and so on.
4. It stops when it finds the smallest group of surnames that appear in every election.
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
   This will output the minimal set of surnames that have appeared on every presidential ballot since 1980.

2. Verbose output:
   ```
   python main.py 1980 verbose
   ```
   This will show detailed information about the relevant elections, all candidates considered, the minimal set found, and the final result.

## Output

The script will output a sentence describing the minimal set of surnames. For example:

```
Since 1980, at least one of these surnames has appeared on every presidential ballot (in chronological order of first appearance): Bush, Clinton, or Trump.
```

In verbose mode, you'll see additional information about the script's execution process.

## Requirements

- Python 3.x

No additional libraries are required; the script uses only Python's standard library.

## Notes

- The script's election data currently goes up to 2024.
- The analysis is based on surnames only and includes both presidential and vice-presidential nominees.
- In cases where multiple minimal sets exist, the script will return one of them.