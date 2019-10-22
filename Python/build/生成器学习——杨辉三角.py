def triangle():
     l=[1]
     while True:
             yield l
             l.append(0)
             l= [l[i-1]+l[i] for i in range(len(l))]

x = triangle()
for i in range(10):
    print(next(x))
