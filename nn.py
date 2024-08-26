Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
... p=3
... q=7
... n=p*q
... e=2
... phi=(p-1)*(q-1)
... while(e<phi):
... if(math.gcd(e,phi)==1):
... break
... else:
... e=e+1
... msg=12.0
... print("message sent:",msg)
... c=pow(msg,e)
... c=math.fmod(c,n)
... print("encrypted data",c)
... m=pow(c,d)
... m=math.fmod(m,n)
