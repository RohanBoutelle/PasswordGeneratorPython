u='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
l='abcdefghijklmnopqrstuvwxyz'
d='1234567890'
s='!@#$%^&*()?|\/'

st=input('Select Password Type: Strong/Medium/Weak')

if st=='Strong' or st=='strong':
    x=2;y=3;z=3;w=3;
elif st=='Medium' or st=='medium':
    x=2;y=2;z=2;w=2;
elif st=='Weak' or st=='weak':
    x=2;y=2;z=2;w=0;
else:
    print('Wrong Choice!!!!')
    exit()

import random
m=random.choices(u,k=x)
nu=random.choices(l,k=y)
o=random.choices(d,k=z)
p=random.choices(s,k=w)

dd=[m,nu,o,p]
random.shuffle(dd)
pa=sum(dd,[])
str(pa)
f=''
f=f.join(pa)

print(pa)
