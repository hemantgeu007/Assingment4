'''DICTIONARIES'''

'''1'''
stud_data={}

for i in range(0,3):
    Name = input("Enter the student name :").split()
    Marks = input("Enter the Marks :".format(Name)).split()
    Nam_key =  Name[0]
    Marks_value = Marks[0]
    stud_data[Nam_key] = {Marks_value}
print(stud_data)

'''2'''
for key in sorted(stud_data):
    print("%s: %s" % (key, stud_data[key]))

'''3'''
word='MISSISSIPPI'
res = dict((letter,word.count(letter)) for letter in set(word))
print(res)
