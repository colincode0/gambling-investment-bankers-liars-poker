## This repository includes a Liar's Poker Monte Carlo simulator and the rules for a modified version of the game Liar's Poker.
![aaaa](https://github.com/colindharrington/gambling-investment-bankers-liars-poker/assets/42985430/8f22795d-cf44-48a9-b48e-37443675fb80)

**Vertical axis** = x number of players  
**Horizontal axis** = probability of x of the same number amongst all bills

Python file allows user to specify:
- Number of simulations
- Number of players
- Number frequency threshold
- Number of CPU cores used to simulate

Output in the terminal will be colored based on probability, and simulations will be saved to `probability_matrix.txt`.

--------------------------------------------

# Rules of Gambling Investment Bankers Liars Poker

*It is assumed the players understand the regular rules of liar's poker. The following rules define the changes to the normal rules.*

1. **Challenge Mechanism:**
   - Anyone can challenge at any time.
   - Any player that challenges a bet is only betting against the bettor. If the bet is correct, the challenger pays the bettor one dollar, and if the bet is incorrect, the bettor pays the challenger one dollar.

2. **Betting:**
   - Any bet can be made at any time.
   - Bets on the letters around the serial number wager double the regular bet for both the bettor and the challenger.
   - Letter bets are higher than bets of the number zero, but a player can never bet fewer letters than the current number bet.

3. **Default Mechanism:**
   - If a player cannot repay a loan, they default. In default, the borrower must pay as much as they can. After this payment, their remaining debt is wiped clean unless the terms of the bet specify otherwise.

--------------------------------------------

## Examples

### Example 1: Game of 5 Players
- **Player 1**: three threes
- **Player 2**: five fours
- **Player 3**: six threes
- **Player 4**: seven threes
- **Player 2**: challenge

If there are fewer than seven 3's amongst all bills, Player 4 pays Player 2 one dollar.  
If there are seven or more 3's, Player 2 pays Player 4 one dollar.

### Example 2: Game of 3 Players
- **Player 1**: two eights
- **Player 2**: two L's (double bet)
- **Player 3**: three twos
- **Player 1**: three nines
- **Player 2**: three L's (double bet)
- **Player 3**: challenge

If there are fewer than three L's amongst all bills, Player 2 pays Player 3 two dollars.  
If there are three or more L's, Player 3 pays Player 2 two dollars.

--------------------------------------------

## Gambling Investment Banker Strategies
- If a player runs out of money, another player can loan them money to get back in the game:
  - *"I'll give you a dollar now, and if you still have money in three turns, you will give me two dollars."*
- A player can make side bets on another player:
  - *"I will bet anyone one dollar that Player 3 doesn't win this next hand."*
- A player must pay another player when they lose, unless the two players can agree on terms
  - *"I will owe you one dollar, and keep this dollar I would have given up as I lost the bet. If I still have money in three turns, I will give you two dollars"*
- A player might negociate out of a default to stay in the game for longer
  - *"I can't pay the full three dollars right now, and will default. How about I give you one dollar now and two dollars in two turns?"*
- A player can pool resources with another player to challenge a high bet:
  - *"Let's pool our money to challenge Player 3's bet. If we win, we split the winnings. If we lose, we both contribute to the payment."*
- A player can offer a debt as collateral to secure a loan:
  - *"I'll give you my debt from Player 2 as collateral for the one-dollar loan. You can collect from them if I don't repay you in three turns."*
- A player can sell their position/turn as part of negotiations:
  - *(The next turn still goes to the person left of the player who sold the turn position)*
  - *"I'll give my turn to any other player for the cost of one dollar."*
