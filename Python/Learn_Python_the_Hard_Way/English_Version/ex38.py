ten_things = 'Apples Oranges Crows Telephones Light Sugar'

print 'Wait, there\'s not ten things in the list. Let\'s fix it.'

stuff = ten_things.split (' ') # space here
more_stuff = ['Days', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

while len(stuff) <= 10:
    next_one = more_stuff.pop ()
    print 'adding: ', next_one
    stuff.append (next_one)
    print 'There\'s %d items now.' % len(stuff)
    
print 'There we go: ', stuff

print 'Let\'s do some things with stuff.'

print stuff[1] # the second item.
print stuff[-1] # 
print stuff.pop ()
print ' '.join(stuff)
print '#'.join(stuff[3:5]) 
