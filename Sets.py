'''SETS/'''
set1 = set()
set1size = int(input("Enter the size of first set: "))
for i in range(0 , set1size):
    set1Item = int(input())
    set1.add(set1Item)
set2 = set()
set2size = int(input("Enter the size of second set: "))
for i in range(0 , set2size):
    set2Item = int(input())
    set2.add(set2Item)
print(set1)
print(set2)

'''1'''
diffset = set1 - set2
print(diffset)
diffset = set2 - set1
print(diffset)

'''2'''
issubset = set1 <= set2
if issubset == True:
    print("First set is subset of Second set")
else:
    print("First set is not a subset of Second set")
issubset = set2 <= set1
if issubset == True:
    print("Second set is subset of First set")
else:
    print("Second set is not a subset of First set")
issuperset = set2 >= set1
if issuperset == True:
    print("Second set is superset of First set")
else:
    print("Second set is not a superset of First set")
issuperset = set1 >= set2
if issuperset == True:
    print("First set is superset of Second set")
else:
    print("First set is not a superset of Second set")

'''3'''
intersection = set1 & set2
print("The intersection of both sets:" , intersection)