import random
from collections import defaultdict
import pandas as pd

def monte_carlo_simulation(num_simulations, num_players, threshold):
    num_digits = num_players * 8  # Each player has 8 digits
    success_count = 0
    
    for _ in range(num_simulations):
        digits = [random.randint(0, 9) for _ in range(num_digits)]
        digit_counts = [digits.count(i) for i in range(10)]
        
        if max(digit_counts) >= threshold:
            success_count += 1
    
    return success_count / num_simulations

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

    # Display the result as a table
    print("\nProbability Matrix:")
    print(probabilities_df)

    # Optionally, save to a file
    probabilities_df.to_csv("probability_matrix.csv", index=True)
    print("\nProbability matrix saved to 'probability_matrix.csv'")

if __name__ == "__main__":
    main()
