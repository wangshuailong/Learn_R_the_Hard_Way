people = 20
cats = 30
dogs = 15

if people < cats:   # Ture
    print 'Too many cats. The world is doomed !'

if people > cats: # False
    print 'Not many cats. The world is saved !'
    
if people < dogs:   # False
    print 'The world is drilled on !'

if people > dogs: #True
    print 'The world is dirty.'
    


dogs += 5 # notice how the '+=' is wrate. the same with "dogs = dogs + 5  # dogs = 20 now

if people >= dogs: # True
    print 'People are greater than or equal to dogs.'
    
if people <= dogs:  # True
    print 'People are less than or equal to dogs.'
    
if people == dogs:  # True
    print 'People are dogs.' 
