import sys
import time
from collections import defaultdict
from itertools import combinations, cycle

# Initialize the dataset of major presidential and vice-presidential nominees (surnames only)
elections = [
    {'year': 1789, 'candidates': ['Washington', 'Adams']},
    {'year': 1792, 'candidates': ['Washington', 'Adams']},
    {'year': 1796, 'candidates': ['Adams', 'Jefferson', 'Pinckney', 'Burr']},
    {'year': 1800, 'candidates': ['Jefferson', 'Burr', 'Adams', 'Pinckney']},
    {'year': 1804, 'candidates': ['Jefferson', 'Clinton', 'Pinckney', 'King']},
    {'year': 1808, 'candidates': ['Madison', 'Clinton', 'Pinckney', 'King']},
    {'year': 1812, 'candidates': ['Madison', 'Gerry', 'Clinton', 'Ingersoll']},
    {'year': 1816, 'candidates': ['Monroe', 'Tompkins', 'King', 'Howard']},
    {'year': 1820, 'candidates': ['Monroe', 'Tompkins']},
    {'year': 1824, 'candidates': ['Adams', 'Calhoun', 'Jackson', 'Crawford', 'Clay']},
    {'year': 1828, 'candidates': ['Jackson', 'Calhoun', 'Adams', 'Rush']},
    {'year': 1832, 'candidates': ['Jackson', 'Van Buren', 'Clay', 'Sergeant']},
    {'year': 1836, 'candidates': ['Van Buren', 'Johnson', 'Harrison', 'Granger']},
    {'year': 1840, 'candidates': ['Harrison', 'Tyler', 'Van Buren', 'Johnson']},
    {'year': 1844, 'candidates': ['Polk', 'Dallas', 'Clay', 'Frelinghuysen']},
    {'year': 1848, 'candidates': ['Taylor', 'Fillmore', 'Cass', 'Butler', 'Van Buren', 'Adams']},
    {'year': 1852, 'candidates': ['Pierce', 'King', 'Scott', 'Graham']},
    {'year': 1856, 'candidates': ['Buchanan', 'Breckinridge', 'Frémont', 'Dayton', 'Fillmore', 'Donelson']},
    {'year': 1860, 'candidates': ['Lincoln', 'Hamlin', 'Douglas', 'Johnson', 'Breckinridge', 'Lane', 'Bell', 'Everett']},
    {'year': 1864, 'candidates': ['Lincoln', 'Johnson', 'McClellan', 'Pendleton']},
    {'year': 1868, 'candidates': ['Grant', 'Colfax', 'Seymour', 'Blair']},
    {'year': 1872, 'candidates': ['Grant', 'Wilson', 'Greeley', 'Brown']},
    {'year': 1876, 'candidates': ['Hayes', 'Wheeler', 'Tilden', 'Hendricks']},
    {'year': 1880, 'candidates': ['Garfield', 'Arthur', 'Hancock', 'English']},
    {'year': 1884, 'candidates': ['Cleveland', 'Hendricks', 'Blaine', 'Logan']},
    {'year': 1888, 'candidates': ['Harrison', 'Morton', 'Cleveland', 'Thurman']},
    {'year': 1892, 'candidates': ['Cleveland', 'Stevenson', 'Harrison', 'Reid']},
    {'year': 1896, 'candidates': ['McKinley', 'Hobart', 'Bryan', 'Sewall']},
    {'year': 1900, 'candidates': ['McKinley', 'Roosevelt', 'Bryan', 'Stevenson']},
    {'year': 1904, 'candidates': ['Roosevelt', 'Fairbanks', 'Parker', 'Davis']},
    {'year': 1908, 'candidates': ['Taft', 'Sherman', 'Bryan', 'Kern']},
    {'year': 1912, 'candidates': ['Wilson', 'Marshall', 'Roosevelt', 'Johnson', 'Taft', 'Butler']},
    {'year': 1916, 'candidates': ['Wilson', 'Marshall', 'Hughes', 'Fairbanks']},
    {'year': 1920, 'candidates': ['Harding', 'Coolidge', 'Cox', 'Roosevelt']},
    {'year': 1924, 'candidates': ['Coolidge', 'Dawes', 'Davis', 'Bryan', 'La Follette', 'Wheeler']},
    {'year': 1928, 'candidates': ['Hoover', 'Curtis', 'Smith', 'Robinson']},
    {'year': 1932, 'candidates': ['Roosevelt', 'Garner', 'Hoover', 'Curtis']},
    {'year': 1936, 'candidates': ['Roosevelt', 'Garner', 'Landon', 'Knox']},
    {'year': 1940, 'candidates': ['Roosevelt', 'Wallace', 'Willkie', 'McNary']},
    {'year': 1944, 'candidates': ['Roosevelt', 'Truman', 'Dewey', 'Bricker']},
    {'year': 1948, 'candidates': ['Truman', 'Barkley', 'Dewey', 'Warren', 'Thurmond', 'Wright']},
    {'year': 1952, 'candidates': ['Eisenhower', 'Nixon', 'Stevenson', 'Sparkman']},
    {'year': 1956, 'candidates': ['Eisenhower', 'Nixon', 'Stevenson', 'Kefauver']},
    {'year': 1960, 'candidates': ['Kennedy', 'Johnson', 'Nixon', 'Lodge']},
    {'year': 1964, 'candidates': ['Johnson', 'Humphrey', 'Goldwater', 'Miller']},
    {'year': 1968, 'candidates': ['Nixon', 'Agnew', 'Humphrey', 'Muskie', 'Wallace', 'LeMay']},
    {'year': 1972, 'candidates': ['Nixon', 'Agnew', 'McGovern', 'Shriver']},
    {'year': 1976, 'candidates': ['Carter', 'Mondale', 'Ford', 'Dole']},
    {'year': 1980, 'candidates': ['Reagan', 'Bush', 'Carter', 'Mondale']},
    {'year': 1984, 'candidates': ['Reagan', 'Bush', 'Mondale', 'Ferraro']},
    {'year': 1988, 'candidates': ['Bush', 'Quayle', 'Dukakis', 'Bentsen']},
    {'year': 1992, 'candidates': ['Clinton', 'Gore', 'Bush', 'Quayle', 'Perot', 'Stockdale']},
    {'year': 1996, 'candidates': ['Clinton', 'Gore', 'Dole', 'Kemp', 'Perot', 'Choate']},
    {'year': 2000, 'candidates': ['Bush', 'Cheney', 'Gore', 'Lieberman']},
    {'year': 2004, 'candidates': ['Bush', 'Cheney', 'Kerry', 'Edwards']},
    {'year': 2008, 'candidates': ['Obama', 'Biden', 'McCain', 'Palin']},
    {'year': 2012, 'candidates': ['Obama', 'Biden', 'Romney', 'Ryan']},
    {'year': 2016, 'candidates': ['Trump', 'Pence', 'Clinton', 'Kaine']},
    {'year': 2020, 'candidates': ['Biden', 'Harris', 'Trump', 'Pence']},
    {'year': 2024, 'candidates': ['Harris', 'Walz', 'Trump', 'Vance']},
]


