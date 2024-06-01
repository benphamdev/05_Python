import math

def power(x, y, p) :
	res = 1	 
	x = x % p 
	if (x == 0) :
		return 0
	while (y > 0) :
		if ((y & 1) == 1) :
			res = (res * x) % p
		y = y >> 1	 
		x = (x * x) % p		
	return res
	
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    gcd_val, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_val, x, y

def mod_inverse(A, M):
    gcd_val, x, y = gcd_extended(A, M)
    if gcd_val != 1:
        print("Inverse doesn't exist")
    else:
        res = (x % M + M) % M
        print("Modular multiplicative inverse is", res)

if __name__ == "__main__" :
    p, alpha, a = map(int, input().split())
    public_key = power(alpha, a, p)
    print("Public key is ", public_key)
    k = 23
    x = 34

    y1 = power(alpha, k, p)
    print("y1 is ", y1)
    y2 = (x * power(public_key, k, p)) % p
    print("y2 is ", y2)

    e = p - 1 - a
    b  = power(y1, e, p)
    print("b is ", b)

    x = (y2 * b) % p
    # x = power(y2 * b, 1, p)
    print("x is ", x)