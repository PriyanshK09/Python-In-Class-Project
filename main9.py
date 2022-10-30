#Fibonacci Series
#Formula for FS : "Fn = Fn-1 + Fn-2" where Fn is Current Term

N = int(input("Number of elements in Fibonacci Series : "))
fiboSeries = [0,1]

if N>2:
	for i in range(2, N):
		nextElement = fiboSeries[i-1] + fiboSeries[i-2]
		fiboSeries.append(nextElement)

print(fiboSeries)


