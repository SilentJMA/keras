from keras.backend.config import backend

if backend() == "torch":
    # When using the torch backend,
    # torch needs to be imported first, otherwise it will segfault
    # upon import.
    import torch

from keras.backend.common.keras_tensor import KerasTensor
from keras.backend.common.keras_tensor import any_symbolic_tensors
from keras.backend.common.keras_tensor import is_keras_tensor
from keras.backend.common.name_scope import name_scope
from keras.backend.common.stateless_scope import StatelessScope
from keras.backend.common.stateless_scope import get_stateless_scope
from keras.backend.common.stateless_scope import in_stateless_scope
from keras.backend.common.variables import AutocastScope
from keras.backend.common.variables import get_autocast_scope
from keras.backend.common.variables import is_float_dtype
from keras.backend.common.variables import is_int_dtype
from keras.backend.common.variables import standardize_dtype
from keras.backend.common.variables import standardize_shape
from keras.backend.config import epsilon
from keras.backend.config import floatx
from keras.backend.config import image_data_format
from keras.backend.config import set_epsilon
from keras.backend.config import set_floatx
from keras.backend.config import set_image_data_format
from keras.backend.config import standardize_data_format
from keras.utils.io_utils import print_msg

# Import backend functions.
if backend() == "tensorflow":
    print_msg("Using TensorFlow backend")
    from keras.backend.tensorflow import *  # noqa: F403

    distribution_lib = None
elif backend() == "jax":
    print_msg("Using JAX backend.")
    from keras.backend.jax import *  # noqa: F403
elif backend() == "torch":
    print_msg("Using PyTorch backend.")
    from keras.backend.torch import *  # noqa: F403

    distribution_lib = None
elif backend() == "numpy":
    print_msg(
        "Using NumPy backend.\nThe NumPy backend does not support "
        "training. It should only be used for inference, evaluation, "
        "and debugging."
    )
    from keras.backend.numpy import *  # noqa: F403

    distribution_lib = None
else:
    raise ValueError(f"Unable to import backend : {backend()}")
