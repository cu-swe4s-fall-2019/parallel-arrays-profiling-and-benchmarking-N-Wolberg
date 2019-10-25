import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import math_lib
matplotlib.use('Agg')
# With helpful permission from Chi-Ju Wu


def boxplot(data, meta, x_label, y_label, title, out_file):
    """
    plot boxplot for input parallel array and save the result as a png file
    """
    fig, ax1 = plt.subplots(figsize=(12, 8))

    ax1.boxplot(data)

    # Hide these grid behind plot objects
    ax1.set_axisbelow(True)
    ax1.set_title(title)
    ax1.set_xlabel(x_label)
    ax1.set_ylabel(y_label)

    # set tick labels and export the result
    ax1.set_xticklabels(meta, rotation=90, fontsize=8)
    fig.savefig(out_file, bbox_inches='tight')


def histogram(L, out_file_name):
    """plot boxplot for an input array and save the result as a png file
    """
    plt.hist(L, bins=30)
    plt.ylabel('Frequency')
    plt.xlabel('Value')
    plt.title('mean: ' + str(math_lib.list_mean(L)) + ' ' +
              'stdev: ' + str(math_lib.list_stdev(L)))
    plt.savefig(out_file_name)
    pass


def combo(L, out_file_name):
    """plot boxplot for an input array and save the result as a png file
    """
    fig, axs = plt.subplots(1, 2, figsize=(10, 6))
    axs[0].hist(L, bins=30)
    axs[1].boxplot(L)
    fig.suptitle('mean: ' + str(math_lib.list_mean(L)) + ' ' +
                 'stdev: ' + str(math_lib.list_stdev(L)))
    fig.savefig(out_file_name)
    pass
