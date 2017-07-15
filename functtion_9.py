def string_finder(my_string):
  words = my_string.split()
  new_string=''
  new_string2=''
  new_string3=''
  new_string4=''
  for s in words:
    for i in range(0,len(s)):
      if s[i]>='A' and s[i]<='Z':
        new_string +=s[i]
  print(new_string)
  for s in words:
    for i in range(0,len(s)):
      if s[i]>='a' and s[i]<='z':
        new_string2 += s[i]
  print(new_string2)
  for s in words:
    for i in range(0,len(s)):
      if s[i]>='0' and s[i]<='9':
        new_string3 += s[i]
  print(new_string3)
  for c in my_string:
    if c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789':
      new_string4 += c
  print(new_string4)
str = "Hello Test! 123 123, good."
string_finder(str)
