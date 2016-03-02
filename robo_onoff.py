import numpy as np
import pylab as py

def sigma(x): return (1.+np.exp(-x))**-1
def x_tp1(theta,w,x,c): return sigma(theta+np.dot(w,x)+c)
def cont(mu,w,delta): return mu*np.dot(w,delta)
def mu_tp1(mu,lam,delta,p): return mu+lam*(delta[0]**2+delta[1]**2)*p**-1   


t=range(0,5000)
w=np.array([[-22.0,5.9],[-6.6,0.0]])
theta=np.array([-3.4,3.8])
mu_vals=np.ones(300)*(-1)
x=[np.array([0.5,0.5])]
for step in t[1:300]:
	x.append(x_tp1(theta,w,x[-1],0.))
p_vals=[0,9,0,2,0,19,0,2,0,12,9,5,6,13,11,4]
for p in p_vals:
	mu=-1
	for step in t:
		if p==0: 
			c=np.array([0.,0.])
		else:
			if (step)%(p+1)==0:
				c=cont(mu,w,x[-1]-x[-1-p])
			else:c=np.array([0.,0.])
		x.append(x_tp1(theta,w,x[-1],c))
		if p!=0:mu=mu_tp1(mu,0.05,x[-1]-x[-1-p],p)
		mu_vals=np.append(mu_vals,mu)
x=np.array(x)
zeiten=range(0,len(p_vals)*len(t)+300)
print len(zeiten),mu_vals.shape
f=py.figure()
ax1=f.add_subplot(211)
ax2=f.add_subplot(212)
#py.title('p='+str(p))
#py.scatter(zeiten,x[:,0],label='x1')
#py.scatter(zeiten,x[:,1],label='x2')
ax1.scatter(zeiten,x[:,0]*.5+x[:,1]*.5,label='(x1+x2)/2',s=0.1)
ax1.set_ylim(0,1)
ax1.set_ylabel('$\\bar{x}$')
#py.legend()
#py.xlim(600,630)
#f=py.figure()
#py.title('p='+str(p))
ax2.scatter(zeiten,mu_vals+1.,c='r',s=0.25)
ax2.set_ylim(0,.4)
ax2.set_ylabel('$\mu +1$')
ax2.set_xlabel('t')
#py.scatter(zeiten,x[:,0],label='x1')
#	py.plot(t,x[:,1],label='x2')
#	py.plot(t,x[:,0]*.5+x[:,1]*.5,label='(x1+x2)/2')
#py.legend()
f.savefig('robo_onoff.png')
#py.xlim(0,2000)
#py.show()
