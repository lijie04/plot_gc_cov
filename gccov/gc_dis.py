"""
The :mod:`gccov.coverm` pile up coverm.
"""

# Author: Jie Li <jlli6t@gmail.com>
# License: GNU v3.0
# Copyrigth: 2021

import sys
import pandas as pd

from biosut import gt_file, gt_path, io_seq

def window_for_gc_depth(fasta, all_depth, window_size:int=1000):
    """
    Generage window for gc ratio computing.

    Parameters:
    -----------
    fasta : str
        Input fasta file.
    all_depth: str
        Depth file from samtools depth command.
    window_size : int.
        Sliding window size you prefer, default is 1000.

    Returns:
    --------
        Return a list of gc ratio, order in line with inputted sequence.
    """
    all_depth = pd.read_csv(depth, sep="\t", header=None, index_col=0)
    fh = gt_file.perfect_open(fasta)
    dt_return = pd.DataFrame(columns=["gc", "depth"])
    start = []

    for t, seq, _ in io_seq.iterator(fh):
        seq_depth = all_depth.loc[t]
        for i in range(window_size, len(seq)+1-1000, window_size):
            window_seq = seq[start:i] # last window with non-enough bases will be dropped, no big deal.
            window_depth = seq_depth.iloc[start:i, 2].sum()/window_size
            dt_return = dt_return.append(pd.Series())
            gc.append(string_gc(window_seq)*100/len(window_seq))
            depth.append(window_depth)
    return gc, depth
