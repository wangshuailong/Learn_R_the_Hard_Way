def apple_and_banana(apple, banana):
    print 'I have %r apples.' % apple
    print 'I have %r bananas.' % banana
    print 'You have %r apples and %r bananas.\n' %(apple, banana)
    
print 'So, how many do we have? \n'
apple_and_banana(20, 10)

print 'We can also count them this way.\n'
myapple = 20
yourbanana = 10
apple_and_banana(myapple, yourbanana)

print 'We can also use math.\n'
apple_and_banana(10+10, 20-10)
