counter = 2
biggest = 2
length = len(s) - 1
longestString = s[0]
currentString = s[0]
for i in range(length):
  if s[i] <= s[i+1]:
    counter = counter + 1
    currentString = currentString+ s[i+1]
    if counter > biggest:
      biggest = counter
      longestString = currentString
  else:
    counter = 2
    currentString = s[i+1]
print('counter is ' + str(counter))
print(longestString)
