import re
x = "1 & 2"
y = re.findall('[0-9]',x)
print(y)

x1 = "Hello : Shahin :"
y1 = re.findall('^H.+?:',x1)
print(y1)

data ="hello i:m@shahin"
z = data.find('@')
print(z)
