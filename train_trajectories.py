# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 10:09:58 2022

@author: daniel
"""

import shelve
import os
from Tempotron import Tempotron
import numpy as np
import matplotlib.pyplot as plt

"""Parameters"""
seed = 0
np.random.seed(seed)
epochs = 100  # Number of learning epochs
total_time = 2000.0  # Simulation time
V_rest = 0.0  # Resting potential
tau = 10.0  # 
tau_s = 2.5
threshold = 3.0
efficacies = 1.8 * np.random.random(10) - 0.50
learning_rate = 1e-4


"""Load data"""
dirname = os.path.dirname(__file__)
example_data = os.path.join(
    dirname, 'data',
    'grid-seed_duration_shuffling_tuning_10_2000_non-shuffled_tuned')
data = shelve.open(example_data)

"""Structure and label spike times"""
spike_times1 = [(np.array(data['75']['grid_spikes'][x][:10], dtype=object), True) for x in data['75']['grid_spikes']]
spike_times2 = [(np.array(data['60']['grid_spikes'][x][:10], dtype=object), False) for x in data['60']['grid_spikes']]
all_spikes = spike_times1 + spike_times2

print('synaptic efficacies:', efficacies, '\n')

tempotron = Tempotron(V_rest, tau, tau_s, efficacies, threshold)

tempotron.plot_membrane_potential(0, total_time, all_spikes[0][0])

tempotron.train(all_spikes, epochs, learning_rate=learning_rate)
print(tempotron.efficacies)

tempotron.plot_membrane_potential(0, total_time, all_spikes[0][0])
plt.show()
