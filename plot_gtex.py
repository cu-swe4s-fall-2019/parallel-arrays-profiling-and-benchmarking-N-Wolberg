import data_viz
import gzip
import sys
import os
import argparse


# parse arguments
def parse_args():
    parser = argparse.ArgumentParser(
        description='Takes .',
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
    pass

def binary_serach(key, L):
    pass


def main():


if __name__ == '__main__':
    main()
