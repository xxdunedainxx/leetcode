# REMEMBER:: this logic pretty much removes from front slowly. 

ts1="abcabcdbb"
ts2="bbbbb"
ts3="pwppwkew"

def getLongestSubStringNoRptChars(s: str)->int:
	i:int = 0 
	j:int = 0
	longestSubStr = 0
	indexTracker : dict = {

	}

	while j < len(s):

		# duplicate character detection
		if s[j] in indexTracker:
			print(f"Duplicate found @ s[j]=={s[j]}")
			print(f"indextracker=={indexTracker}")
			# remember this is setting i to the last siting of the character. So it will remove from the front of the array 
			i = max(indexTracker[s[j]],i)
			print(f"i=={i}, j=={j}")
		else:
			print(f"unique stuff found, i--{i} && j--{j}, char {s[j]}")

		longestSubStr=max(longestSubStr, j - i + 1)
		indexTracker[s[j]] = j + 1
		j+=1
	return longestSubStr

print(getLongestSubStringNoRptChars(ts1))
print(getLongestSubStringNoRptChars(ts2))
print(getLongestSubStringNoRptChars(ts3))