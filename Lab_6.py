import scipy.signal as sci
import numpy as np
import matplotlib.pyplot as plt

#y_n Coeffectients = [1, 0.7, -0.45, -0.6]
#x_n Coeffectiants = [0.8, -0.44, 0.36, 0.02]

y_n = [1, 0.7, -0.45, -0.6]
x_n = [0.8, -0.44, 0.36, 0.02]

xn = np.zeros(20)
xn[0] = 1

h_n = sci.lfilter(y_n, x_n, xn)

n = np.arange(0, len(h_n), 1)

plt.stem(n, h_n)
plt.show()

step_respnse = np.ones(25)

y_n = sci.convolve(step_respnse, h_n)



n = np.arange(0, len(y_n), 1)
plt.stem(n, y_n, 'b')
plt.plot(n,y_n, 'g')
plt.show()


B = [1,0.1,-0.2]
A = [1,1]

w, h = sci.freqz(B,A)

AngInDeg = np.angle(h, deg=True)



plt.subplot(211); plt.plot(w/np.pi,20*np.log10(np.abs(h)),'r-',linewidth=4); plt.grid(True); 
plt.title('|H($\Omega$)|'); plt.ylabel('Magnitude [dB]')
plt.subplot(212); plt.plot(w/np.pi,AngInDeg,'r-',linewidth=4); plt.grid(True); 
plt.title('Angle of |H($\Omega$)|'); plt.xlabel('$\Omega$/$\pi$'); plt.ylabel('degree')
plt.tight_layout()
plt.show()



#_____________________________________________________________________________________________________

B_4 = [1,0.13,0.52,0.3]
A_4 = [0.16, -0.48, 0,  -0.16]


#impulse response
x_n_4 = np.zeros(10)
x_n_4[0] = 1

h_n_4_impulse = sci.lfilter(B_4, A_4, x_n_4)

#step response
x_n_4_step = np.ones(50)

y_n_4_step = sci.convolve(h_n_4_impulse, x_n_4_step)

n= np.arange(0,len(h_n_4_impulse),1)
k = np.arange(0,len(y_n_4_step),1)

plt.subplot(211)
plt.stem(n, h_n_4_impulse)

plt.subplot(212)
plt.stem(k, y_n_4_step)

plt.show()

w, h = sci.freqz(B_4,A_4)

AngInDeg = np.angle(h, deg=True)



plt.subplot(211); plt.plot(w/np.pi,20*np.log10(np.abs(h)),'r-',linewidth=4); plt.grid(True); 
plt.title('|H($\Omega$)|'); plt.ylabel('Magnitude [dB]')
plt.subplot(212); plt.plot(w/np.pi,AngInDeg,'r-',linewidth=4); plt.grid(True); 
plt.title('Angle of |H($\Omega$)|'); plt.xlabel('$\Omega$/$\pi$'); plt.ylabel('degree')
plt.tight_layout()
plt.show()
