import data_viz
import gzip
import sys
import os
import argparse


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='Parallel Arrays Handeling.',
        prog='plot_gtex.py')

    # require file name as one of the inputs
    parser.add_argument('--output_file',
                        type=str,
                        help='Name of the output plot',
                        required=True)

    # require group type as one of the inputs
    parser.add_argument('--group_type',
                        type=str,
                        help='The group type. e.g. SMTS',
                        required=True)

    # require gene as one of the inputs
    parser.add_argument('--gene',
                        type=str,
                        help='Target gene. e.g. ACTA2',
                        required=True)

    # require meta file as one of the inputs
    parser.add_argument('--sample_attributes',
                        type=str,
                        help='A txt file containing meta data',
                        required=True)

    # require gene data as one of the inputs
    parser.add_argument('--gene_reads',
                        type=str,
                        help='Database of genes',
                        required=True)

    return parser.parse_args()


def linear_search(key, L):
    for i in range(len(L)):
        if key == L[i]:
            return i
    return -1


def binary_serach(key, L):
    lo = 0
    hi = len(L)-1
    while (hi > lo):
        mid = (hi + lo) // 2

        if key == L[mid][0]:
            return L[mid][1]

        if (key < L[mid][0]):
            hi = mid - 1
        else:
            lo = mid + 1

    return -1


if __name__ == '__main__':
    main()
