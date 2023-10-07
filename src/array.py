'''
Array containts n integers
the element of array together represent a chain
and each element represent the strength of 
each link in chain. We want to divide this chain into
three smaller chains. We can break it in exactly
two non-adjacent posistions. 

We should break links P,Q 0<P<Q<N=1, Q>P+1
0, P-1, P+1,Q-1, Q+1, N-1 : Cost is A[P] + A[Q]

Consider A= [5,2,4,6,3,7]
Choose to break (1,3) => Cost 2+6
1,4: 5
2,4: 7

Write int solution<vector<int ampersand A>
Returns minimal cost of dividing chain in 3 pieces
5,2,4,6,3,7 should return 5
 '''


'''
You are given two arrays A and B consisting of N integers each.
Index K is named fair if the four sums (A[0] + ... + A[K-11), (A[K] + ... + A[N-1]), B|0] + .
.. + BIK-1|) and (BIKI + .
... + BIN-11)
are all equal. In other words, K is the index where the two arrays, A and B, can be split (into two non-empty arrays each in such a way that the sums of the resulting arrays' elements are equal.
For example, given arrays A = [0, 4, -1, 0, 3] and B = [0, -2, 5, 0,
3], index K = 3 is fair. The sums of the subarrays are all
equal: 0 + 4 + (-1) = 3; 0 + 3 = 3; 0+ (-2) + 5 = 3 and 0 + 3 = 3.
On the other hand, index K = 2 is not fair, the sums of the
subarrays are: 0 + 4 = 4; (-1) + 0 + 3 = 2; 0+(-2) = -2 and 5 + 0
† 3 = 8.
Write a function:
def solution(A, B)
which, given two arrays of integers A and B, returns the total number of fair indexes.
Examples:
1. Given A = [0, 4, -1, 0, 3] and B = [0, -2, 5, 0, 3], your function
should return 2. The fair indexes are 3 and 4. In both cases, the sums of elements of the subarrays are equal to 3.
2. Given A = [2, -2, -3, 3] and B = [0, 0, 4, -4], your function
should return 1. The only fair index is 2. Index 4 is not fair as the subarrays containing indexes from K to N - 1 would be empty.
3. Given A = 14, -1, 0, 3] and B = [-2, 6, 0, 4], your function
should return 0. There are no fair indexes.
4. Given A = [3, 2, 6] and B = [4, 1, 6], your function should
return 0.
5. Given A = [1, 4, 2, -2, 5], B = [7, -2, -2, 2, 5], your function
should return 2. The fair indexes are 2 and 4.
Write an efficient algorithm for the following assumptions:
• N is an integer within the range [2..100,000];
• each element of arrays A and B is an integer within the range
[-1,000,000,000.. 1,000,000,000].
'''