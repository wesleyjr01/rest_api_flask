def double(x):
    return x * 2


# solution wihtout lambda
sequence = [1, 3, 5, 9]
doubled = [double(x) for x in sequence]
print(doubled)

# solution with lambda
Doubled = list(map(lambda x: x * 2, sequence))
print(Doubled)
