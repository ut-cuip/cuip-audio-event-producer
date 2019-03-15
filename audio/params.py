# Architectural constants.
NUM_FRAMES = 96  # Frames in input mel-spectrogram patch.
NUM_BANDS = 64  # Frequency bands in input mel-spectrogram patch.
EMBEDDING_SIZE = 128  # Size of embedding layer.
MAX_FRAMES = 300

# Hyperparameters used in feature and example generation.
SAMPLE_RATE = 16000
STFT_WINDOW_LENGTH_SECONDS = 0.025
STFT_HOP_LENGTH_SECONDS = 0.010
NUM_MEL_BINS = NUM_BANDS
MEL_MIN_HZ = 125
MEL_MAX_HZ = 7500
LOG_OFFSET = 0.01  # Offset used for stabilized log of input mel-spectrogram.
EXAMPLE_WINDOW_SECONDS = 0.96  # Each example contains 96 10ms frames
EXAMPLE_HOP_SECONDS = 0.96     # with zero overlap.

# Parameters used for embedding postprocessing.
PCA_EIGEN_VECTORS_NAME = 'pca_eigen_vectors'
PCA_MEANS_NAME = 'pca_means'

# Hyperparameters used in training.
INIT_STDDEV = 0.01  # Standard deviation used to initialize weights.
LEARNING_RATE = 1e-4  # Learning rate for the Adam optimizer.
ADAM_EPSILON = 1e-8  # Epsilon for the Adam optimizer.

# Names of ops, tensors, and features.
VGGISH_MODEL = 'models/vggish_model.ckpt'
VGGISH_PCA_PARAMS = 'models/vggish_pca_params.npz'
VGGISH_INPUT_TENSOR_NAME = 'vggish/input_features:0'
VGGISH_OUTPUT_TENSOR_NAME = 'vggish/embedding:0'

YOUTUBE_CHECKPOINT_FILE = 'models/youtube_model.ckpt'

CLASS_LABELS_INDICES = 'models/class_labels_indices.csv'

# Predictions filter
PREDICTIONS_COUNT_LIMIT = 20
PREDICTIONS_HIT_LIMIT = 0.1
