import functools
import operator

import perfplot
import numpy as np

myValues = [[1,2,3], [4,5,6], [7,8,9]]

def list_comp(values):
    return [x for sublist in values for x in sublist]

def reduce_method(values):
    return functools.reduce(operator.concat, values)

def sum_method(values):
    return sum(values, [])

def numpy_flat(values):
    return list(np.array(values).flat)

def numpy_concat(values):
    return list(np.concatenate(values))

def nested_loops(values):
    result = []
    for sublist in values:
        for x in sublist:
            result.append(x)
    return result


perfplot.show(
    #defining the input
    setup = lambda n: [list(range(10))] * n, #different imput sizes n

    # functions to evaluate
    kernels = [
        list_comp,
        reduce_method,
        sum_method,
        numpy_flat,
        numpy_concat,
        nested_loops
    ],

    #input size
    n_range = [2**k for k in range(16)],
    labels = ["List comp", "Reduce", "Sum", "Numpy flat", "Numpy concat", "Nested Loops"],
    xlabel = "Input size"
)
