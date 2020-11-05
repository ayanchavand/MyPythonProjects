import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,linear_model

illness = datasets.load_diabetes()
#dict_keys(['data', 'target', 'DESCR', 'feature_names', 'data_filename', 'target_filename'])
print(illness)