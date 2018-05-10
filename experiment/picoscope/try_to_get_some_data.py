from picoscope import ps3000a

import matplotlib.pyplot as plt
import numpy as np
import scipy.fftpack
import scipy.signal

import os
import pickle
import sys
import time

numSamples = 2000000

def setupScope():
    ps = ps3000a.PS3000a()

    res = ps.setSamplingFrequency(2E6, numSamples)
    ps.setChannel("A", "AC", 10)
    print("Sampling @ %f MHz, %d samples" % (res[0] / 1E6, res[1]))
    return [ps, res[0]]

def plot(data, freq, bstart, bend):
    f, t, Zxx = scipy.signal.stft(data, freq, nperseg=1000)

    plt.rcParams['agg.path.chunksize'] = 10000
    plt.pcolormesh(t, f, np.abs(Zxx))
    plt.axhline(y=700000, color="yellow")
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.title("Brightness change from {} to {}".format(bstart, bend))
    plt.tight_layout()
    plt.show()

def main():
    bstart = int(sys.argv[1])
    bend = int(sys.argv[2])
    os.system("hueadm light 1 \"={}\"".format(bstart))
    [scope, rate] = setupScope()
    scope.runBlock()
    os.system("hueadm light 1 \"={}\"".format(bend))
    time.sleep(.1)
    os.system("hueadm light 1 \"={}\"".format(bstart))

    while not scope.isReady():
        pass

    data = scope.getDataV(0, numSamples)
    plot(data, rate, bstart, bend)
    with open("{}-{}.pickle".format(bstart, bend), 'wb') as fp:
        pickle.dump(data, fp)

if __name__ == "__main__":
    main()
