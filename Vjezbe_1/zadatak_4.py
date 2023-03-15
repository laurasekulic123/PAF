def funkcija(x1,y1,x2,y2):

    k=(y2-y1)/(x2-x1)
    if (x2-x1)!=0:
        l=y1-(k*x1)
        print('y={}x+{}'.format(k,l))

funkcija(2,4,6,8)
