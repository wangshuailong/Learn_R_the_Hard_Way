from sys import argv

script, txtfile = argv

def read_file(f):
    print f.read()
    
# def write_file(f, line_num):
#   print f.write(line_num)

def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print line_count, f.readline()

print 'First, let\'s look at what is inside this file.'

context_of_file = open(txtfile, 'r+')

print 'I am going to erase %r.' % txtfile

context_of_file.truncate()

print 'Now I\'m going to write somethings on the clean file %r.' % txtfile

line1 = raw_input('>line 1:')
line2 = raw_input('>line 2:')
line3 = raw_input('>line 3:')

context_of_file.write(line1)
context_of_file.write(line2)
context_of_file.write(line2)

context_of_file2 = open(context_of_file)

read_file(context_of_file2)

rewind(context_of_file2)

print 'Let\'s look at each line of this file.'

current_line = 1
print_a_line(current_line, context_of_file2)
current_line = 1 + 1
print_a_line(current_line, context_of_file2)
current_line = 1 + 1
print_a_line(current_line, context_of_file2)
