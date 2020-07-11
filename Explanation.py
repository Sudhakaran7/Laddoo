We have a box of Laddoo in different weight, each Laddoo has a positive integer weight.

Each turn, we choose the two maximum weighted laddoos and smash them together.  Suppose the laddoo have weights a and b with  a<= b.  The result of this smash is:

If a == b, both laddoos are totally smashed abd distributed to children;
If x != y, the laddoo of weight a is totally destroyed, and the laddoo of weight b has new weight b-a.
At the end, there is at most 1 laddoo left.  Return the weight of this laddoo (or 0 if there are no laddoo left.)
(Anyway the laddoo will be distributed to children :P )

Find the algorithm, using the stack.

Sample input:
2 7 4 1 3 1

Sample output:
0

Explanation:
First 7,4 is taken, 7 is destroyed and 7-4 =3 is appended in stack [2,3,1,3,1]
Then 3,3 is taken, 3==3 so they both got popped so the stack is [2,1,1]
then 2,1 is taken, 2 is deleted from stack and 2-1=1 is appended in stack, stack is [1,1]
then 1,1, 1==1 so 1 is popped, so there is no laddoos, print 0

Sample input:
2 7 4 1 8 1

Sample output:
1

Explanation:
first 7,8 then 7-8=1 is appended so the stack converts to [2,4,1,1,1]
then , 2,4 2-4=2 where 2 is removed and the stack is [2,1,1,1]
then 2,1 is taken, 2 is deleted from stack and 2-1=1 is appended in stack, stack is [1,1]
then 1,1, 1==1 so 1 is popped, then the remaining laddoo weight is 1, print the output as 1

Sample input:
12 34 56 38 77

Sample output:
5

Explanation:
first 56,77 where 77-56=21 so the stack is [12,34,38,21]
then 34,38 where 38-34=4 so the stack is [12,4,21]
then 12,21 where 21-12=9 so the stack is [4,9]
then 4,9 where 9-4=5 that is the last laddoo, print 5 as answer.
