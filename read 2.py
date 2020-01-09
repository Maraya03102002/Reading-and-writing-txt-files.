#Reading from text file using Python

print "Opening and closing the file."
text_file=open (Read_it.txt", "r")
text_file.close()

print "\nReading Character from the file."
text_file=open("read_it.txt", "r")
    print text_file.read(1)
    print text_file.read(2)
text_file.close()

print "\nReading the entire file at once."
text_file=open("read_it.txt", "r")
    print text_file.read(3)
    print text_file.read(4)
text_file.close()

print "\nReading Character from the file."
text_file=open("read_it.txt", "r")
    print text_file.read(5)
    print text_file.read(6)
text_file.close()

print "\nReading one line at a time."
text_file=open("read_it.txt", "r")
    print text_file.read(7)
    print text_file.read(8)
text_file.close()


text_file=open("read_it.txt", "r")
all_lines= text_file.readlines()
print lines
print len(lines) for line in lines:
print line
text_file.close()
