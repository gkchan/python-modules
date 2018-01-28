from collections import Counter, deque, OrderedDict

count = Counter([9, 4, 5, 6, 2, 4, 4, 5, 2])
print count
print count[4]

print count.elements()
print list(count.elements())

deque1 = deque()
print deque1

deque1.append(1)
deque1.appendleft(0)
deque1.extend([2, 3])
deque1.extendleft([-1])
deque1.rotate(2)

print deque1

ordered_dict1 = OrderedDict([(4, 5), (7, 3)])
ordered_dict1[5] = 8
print ordered_dict1




