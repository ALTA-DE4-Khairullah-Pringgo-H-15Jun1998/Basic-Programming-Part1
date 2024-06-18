N = 1000221;
fourDiv = [False] * (N + 1);

def fourDistinctFactors():
	
	primeAll = [True] * (N + 1);
	p = 2;

	while (p * p <= N): 

		if (primeAll[p] == True):

			i = p * 2;
			while (i <= N):
				primeAll[i] = False;
				i += p;
		p += 1;

	prime = [];

	for p in range(2, N + 1):
		if (primeAll[p]):
			prime.append(p);

	for i in range(len(prime)): 
		p = prime[i];
		if (1 * p * p * p <= N):
			fourDiv[p * p * p] = True;
		for j in range(i + 1, len(prime)):
			q = prime[j];
			if (1 * p * q > N):
				break;
			fourDiv[p * q] = True;

fourDistinctFactors();

num = int(input("Masukkan angka bilangan keren ="))
for x in range (2,num):
    if num % x ==0:
        break
if x+1 == num:
    print ("Ya")
elif (fourDiv[num]):
	print("Ya");
else:
	print("Tidak");

