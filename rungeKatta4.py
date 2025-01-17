import math
#variables équations différentielles
x0=0
y0=3

#t voulu 
T=10

#nombre de découpage de sous ensemble (va exécuter n fois runge kutta 4 en étant plus précis)
n=100

#pas de discrétion
h=T/n

#equation 
def fonctionX(x,y):
    return x+y

def fonctionY(x,y):
    return x*2

#Résolution

def rungeKatta4IterationNormal(equationX,x,y,h,nbIteration):
    results=[(x,y)]
    for i in range(nbIteration):
        y=rungeKatta4(equationX,x,y,h)
        x+=h
        results.append((x,y))
    return results

def rungeKatta4(equation,x,y,h):
    k1=equation(x,y)
    k2=equation(x+0.5*h,y+0.5*h*k1)
    k3=equation(x+0.5*h,y+0.5*h*k2)
    k4=equation(x+h,y+h*k3)
    return y+(h/6)*(k1+2*k2+2*k3+k4)


def rungeKatta4IterationSysteme(equationX,equationY,x,y,h,TVoulu,n):
    results=[(x,y)]
    for i in range(n):
        x,y=rungeKatta4Systeme(equationX,equationY,x,y,h)
        results.append((x,y))
        print(x,y)
    return results    

def rungeKatta4Systeme(equationX,equationY,x,y,h):
    
    k1X=equationX(x,y)
    k1Y=equationY(x,y)

    k2X=equationX(x+0.5*h*k1X,y+0.5*h*k1Y)
    k2Y=equationY(x+0.5*h*k1X,y+0.5*h*k1Y)

    k3X=equationX(x+0.5*h*k2X,y+0.5*h*k2Y)
    k3Y=equationY(x+0.5*h*k2X,y+0.5*h*k2Y)

    k4X=equationX(x+h*k3X,y+h*k3Y)
    k4Y=equationY(x+h*k3X,y+h*k3Y)

    return x+(1/6)*h*(k1X+2*k2X+2*k3X+k4X), y+(1/6)*h*(k1Y+2*k2Y+2*k3Y+k4Y)