def spinner():
    return cycle(['|', '/', '-', '\\'])

def print_header(text):
    print("\n" + "=" * 50)
    print(f" {text} ".center(50, "="))
    print("=" * 50)

def print_subheader(text):
    print(f"\n--- {text} ---")

def print_list(items):
    for item in items:
        print(f"  • {item}")

def validate_input(args):
    if len(args) < 1 or len(args) > 2:
        print("Usage: python script.py <year> [verbose]")
        sys.exit(1)
    
    try:
        year = int(args[0])
        if year < 1789 or year > 2024:
            raise ValueError("Year must be between 1789 and 2024")
        verbose = len(args) == 2 and args[1].lower() == 'verbose'
        return year, verbose
    except ValueError as e:
        print(f"Error: Invalid input. {str(e)}")
        sys.exit(1)

def find_minimal_sets(relevant_elections, verbose):
    spin = spinner()
    start_time = time.time()

    all_candidates = set()
    for election in relevant_elections:
        all_candidates.update(election['candidates'])
    
    if verbose:
        print_subheader("All Candidates Considered")
        print_list(sorted(all_candidates))
    
    candidate_elections = defaultdict(set)
    for i, election in enumerate(relevant_elections):
        for candidate in election['candidates']:
            candidate_elections[candidate].add(i)
    
    for candidate in list(candidate_elections.keys()):
        if any(candidate_elections[candidate] < candidate_elections[other] 
               for other in candidate_elections if other != candidate):
            del candidate_elections[candidate]
            all_candidates.remove(candidate)
    
    sorted_candidates = sorted(all_candidates, key=lambda c: len(candidate_elections[c]), reverse=True)
    
    def covers_all_elections(candidate_set):
        covered = set()
        for candidate in candidate_set:
            covered.update(candidate_elections[candidate])
            if len(covered) == len(relevant_elections):
                return True
        return False
    
    greedy_solution = []
    uncovered = set(range(len(relevant_elections)))
    for candidate in sorted_candidates:
        if uncovered & candidate_elections[candidate]:
            greedy_solution.append(candidate)
            uncovered -= candidate_elections[candidate]
            if not uncovered:
                break
    
    if verbose:
        print_subheader("Greedy Solution Found")
        print_list(greedy_solution)
    
    if len(greedy_solution) <= 3:
        return greedy_solution
    
    best_solution = greedy_solution
    for i in range(1, len(greedy_solution)):
        for j, combo in enumerate(combinations(sorted_candidates, i)):
            if j % 1000 == 0:  # Update spinner every 1000 iterations
                elapsed_time = time.time() - start_time
                sys.stdout.write(f"\rSearching for optimal solution... {next(spin)} (Elapsed time: {elapsed_time:.2f}s)")
                sys.stdout.flush()
            
            if len(combo) >= len(best_solution):
                break
            if covers_all_elections(combo):
                best_solution = combo
                if verbose:
                    print(f"\nBetter Solution Found (size {len(best_solution)})")
                    print_list(best_solution)
                break
        if len(best_solution) == i:
            break
    
    print("\nSearch completed.")
    return list(best_solution)

