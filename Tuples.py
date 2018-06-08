'''*TUPLES*'''

'''Q1'''
tup1 = ("tuple", False, 3.2, 1)
print(tup1)

print(len(tup1))

'''Q2'''
tup2 = (22, 82, 69, 43, 55, 10, 32, 25, 42, 14, 46, 28, 40, 33, 11, 82, 65, 42)
largest = tup2[0]
smallest = tup2[0]
for item in tup2:
    if item > largest:
        largest = item
    elif item < smallest:
        smallest = item
print("Largest element is:", largest)
print("Smallest element is:", smallest)

'''Q3'''
tup3 = (2, 1, 12, 4, 13, 4)
product = 1
for item in tup3:
    product *= item
print("product of the tuple is:", product)
