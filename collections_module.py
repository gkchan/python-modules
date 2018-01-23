from collections import Counter

count = Counter([9, 4, 5, 6, 2, 4, 4, 5, 2])
print count
print count[4]

print count.elements()
print list(count.elements())



