#! /usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
import os
import pickle
import scipy.fftpack
import scipy.signal
import sys

def plot(data, freq, fname):
    """Plot the given data.

    :param data: the raw voltage values
    :param freq: used sampling frequency
    :param bstart: starting brightness level
    :param bend: end brightness level
    """
    # Perform STFT (https://en.wikipedia.org/wiki/Short-time_Fourier_transform)
    f, t, Zxx = scipy.signal.stft(data, freq, nperseg=1000)

    plt.rcParams['agg.path.chunksize'] = 10000 # allows opening huge graphs
    plt.tight_layout()

    # Plot frequencies over time
    # plt.pcolormesh(t, f, np.abs(Zxx))
    # Add a horizontal line to make it easier to see differences
    plt.axhline(y=700000, color="yellow")

    # Label the graph
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title("Brightness change from trace {}".format(fname))
    # Show the graph
    plt.show()

    print(scipy.signal.find_peaks(Zxx))

def main():
    tracefile = sys.argv[1]

    data = None
    with open(tracefile, 'rb') as fp:
        data = pickle.load(fp)

    plot(data, 2E6, tracefile)

if __name__ == "__main__":
    main()
