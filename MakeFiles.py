import numpy as np

size = 500000

sorted_arr = np.arange(1, size)
np.save("sorted_arr.npy", sorted_arr)

reverse_sorted_arr = sorted_arr[::-1]
np.save("reverse_sorted_arr.npy", reverse_sorted_arr)

np.random.shuffle(reverse_sorted_arr)
np.save("random_arr.npy", reverse_sorted_arr)
