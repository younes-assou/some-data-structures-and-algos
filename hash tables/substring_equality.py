# python3

_multiplier = 4
_prime1 = 1000000007
_prime2 = 1000000009 

def h1(s):
	H1 = [0] * (len(s)+1)
	for i in range(1,len(s)+1):
		H1[i] = (_multiplier*H1[i-1] + ord(s[i-1]))%_prime1
	return H1

def h2(s):
	H2 = [0] * (len(s)+1)
	for i in range(1,len(s)+1):
		H2[i] = (_multiplier*H2[i-1] + ord(s[i-1]))%_prime2
	return H2

class Solver:
	def __init__(self, s):
		self.s = s
		self.H1 = h1(self.s)
		self.H2 = h2(self.s)
		self.pows1 = [pow(_multiplier,i,_prime1)for i in range(len(s))]
		self.pows2 = [pow(_multiplier,i,_prime2)for i in range(len(s))]

	def ask(self, a, b, l):
		h_a = self.H1[a+l] - (self.pows1[l-1] * self.H1[a])
		h_b = self.H2[b+l] - (self.pows2[l-1] * self.H2[b])

		return (h_a%_prime1 + _prime1)%_prime1 == (h_b%_prime1 + _prime1)%_prime1 and (h_a%_prime2 + _prime2)%_prime2 == (h_b%_prime2 + _prime2)%_prime2
		

s = input()
q = int(input())
solver = Solver(s)
for i in range(q):
	a, b, l = map(int, input().split())
	print("Yes" if solver.ask(a, b, l) else "No")
