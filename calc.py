import random
from collections import defaultdict

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
    num_players = int(input("Enter the number of players: "))
    threshold = int(input("Enter the number frequency threshold: "))

    # Run the simulation
    probability = monte_carlo_simulation(num_simulations, num_players, threshold)

    # Display the result
    print(f"Probability of having at least {threshold} of the same number with {num_players} players is approximately {probability:.4f}")

if __name__ == "__main__":
    main()
