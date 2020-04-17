#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)


b) O(n^2)


c) O(n)

## Exercise II

I think the best way would be to create a variable called "median_index" that would be about 50% of n. It would return true or false if the egg dropped was broken at that floor. If egg is broken, then split the left half (all floors below median_index) and repeat the pattern. If the egg is not broken, split the right half and repeat the pattern until the floor is found. This would be O(log(n)) time-complexity  