def analyze_elections(input_year, verbose):
    if not elections:
        raise ValueError("No election data available")
    
    relevant_elections = [e for e in elections if e['year'] >= input_year]
    
    if verbose:
        print_subheader("Relevant Elections")
        for election in relevant_elections:
            print(f"  • {election['year']}: {', '.join(election['candidates'])}")
    
    if not relevant_elections:
        return []

    minimal_set = find_minimal_sets(relevant_elections, verbose)

    result = []
    for election in relevant_elections:
        for candidate in election['candidates']:
            if candidate in minimal_set and candidate not in [r[1] for r in result]:
                result.append((election['year'], candidate))
                if len(result) == len(minimal_set):
                    return result

    return result


def format_output(input_year, relevant_surnames):
    if not relevant_surnames:
        return f"No surnames from the minimal set have appeared on presidential ballots since {input_year}."
    
    surnames_list = [surname for _, surname in relevant_surnames]
    if len(surnames_list) == 1:
        return f"Since {input_year}, {surnames_list[0]} has appeared on every presidential ballot."
    elif len(surnames_list) == 2:
        return f"Since {input_year}, either {surnames_list[0]} or {surnames_list[1]} has appeared on every presidential ballot."
    else:
        formatted_names = ', '.join(surnames_list[:-1]) + f", or {surnames_list[-1]}"
        return f"Since {input_year}, at least one of these surnames has appeared on every presidential ballot (in chronological order of first appearance): {formatted_names}."

def main(args):
    input_year, verbose = validate_input(args)
    try:
        if verbose:
            print_header(f"Analyzing Presidential Elections Since {input_year}")
        
        relevant_surnames = analyze_elections(input_year, verbose)
        
        if verbose:
            print_subheader("Relevant Surnames (Year of First Appearance)")
            print_list([f"{surname} ({year})" for year, surname in relevant_surnames])
        
        result = format_output(input_year, relevant_surnames)
        
        if verbose:
            print_header("Final Result")
        print(result)
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main(sys.argv[1:])