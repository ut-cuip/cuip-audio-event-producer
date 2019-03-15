import numpy as np


def resize(data, axis, new_size):
    shape = list(data.shape)

    pad_shape = shape[:]
    pad_shape[axis] = np.maximum(0, new_size - shape[axis])

    shape[axis] = np.minimum(shape[axis], new_size)
    shape = np.stack(shape)

    slices = [slice(0, s) for s in shape]

    resized = np.concatenate([
      data[slices],
      np.zeros(np.stack(pad_shape))
    ], axis)

    # Update shape.
    new_shape = list(data.shape)
    new_shape[axis] = new_size
    resized.reshape(new_shape)
    return resized
