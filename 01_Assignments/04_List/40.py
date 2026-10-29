'''Demonstrate all common list methods'''

numbers = [30, 10, 20, 10]
print("Original:", numbers)

numbers.append(40)
print("append():", numbers)

numbers.insert(1, 15)
print("insert():", numbers)

numbers.extend([50, 60])
print("extend():", numbers)

numbers.remove(10)
print("remove():", numbers)

removed = numbers.pop()
print("pop():", numbers, "| Removed:", removed)

copied = numbers.copy()
print("copy():", copied)
print("count(10):", numbers.count(10))
print("index(20):", numbers.index(20))

numbers.sort()
print("sort():", numbers)

numbers.reverse()
print("reverse():", numbers)

numbers.clear()
print("clear():", numbers)