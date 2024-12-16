#variables équations différentielles
x0=1
y0=3
T=0.5
n=3
h=T/n

#equation 
def fonctionX(x,y):
    print(x+y)
    return x+y

def fonctionY(x,y):
    return y+x

#Résolution

def rungeKatta4Iteration(equationX,equationY,x,y,h,nbIteration):
    results=[(x,y)]
    for i in range(nbIteration):
        x=rungeKatta4(equationX,results[i][0],results[i][1],h)
        y=rungeKatta4(equationY,results[i][1],results[i][0],h)
        results.append((x,y))
    return results    

def rungeKatta4(equation,x,y,h):
    k1=h*equation(x,y)
    k2=h*equation(x+(h/2),y+(h/2)*k1)
    k3=h*equation(x+(h/2),y+(h/2)*k2)
    k4=h*equation(x+h,y+h*k3)
    return x+(h/6)*(k1+2*k2+2*k3+k4)
        
print(rungeKatta4Iteration(fonctionX,fonctionY,x0,y0,h,4))
