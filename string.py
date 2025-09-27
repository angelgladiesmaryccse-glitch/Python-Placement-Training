#anagram 

a=input().strip()
b=input().strip()
if sorted(a)==sorted(b):
    print(a,"and",b,"are Anagrams.")
else:
    print(a,"and",b,"are Not Anagrams.")

#Isogram

a=input()
s=sorted(a)
flag=0
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        flag=1
if flag==0:
    print("ISOGRAM")
else:
    print("NOT ISOGRAM")
    
# convert the digits of the string into a single number

a=input()
digits= ''.join([i for i in a if i.isdigit()])
if digits:
    number=int(digits)
else:
    number= 0
print (number)
