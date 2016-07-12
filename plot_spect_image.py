import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('inputfile', help='A datafile created by the old SPECT camera')
parser.add_argument(
    '--outputfile', '-o', required=False,
    dest='outputfile',
    help='If given, save the image to outputfile'
)


if __name__ == '__main__':

    args = parser.parse_args()

    data = np.fromfile(args.inputfile, dtype='<u2')
    width = np.sqrt(data.size)
    assert width.is_integer()
    width = int(width)

    img = data.reshape((width, width))

    plt.imshow(
        img,
        cmap='inferno',
        interpolation='nearest',
    )
    plt.colorbar()
    if args.outputfile:
        plt.savefig(args.outputfile, dpi=300)
    else:
        plt.show()
