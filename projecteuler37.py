import sympy
def soldan_sağa(x):
    a=str(x)
    for i in range(len(a)):
        if not sympy.isprime(int(a[i::])):
            return False
    return True
def sağdan_sola(x):
    a=str(x)
    for i in range(len(a)):
        if not sympy.isprime(int(a[:i+1:])):
            return False
    return True
a=10
b=[]
while True:
    if sympy.isprime(a) and soldan_sağa(a) and sağdan_sola(a):
        b.append(a)
    a+=1
    if len(b)==11:
        break
print(sum(b))
    

