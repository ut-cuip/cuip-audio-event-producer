import argparse
import numpy as np
from scipy.io import wavfile

parser = argparse.ArgumentParser(description='Read file and process audio')
parser.add_argument('wav_file', type=str, help='File to read and process')


def process_file(wav_file):
    sr, data = wavfile.read(wav_file)
    if data.dtype != np.int16:
        raise TypeError('Bad sample type: %r' % data.dtype)

    # local import to reduce start-up time
    from audio.processor import WavProcessor, format_predictions

    with WavProcessor() as proc:
        predictions = proc.get_predictions(sr, data)

    print(format_predictions(predictions))


if __name__ == '__main__':
    args = parser.parse_args()
    process_file(**vars(args))
    
