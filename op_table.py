import random
from collections import defaultdict
import pandas as pd
from colorama import Fore, Back, Style, init
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

# Initialize colorama
init(autoreset=True)

def monte_carlo_simulation(num_simulations, num_players, threshold):
    num_digits = num_players * 8  # Each player has 8 digits
    success_count = 0
    
    for _ in range(num_simulations):
        digits = [random.randint(0, 9) for _ in range(num_digits)]
        digit_counts = [digits.count(i) for i in range(10)]
        
        if max(digit_counts) >= threshold:
            success_count += 1
    
    return success_count / num_simulations

def parallel_simulation(num_simulations, num_players, threshold, num_workers):
    chunk_size = num_simulations // num_workers
    futures = []
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        for _ in range(num_workers):
            futures.append(executor.submit(monte_carlo_simulation, chunk_size, num_players, threshold))
        results = [future.result() for future in as_completed(futures)]
    return sum(results) / len(results)

def style_probability(probability):
    if probability >= 0.90:
        return Fore.BLACK + Back.MAGENTA + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability >= 0.60:
        return Fore.BLACK + Back.GREEN + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability >= 0.50:
        return Fore.BLACK + Back.YELLOW + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability >= 0.40:
        return Fore.BLACK + Back.CYAN + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability >= 0.10:
        return Fore.BLACK + Back.RED + f"{probability:<7.4f}" + Style.RESET_ALL
    else:
        return Fore.BLACK + f"{probability:<7.4f}" + Style.RESET_ALL

def plain_probability(probability):
    return f"{probability:<7.4f}"

def main():
    # Input parameters
    num_simulations = int(input("Enter the number of simulations: "))
    max_players = int(input("Enter the maximum number of players: "))
    max_threshold = int(input("Enter the maximum frequency threshold: "))
    
    # Determine the number of logical cores available
    logical_cores = os.cpu_count()
    print(f"Number of logical cores available: {logical_cores}")
    
    # Suggest a safe number of workers (e.g., 80% of logical cores)
    suggested_workers = max(1, int(logical_cores * 0.8))
    print(f"Suggested number of parallel workers: {suggested_workers}")
    num_workers = int(input(f"Enter the number of parallel workers (1-{logical_cores}): "))

    # Initialize the matrix
    probabilities = defaultdict(dict)

    # Calculate probabilities for each combination of players and thresholds
    for num_players in range(1, max_players + 1):
        for threshold in range(1, max_threshold + 1):
            probability = parallel_simulation(num_simulations, num_players, threshold, num_workers)
            probabilities[num_players][threshold] = probability
    
    # Convert to DataFrame for better visualization
    probabilities_df = pd.DataFrame(probabilities).T

    # Generate styled terminal output
    print("\nProbability Matrix:")
    header_row = "      " + " ".join([f"{i:<7}" for i in range(1, max_threshold + 1)])
    print(header_row)
    
    styled_matrix = []
    plain_matrix = []
    for index, row in probabilities_df.iterrows():
        styled_row = [style_probability(value) for value in row]
        plain_row = [plain_probability(value) for value in row]
        styled_str = f"{int(index):02d}  " + " ".join(styled_row)
        plain_str = f"{int(index):02d}  " + " ".join(plain_row)
        print(styled_str)
        styled_matrix.append(styled_str)
        plain_matrix.append(plain_str)

    # Save to a file with parameters
    with open("probability_matrix.txt", "a") as f:
        f.write(f"\n# Simulations: {num_simulations}, Players: {max_players}, Threshold: {max_threshold}, Workers: {num_workers}\n")
        f.write(header_row + "\n")
        for line in plain_matrix:
            f.write(line + "\n")

    print("\nProbability matrix saved to 'probability_matrix.txt'")

if __name__ == "__main__":
    main()
