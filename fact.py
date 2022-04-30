"""Faktorial hisoblaymiz"""
def factorial(x):
	fact = 1
	for i in range(1, x+1):
		fact*=i
	return fact

"""Kombinatorika hisoblaymiz"""
def compinatorica(n, k):
	res = factorial(n)/(factorial(k)*factorial(n-k))
	return int(res)


# Natija
n = int(input("n = "))
k = int(input("k = "))

natija = compinatorica(n, k)

result = f"""
   {k}	 {n}!
# C == ------------={natija}
   {n}    {k}!({n}-{k})!
   """
print(result)