# Stabilizing orbit 8

import numpy as np
import pylab as py

def sigma(x): return (1.+np.exp(-x))**-1
def x_tp1(theta,w,x,c): return sigma(theta+np.dot(w,x)+c)
def cont(mu,w,delta): return mu*np.dot(w,delta)
def mu_tp1(mu,lam,delta,p): return mu+lam*(delta[0]**2+delta[1]**2)*p**-1


t=range(0,700)
w=np.array([[-22.0,5.9],[-6.6,0.0]])
theta=np.array([-3.4,3.8])
f=py.figure(figsize=(12,8))
i=1
for p in [0,1,4,5,7,9]:
	mu=-1
	x=[np.array([0.,1.])]
	for step in t[1:300]:
		x.append(x_tp1(theta,w,x[-1],0.))
	for step in t[300:]:
		if step%(p+1)==0:
			if p!=0:c=cont(mu,w,x[-1]-x[-1-p])
			else:c=np.array([0.,0.])
		else:c=np.array([0.,0.])
		x.append(x_tp1(theta,w,x[-1],c))
		if p != 0:mu=mu_tp1(mu,0.05,x[-1]-x[-1-p],p)
	x=np.array(x)
	ax=f.add_subplot(2,3,i)
	if p!=0: tit='p='+str(p)
	else:tit='Chaos'
	ax.set_title(tit)
	ax.plot(t,x[:,0],label='x1',linestyle='dashed')
	ax.plot(t,x[:,1],label='x2',linestyle=':')
	ax.plot(t,x[:,0]*.5+x[:,1]*.5,label='(x1+x2)/2')
#	ax.set_legend()
	ax.set_xlim(600,630)
	g=py.figure()
	ax1=g.add_subplot(111)
	ax1.set_title('p='+str(p))
	ax1.scatter(t,x[:,0],label='x1')
#	py.plot(t,x[:,1],label='x2')
#	py.plot(t,x[:,0]*.5+x[:,1]*.5,label='(x1+x2)/2')
#	py.legend()
	ax1.set_xlim(0,700)
	i+=1
f.savefig('robo_diffp.png')
py.show()
