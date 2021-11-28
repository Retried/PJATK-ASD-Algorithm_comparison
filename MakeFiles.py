import numpy as np


def SaveTxt(name, arr):
    np.save(name + ".npy", arr)


size = 500000

sorted_arr = np.arange(1, size)
SaveTxt("sorted_arr", sorted_arr)
reverse_sorted_arr = sorted_arr[::-1]
SaveTxt("reverse_sorted_arr", reverse_sorted_arr)
np.random.shuffle(reverse_sorted_arr)
SaveTxt("random_arr", reverse_sorted_arr)
