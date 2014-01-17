s = 'abcdefgh'
for i in range (len(s)):
	for j in range (i,len(s)):
		print (i,j,s[i:j])