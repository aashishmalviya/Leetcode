Till mountain rising height, we increase peak by 1 and add that peak to required candies,
while climbing if we reach the end, return the total candies.
​
when mountain lowering height, we increase valley by 1 and add that valley to required candies.
​
since we can go into depth(valley) or height(peaks) multiple times on a series of mountains, **its important to note that after every switch cycle (peak then valley (if any exist from either of them)) we will always consider the one that is maximum, in order to satisfy the condition that the highest/deepest point will ensure its getting more candies than its neighbours.**
​
Since we've already considered the max whether depth or height, we need to subtract the other one which is minimum, because while calculating the total candies for every cycle, we added peaks and valleys also.
​
But only one should be there in the total candies answer.