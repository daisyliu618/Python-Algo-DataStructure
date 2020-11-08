"""

Deque in Python

from collections import deque



Deques have O(1) speed for appendleft() and popleft()
while lists have O(n) performance for insert(0, value) and pop(0).


append() :- This function is used to insert the value in its argument to the right end of deque.

appendleft() :- This function is used to insert the value in its argument to the left end of deque.

pop() :- This function is used to delete an argument from the right end of deque.

popleft() :- This function is used to delete an argument from the left end of deque.





index(ele, beg, end) :- This function returns the first index of the value mentioned in arguments, starting searching from beg till end index.

insert(i, a) :- This function inserts the value mentioned in arguments(a) at index(i) specified in arguments.

remove() :- This function removes the first occurrence of value mentioned in arguments.


count() :- This function counts the number of occurrences of value mentioned in arguments.

extend(iterable) :- This function is used to add multiple values at the right end of deque. The argument passed is an iterable.

extendleft(iterable) :- This function is used to add multiple values at the left end of deque. The argument passed is an iterable. Order is reversed as a result of left appends.

reverse() :- This function is used to reverse order of deque elements.

rotate() :- This function rotates the deque by the number specified in arguments. If the number specified is negative, rotation occurs to left. Else rotation is to right.



https://www.geeksforgeeks.org/deque-in-python/
https://www.youtube.com/watch?v=m3JgSV1Obn8
https://www.techwithtim.net/tutorials/python-programming/intermediate-python-tutorials/collections-dequedeck/



"""