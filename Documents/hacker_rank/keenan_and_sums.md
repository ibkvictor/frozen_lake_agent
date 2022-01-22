
[Kenan and sons problem](https://www.hackerrank.com/contests/basics-of-problem-solving/challenges/keenan-and-sums/problem)

Note: There are no partial points for this challenge.

Keenan Zialcita is playing a game on his computer. He just cleared a stage, and got  points.

He also gets a bunch of bonuses and penalties, particularly there are  bonuses or penalties, which give a net score addition of . Bonuses are denoted by a positive integer , while penalties are determined by a non-positive integer .

His final score is calculated, by the sum of the bonuses and penalties. Note that the score can never go below  during the calculation.

If the bonuses and penalties can be calculated in any order, what's the maximum score he can get?

Origin:
ProgVar 2014 Session 3 Level 3

Input Format

The first line contains two integers,  and  .

The second line contains  lines, each with a single integer , which represent the bonuses. 

Output Format

Output a single integer, the maximum number of points Keenan can get after all the calculations.

Sample Input

100 5
-105
300
500
-100
200
Sample Output

1000
Explanation

We start with  points.

We can apply the  penalty, then we now have  points.

We can then apply the  penalty, then we have  points. Of course, we can't have less than  points, so now we have  points again.

Then, we can apply  points, for a current total of  points.

Then , we can apply the  points, for a current total of  points.

Then, we apply the  points, for a total of  points. This is optimal.
