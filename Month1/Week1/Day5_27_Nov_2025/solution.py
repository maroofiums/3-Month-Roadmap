s = "hello"

print(s[::-1])

rev = ""

for ch in s:
    rev = ch + rev 
print(rev)

s = "racecar"
print(s == s[::-1]) 

s2 = "A man a plan a canal Panama"
s2 = s2.replace(" ","").lower()
print(s2 == s2[::-1])