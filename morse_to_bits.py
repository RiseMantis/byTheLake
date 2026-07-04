text = input()
output = ""

for i in text:
  if i == '.':
    output+='0'
  elif i =='-':
    output+='1'
  else:
    output+=i
    
print(output)
