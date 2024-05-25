import random
from collections import defaultdict
import pandas as pd
from colorama import Fore, Back, Style, init

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

def style_probability(probability):
    if probability > 0.75:
        return Fore.BLACK + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability > 0.50:
        return Fore.BLACK + Back.GREEN + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability == 0.50:
        return Fore.BLACK + Back.YELLOW + f"{probability:<7.4f}" + Style.RESET_ALL
    elif probability < 0.25:
        return Fore.BLACK + f"{probability:<7.4f}" + Style.RESET_ALL
    else:
        return Fore.BLACK + Back.RED + f"{probability:<7.4f}" + Style.RESET_ALL

def main():
    # Input parameters
    num_simulations = int(input("Enter the number of simulations: "))
    max_players = int(input("Enter the maximum number of players: "))
    max_threshold = int(input("Enter the maximum frequency threshold: "))
    
    # Initialize the matrix
    probabilities = defaultdict(dict)

    # Calculate probabilities for each combination of players and thresholds
    for num_players in range(1, max_players + 1):
        for threshold in range(1, max_threshold + 1):
            probability = monte_carlo_simulation(num_simulations, num_players, threshold)
            probabilities[num_players][threshold] = probability
    
    # Convert to DataFrame for better visualization
    probabilities_df = pd.DataFrame(probabilities).T

    # Display the result as a styled table
    print("\nProbability Matrix:")
    
    # Print the header row with accurate spacing
    header_row = "      " + " ".join([f"{i:<7}" for i in range(1, max_threshold + 1)])
    print(header_row)
    
    for index, row in probabilities_df.iterrows():
        styled_row = [style_probability(value) for value in row]
        print(f"{int(index):02d}  ", " ".join(styled_row))

    # Optionally, save to a file
    probabilities_df.to_csv("probability_matrix.csv", index=True)
    print("\nProbability matrix saved to 'probability_matrix.csv'")

if __name__ == "__main__":
    main()
