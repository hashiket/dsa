#Find the first non-repeating character from a stream of characters
from collections import deque 
class Solution:
	def FirstNonRepeating(self, A):
		# Code here
		que = deque()
		
		freq = dict()
		
		ans = ''
		
		for char in A:
		    if char in freq:
		        freq[char] += 1
		    else:
		        freq[char] = 1
		    
		    if freq[char] == 1:
		        que.append(char)
	        
	        while que and freq[que[0]] > 1:
	            que.popleft()
	        
	        if not que:
	            ans += '#'
	        else:
	            ans += que[0]
        return ans