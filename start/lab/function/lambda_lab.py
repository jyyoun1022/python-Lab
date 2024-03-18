def hap(x, y):
    return x + y


result = hap(10, 20)
print(result)

result2 = (lambda x, y: x + y)(10, 20)
print(result2)