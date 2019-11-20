# https://leetcode.com/problems/count-binary-substrings/

ts1 = "00110011" # expected output == 6
ts2 = "10101" # expected output == 4

def countBinarySubStrings(s: str):
	i = 1
	
	# Counters are calculated as we find "boundaries", meaning a new '1' or '0'
	previousCounter = 0 
	currentCounter = 1
	answer = 0 
	while i < len(s):
		if s[i - 1] != s[i]:
			answer += min(previousCounter, currentCounter)
			previousCounter = currentCounter
			currentCounter = 1
		else:
			currentCounter+=1
		i+=1
	answer += min(previousCounter, currentCounter)
	return answer

print(countBinarySubStrings(ts1))
print(countBinarySubStrings(ts2))