name = "Amal M P"
print(name[2])
# here name is a string we can not modify the chars inside the string by swapping.
# for that  we have to discuss  the concept of list.

# crating list
lis = ['chemistry ', 'physics', 'mathematics']
print(lis)

lis[2] = 'hindi'
print(lis)
# list is mutable and string is immutable

lis=lis+['social science','information technology',15]

print(lis)

lis.append('amal')
print(lis)
# using append fn we can add values in list
lis.append(input('enter a list value'))
print(lis)