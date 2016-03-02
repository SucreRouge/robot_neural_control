import numpy as np
import pylab as py

def sigma(x): return (1.+np.exp(-x))**-1
def x_tp1(theta,w,x,c): return sigma(theta+np.dot(w,x)+c)
def cont(mu,w,delta): return mu*np.dot(w,delta)
def mu_tp1(mu,lam,delta,p): return mu+lam*(delta[0]+delta[1])*p**-1


t=range(0,700)
f=py.figure()
theta=np.array([-3.4,3.8])
for e in np.linspace(-25,10,200):
	mu=-1
	w=np.array([[e,5.9],[-6.6,0.0]])
	x=[np.array([0.,0.])]
	for step in t:
		x.append(x_tp1(theta,w,x[-1],0.))
#	for step in t[300:]:
#		if step%(p+1)==0:
#			c=cont(mu,w,x[-1]-x[-1-p])
#		else:c=np.array([0.,0.])
#		x.append(x_tp1(theta,w,x[-1],c))
#		mu=mu_tp1(mu,0.05,x[-1]-x[-1-p],p)
	x=np.array(x)

#	py.title('p='+str(p))
#	py.plot(t,x[:,0],label='x1')
#	py.plot(t,x[:,1],label='x2')

	py.scatter(np.ones(701)[300:700]*e,x[300:700,0]*.5+x[300:700,1]*.5,label='(x1+x2)/2',s=0.1)
#	py.legend()
#	py.xlim(600,630)
#	f=py.figure()
#	py.title('p='+str(p))
#	py.scatter(t,x[:,0],label='x1')
#	py.plot(t,x[:,1],label='x2')
#	py.plot(t,x[:,0]*.5+x[:,1]*.5,label='(x1+x2)/2')
#	py.legend()
py.xlim(-25,10)
py.xlabel('$w_{11}$')
py.ylabel('$\\bar{x}$')
f.savefig('bif_w.png')

f=py.figure()
w=np.array([[-22.,5.9],[-6.6,0.0]])

for e in np.linspace(-10,10,200):
	mu=-1
	theta=np.array([e,3.8])
	x=[np.array([0.,0.])]
	for step in t:
		x.append(x_tp1(theta,w,x[-1],0.))
#	for step in t[300:]:
#		if step%(p+1)==0:
#			c=cont(mu,w,x[-1]-x[-1-p])
#		else:c=np.array([0.,0.])
#		x.append(x_tp1(theta,w,x[-1],c))
#		mu=mu_tp1(mu,0.05,x[-1]-x[-1-p],p)
	x=np.array(x)

#	py.title('p='+str(p))
#	py.plot(t,x[:,0],label='x1')
#	py.plot(t,x[:,1],label='x2')

	py.scatter(np.ones(701)[300:700]*e,x[300:700,0]*.5+x[300:700,1]*.5,label='(x1+x2)/2',s=0.1)
#	py.legend()
#	py.xlim(600,630)
#	f=py.figure()
#	py.title('p='+str(p))
#	py.scatter(t,x[:,0],label='x1')
#	py.plot(t,x[:,1],label='x2')
#	py.plot(t,x[:,0]*.5+x[:,1]*.5,label='(x1+x2)/2')
#	py.legend()
py.xlim(-10,10)
py.xlabel('$\\theta_1$')
py.ylabel('$\\bar{x}$')
f.savefig('bif_theta.png')
#py.show()
