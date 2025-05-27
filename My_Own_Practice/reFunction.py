import re

# re.search
string = 'abcdef'
if re.search(r'cd', string):
    print('yes')  # Output: yes
else:
    print('no')

# re.findall
s = 'my 2 favourite numbers are 27 and 69'
numbers = re.findall(r'[0-9]+', s)
print(numbers)  # Output: ['2', '27', '69']# Extract email
x = 'From robot@zju.edu.cn Feb 10:38:06 2025'
email = re.findall(r'^From (\S+@\S+)', x)
print(email)  # Output: ['robot@zju.edu.cn']# Extract login name
login = re.findall(r'^From (\S+)@', x)
print(login)  # Output: ['robot']# Greedy vs non-greedy matching
x = 'From: Using the :character'
greedy = re.findall(r'^F.+:', x)
print(greedy)  # Output: ['From: Using the :']
non_greedy = re.findall(r'^F.+?:', x)
print(non_greedy)  # Output: ['From:']# re.split
x = 'a b c d e'
print(re.split(r'\s+', x))  # Output: ['a', 'b', 'c', 'd', 'e']# re.sub
result = re.sub(r'abc', 'def', 'abcdef')  # Replace 'abc' with 'def'
print(result)  # Output: defdef