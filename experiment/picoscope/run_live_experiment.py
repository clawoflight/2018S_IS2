#! /usr/bin/env python3
from picoscope import ps3000a

import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import scipy.signal

import os
import pickle
import sys
import time

numSamples = 10000000

def setupScope():
    """Open a connection to the picoscope and setup channel & sampling rate.

    :return: [picoscope, sampling rate]
    """
    ps = ps3000a.PS3000a()

    res = ps.setSamplingFrequency(10E6, numSamples)
    ps.setChannel("A", "AC", 10)
    print("Sampling @ %f MHz, %d samples" % (res[0] / 1E6, res[1]))
    return (ps, res[0])

def plot(data, freq, bstart, bend):
    """Plot the given data.

    :param data: the raw voltage values
    :param freq: used sampling frequency
    :param bstart: starting brightness level
    :param bend: end brightness level
    """
    # Perform STFT (https://en.wikipedia.org/wiki/Short-time_Fourier_transform)
    f, t, Zxx = scipy.signal.stft(data, freq, nperseg=1000)

    plt.rcParams['agg.path.chunksize'] = 10000 # allows opening huge graphs

    # Plot frequencies over time
    plt.pcolormesh(t, f, np.abs(Zxx))
    # Add a horizontal line to make it easier to see differences
    plt.axhline(y=700000, color="yellow")

    # Label the graph
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title("Brightness change from {} to {}".format(bstart, bend))
    plt.tight_layout()
    # Show the graph
    plt.show()

def main():
    # Parse command-line arguments
    bstart = int(sys.argv[1])
    bend = int(sys.argv[2])

    # Set initial hue brightness
    os.system("hueadm light 1 \"={}\"".format(bstart))

    # Setup the osci
    (scope, rate) = setupScope()

    # Start collecting data from the osci
    scope.runBlock()

    # Change brightness levels
    os.system("hueadm light 1 \"={}\"".format(bend))
    # time.sleep(.01)
    os.system("hueadm light 1 \"={}\"".format(bstart))

    # Wait until data was collected
    while not scope.isReady():
        pass

    # Download data from the osci
    data = scope.getDataV(0, numSamples)

    plot(data, rate, bstart, bend)

    # Serialize the data for later re-use
    with open("{}-{}@{}.pickle".format(bstart, bend, rate), 'wb') as fp:
        pickle.dump(data, fp)

if __name__ == "__main__":
    main()
