import matplotlib.pyplot as plt
import numpy as np

plt.figure(1)
plt.subplot(2, 1, 1)
A = .8
f0 = 2
phi = np.pi/2
fs = 100
t = np.arange(-1, 1, 1.0/fs)
x = A * np.cos(2*np.pi*f0*t+phi)
plt.plot(t, x)
plt.axis([-1,1,-0.8,0.8])
plt.title('analog')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.subplot(2, 1, 2)
plt.plot(t, x, '*')
plt.grid(True)
plt.title('digital')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
