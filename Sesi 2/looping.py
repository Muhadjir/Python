#while
n = 5
while n > 0:
    n -= 1
    print(n)

#2
i = 1
while i < 6:
  print(i)
  i += 1

#while with break
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break # Break Statement
    print(n)
print('Loop ended.')

#while continue
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('Loop ended.')

#while else
n = 5
while n > 0:
    n -= 1
    print(n)
else:
    print('Loop done.')

#while break else
n = 5
while n > 0:
    n -= 1
    print(n)
    if n == 2:
        break
else:
    print('Loop done.')

#nested while
a = ['foo', 'bar']

while len(a):
    print(a.pop(0))
    
    b = ['baz', 'qux']
    
    while len(b):
        print('>', b.pop(0))

# for
a = ['foo', 'bar', 'baz']
for i in a:
    print(i)

# for dict call key
d = {'foo': 1, 'bar': 2, 'baz': 3}
for k in d:
    print(k)

# for call value
for k in d:
    print(d[k])

#2
for k in d.values():
    print(k)

#for call key and value dict
for k, v in d.items(): 
    print(k, ":", v) 

#for and break
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        break
    print(i)

#for continue
for i in ['foo', 'bar', 'baz', 'qux']:
    if 'b' in i:
        continue
    print(i)

# for else
for i in ['foo', 'bar', 'baz', 'qux']:
    print(i)
else:
    print('Done.')  # Will execute

#for break else
for i in ['foo', 'bar', 'baz', 'qux']:
  if i == 'bar':
    break
  print(i)
else:
  print('Done.') 

