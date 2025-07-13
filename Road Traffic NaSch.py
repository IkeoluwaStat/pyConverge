# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 00:16:43 2022

@author: Engr. IkeOluwa
"""

#%%

# import numpy
import numpy as np

# import matplotlib.pyplot
import matplotlib.pyplot as plt

#%%

# length of road
L = 250

# number of vehicles
N = 25

# set number of time steps to simulate
T = 250

# specify p
p = 0.8

#%%

# create list of gaps
gaps = [ np.random.randint(1, 1 + L//N) for i in range(N) ]
# create list of positions
pos = [ 0 for i in range(N) ]
pos[0] = gaps[0]
for i in range(1, N):
    pos[i] = pos[i-1] + gaps[i]
# set vmax
vmax = 2
# create list of velocities
vel = [ np.random.randint(0, vmax+1) for i in range(N) ]

#%%

print('i\t x[i]\t v[i]')
for i in range(N):
    print(repr(i) + '\t' + repr(pos[i]) + '\t' + repr(vel[i]))

#%%

# for-loop over vehicles
for i in range(N):
    # acceleration
    if vel[i] < vmax:
        vel[i] = vel[i] + 1
    # slowing down
    if i < N-1:
        if vel[i] >= pos[i+1] - pos[i]:
            vel[i] = pos[i+1] - pos[i] - 1
    # impose periodic boundary condition on velocities
    else:
        if vel[i] >= (L - pos[i] - 1) + pos[0]:
            vel[i] = (L - pos[i] - 1) + pos[0] - 1
    # random deceleration
    if vel[i] >= 1:
        if np.random.rand() < p:
            vel[i] = vel[i] - 1
    # move vehicles
    pos[i] = pos[i] + vel[i]
    # impose periodic boundary condition on positions
    if pos[N-1] >= L:
        newpos0 = pos.pop(N-1)
        newvel0 = vel.pop(N-1)
        pos.insert(0, newpos0-L)
        vel.insert(0, newvel0)

#%%

print('i\t x[i]\t v[i]')
for i in range(N):
    print(repr(i) + '\t' + repr(pos[i]) + '\t' + repr(vel[i]))

#%%

# initialize traffic array
traffic = np.zeros((T,L))

#%%

# simulation proper
for t in range(T):
    # draw to traffic array
    for i in range(N):
        if vel[i] == 0:
            traffic[t, pos[i]] = 1
        elif vel[i] == 1:
            traffic[t, pos[i]] = 2
        else:
            traffic[t, pos[i]] = 3
    # update traffic
    for i in range(N):
        # acceleration
        if vel[i] < vmax:
            vel[i] = vel[i] + 1
        # slowing down
        if i < N-1:
            if vel[i] >= pos[i+1] - pos[i]:
                vel[i] = pos[i+1] - pos[i] - 1
        # impose periodic boundary condition on velocities
        else:
            if vel[i] >= (L - pos[i] - 1) + pos[0]:
                vel[i] = (L - pos[i] - 1) + pos[0] - 1
        # random deceleration
        if vel[i] >= 1:
            if np.random.rand() < p:
                vel[i] = vel[i] - 1
        # move vehicles
        pos[i] = pos[i] + vel[i]
        # impose periodic boundary condition on positions
        if pos[N-1] >= L:
            newpos0 = pos.pop(N-1)
            newvel0 = vel.pop(N-1)
            pos.insert(0, newpos0-L)
            vel.insert(0, newvel0)

#%%

plt.matshow(traffic)
plt.colorbar()
plt.axis('equal')
plt.show()

#%%

# Additional Exercises
# Simulations at Different Densities
# In the above simulation, we have 𝑁=25 vehicles over a road with 𝐿=100.

# You should plot the space-time diagrams for simulations at different 
# densities 𝑁/𝐿 to gain an intuition into the behavior of the NS model.

# Simulations with Different 𝑣max
# In the above simulation, we used 𝑣max=2.

# Run simulations with other values of 𝑣max, to better understand the behavior of the NS model.

# Plotting the Fundamental Diagram
# Choose a smaller region within the road, say 0≤𝑥≤20, as your measurement region.

# Every 20 time steps, compute the density 𝜌, which is the number of vehicles 
# in this region divided by 20, and the average velocity 𝑣¯ over all vehicles in this region.

# Collect a large number of points (𝜌,𝑣¯), and plot the scatter diagram of 𝑣¯ 
# against 𝜌. This is called the fundamental diagram of vehicular traffic.

# Further Explorations
# Two Lanes and Overtaking
# Most roads have more than one lane, and allows overtaking to occur.

# Think about how you would modify the simplest NS model shown here, 
# so that you can simulate two-lane vehicular traffic.

# Besides the additional complication for specifying the positions of vehicles, 
# you will also need to add new rules, so that a vehicle can make use of the 
# second lane to overtake another vehicle.

# City Traffic and Traffic Lights
# In this session, we have only discussed vehicular traffic in 1D. Naturally, 
# in a city, vehicular traffic is 2D, on a grid of criss-crossing roads.

# Besides this challenge to programming the NS model, city traffic is also 
# frequently regulated by traffic lights. Again, think of the rules you need 
# to perform city traffic simulations.

#%%

#%%

#%%

#%%

#%%

#%%