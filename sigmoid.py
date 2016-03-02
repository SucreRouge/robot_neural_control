import numpy as np
import pylab as py

def sig(x):return (1+np.exp(-x))**-1

x=np.linspace(-25,25,200)

py.plot(x,sig(x))
py.xlabel('x')
py.ylabel('$\sigma$(x)')
py.savefig('sigmoid.png')
