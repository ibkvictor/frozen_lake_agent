[Buying Hearthstone Decks problem](https://www.hackerrank.com/contests/basics-of-problem-solving/challenges/buying-hearthstone-decks)

Mr. Manchester Sy wants to buy some cards in Hearthstone, but you know, Xavier's salary isn't so high, so he only has  pesos.

Unfortunately, in Hearthstone, cards can only be bought in sets, each set costs the number of cards it has. So, there are  sets, with  cards in each set.

Of course, sets can be bought multiple times.

Find out the maximum amount of cards that Mr. Sy can get, if he doesn't go beyond  pesos.

Input Format

The first line contains two integers,  and , , the amount of pesos that Mr. Sy has, and the number of sets he can buy from.

Then, follows  integers,  , the number of cards in each set.

Output Format

Output a single integer, the maximum number of cards that Mr. Sy can buy, that he can stil afford.

Note: There are no partial points for this challenge.

Sample Input

20 3
7 8 9
Sample Output

18
Explanation

For the example, Mr. Manchester Sy has exactly  pesos, and there are  card packs to choose from, with costs .

There are some ways we can choose them, particularly:

Buy just the set . The total is .
Buy just the set . The total is .
Buy just the set . The total is .
Buy the sets . The total is .
Buy the sets . The total is .
Buy the sets . The total is .
Buy the sets . The total is .
Buy the sets . The total is .
Buy the sets . The total is .
It's easy to see that the maximum cost that doesn't go over his money is .

We can't choose, for example, , since he can't afford cost of  pesos.
