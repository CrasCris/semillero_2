a = 1
c = 0
b = 1
for i in range(1000):
	for j in range(10000):
		c = c- a - b
		a = a + 1500
		b = a - 1
print(c)
