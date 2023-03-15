x1=float(input('unesite x1: '))
y1=float(input('upisite y1: '))
x2=float(input('upisite x2: '))
y2=float(input('upisite y2: '))
while x1==x2 and y1==y2:
    print('upisali ste krive koordinate')
    x1=float(input('unesite x1: '))
    y1=float(input('upisite y1: '))
    x2=float(input('upisite x2: '))
    y2=float(input('upisite y2: '))

k=(y2-y1)/(x2-x1)
l=y1-(k*x1)

print('y={}x+{}'.format(k,l))