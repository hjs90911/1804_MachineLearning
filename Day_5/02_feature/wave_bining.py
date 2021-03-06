import numpy as np 
import mglearn

X, y = mglearn.datasets.make_wave(n_samples=100)
bins = np.linspace(start=-3, stop=3, num=11)
print("bins: {}".format(bins))
which_bin = np.digitize(X, bins=bins)
print("\ndata:\n", X[:5])
print("\nwhich_bin:\n", which_bin[:5])