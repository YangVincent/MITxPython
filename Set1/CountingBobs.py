


#print "Hello WOrld"
#s = 'azcbobobegghakl'
s = 'uoobbobbqbobobdoboosf'
#print s.count('bob')
count = 0
while s.find('bob', 0, len(s)) != -1:
  if s.find('bob', 0, len(s)) != -1:
    count = count + 1
    print 'count is now ' + str(count)
    i = s.find('bob', 0, len(s))
    print 'replacing' + s[i]
#    s = s.remove(s[i])
    print 'before replace s is ' + s
    s = s[:i] + s[i+2:]
#    print 'after replace s is ' + s    
    print 'in loop i is ' + str(i)
#print 'count is ' + str(count)
print str(count)
