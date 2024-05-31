import numpy as np

def fft(data):
  """
  Performs the Fast Fourier Transform (FFT) on a given data set.

  Args:
      data: A numpy array containing the data for which to compute the FFT.

  Returns:
      A numpy array containing the frequency spectrum of the data.
  """
  return np.fft.fft(data)

# Sample data
data = np.random.rand(100)

# Calculate FFT
fft_result = fft(data)

# Print the magnitude of the frequency spectrum (absolute values)
print(np.abs(fft_result))
