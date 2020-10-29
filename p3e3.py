from matplotlib.pylab import *
import numpy as np

L = 1.04
N = 20
dx = L/N

x = np.linspace(0,L,N+1)
#i=2,4,8

#Arreglo con la solucion

dt = 1.
Nt = 5000#97200
u_k  = np.zeros((N+1))
u_km1  = np.zeros((N+1))

#Condicion inicial
u_k[:]  = 20.

#Condiciones de Borde
u_k[0]  = 0.
u_k[-1] = 0.

K = 79.5 # m2 / s
c = 450. # J/kg C
rho=7800.# kg/m3

def u_fourier(x,t,L,alp,N=50000):
	suma=0.
	for n in range(1,N):
		suma += (40*(1-(-1**n)))/(n*np.pi) * np.sin(n*np.pi*x/L)*np.exp(-alp * (np.pi*n/L)**2 * t)
	return suma 

dts = [1.,5.,10.,50.,100.]
for dt in dts:
	alp=K*dt/(c*rho* dx**2)*0.029
	Nt = 97200./dt
	u_k  = np.zeros((N+1))
	u_km1  = np.zeros((N+1))
	
	#Condicion inicial
	u_k[:]  = 20.
	
	#Condiciones de Borde
	u_k[0]  = 0.
	u_k[-1] = 0.
	time=[]
	data2=[]
	data4=[]
	data8=[]
	for k in range(int(Nt)-1):
		t = dt * k
		time.append(t/3600.)
		#print(f'k= {k},t={t}')
		for i in range(1,N):
			u_km1[i] = u_k[i] + alp*(u_k[i+1] - 2*u_k[i] + u_k[i-1])
		u_k = u_km1
		data2.append(u_k[2])
		data4.append(u_k[4])
		data8.append(u_k[8])
		#if k%200 == 0:
		#	plot(x,u_k[:])
	figure(0)
	#subplot(3,1,1)
	title('x=0.104 m')
	ylabel("Temperatura [°C]")
	xlabel("Tiempo [horas]")
	yticks([20,15,10,5],[20,15,10,5])
	grid(True)
	plot(time,data2,label=f'Malla 20 dt= {int(dt)}s')
	legend(loc='upper right')
	savefig("x=0.104.png")
	figure(1)
	#subplot(3,1,2)
	title('x=0.208 m')
	ylabel("Temperatura [°C]")
	xlabel("Tiempo [horas]")
	plot(time,data4,label=f'Malla 20 dt= {int(dt)}s')
	grid(True)
	legend(loc='upper right')
	savefig("x=0.208.png")
	figure(2)
	#subplot(3,1,3)
	title('x=0.416 m')
	ylabel("Temperatura [°C]")
	xlabel("Tiempo [horas]")
	yticks([20,18,16,14],[20,18,16,14])
	grid(True)
	plot(time,data8,label=f'Malla 20 dt= {int(dt)}s')
	legend(loc='upper right')
	savefig("x=0.416.png")
#figure(0)
#plot(array(time),u_fourier(0.104,array(time),L,alp))
#figure(1)
#plot(array(time),u_fourier(0.208,array(time),L,alp))
#figure(2)
#plot(array(time),u_fourier(0.416,array(time),L,alp))
show()