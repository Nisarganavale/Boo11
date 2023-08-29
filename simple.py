def f(x,y):
    return x+y
def rk4(x0,y0,xn,n):
    h=(xn-x0)/n
    print('...solution...')
    print('x0\t y0\t yn')
    for i in range(n):
        k1=h*(f(0,y0))
        k2=h*f((x0+h/2),(y0+k1/2))
        k3=h*(f((x0+h/2),(y0+k2/2)))
        k4=h*f((x0+h),(y0+k3))
        k=(k1+2*k2+2*k3+k4)/6
        yn=y0+k
        print('%0.4f\t %0.4f\t %0.4f'%(x0,y0,yn))
        y0=yn
        x0=x0+h
    print('\n at x=%0.4f,y=%0.4f'%(xn,yn))
print('enter initial conditions:')
x0=float(input('x0='))
y0=float(input('y0='))
print('enter calculation point:')
xn=float(input('xn='))
step=int(input('number of steps='))
rk4(x0,y0,xn,step)