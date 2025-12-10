from logger import log_prediction

# Inside your face recognition loop
actual = 'Alice'  # For testing or labeled environment
predicted = 'Unknown'  # From your model output

log_prediction(actual, predicted)
