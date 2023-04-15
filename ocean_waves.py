import numpy as np
import matplotlib.pyplot as plt

def ocean_waves():
    # Constants
    L = 20.0     # Length of the domain
    N = 256      # Number of grid points
    A = 1.0      # Amplitude of the waves
    k = 2*np.pi/L

    # Generate the x-coordinates
    x = np.linspace(0, L, N, endpoint=False)

    # Generate the initial condition (a Gaussian wave packet)
    sigma = 0.1*L
    u = A*np.exp(-0.5*((x-L/2)/sigma)**2)

    # Generate the time steps
    tmax = 10.0
    dt = 0.01
    tsteps = int(tmax/dt)

    # Generate the wave animation
    for t in range(tsteps):
        # Calculate the second derivative using a finite difference method
        d2udx
