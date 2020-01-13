#!/usr/bin/env python

#f="test.fasta"
f = 'O5_contigs_more500.fasta'
cov = 'O5-2_Contigs_coverage'

import seqs_utils
from seqs_utils import gc
#from bam_utils import check
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import argparse

def read_pars(args):
	p = argparse.ArgumentParser(description=__doc__)
	p.add_argument('--contigs', dest='contigs', required=True, 
				help='contigs/scaffolds for GC content')
	p.add_argument('--coverage', dest='coverage', required=True,
				help='coverage file')
	p.add_argument('-contig_len', dest='contig_len', default='2500',
				help='contig length cutoff for GC content and plot, [2500]')
	


#print(seqs_utils)
final_gc = gc(f, 2500)
table = final_gc.count_fasta_gc()
table = pd.DataFrame.from_dict(table, orient='index', columns=['GC_content'])

#print(table)
#pd.DataFrame.from_dict(table, orient='index', columns=['GC_content']).to_csv("gc_content.txt", sep="\t")
table.to_csv("gc_content.txt", sep="\t")

cov = pd.read_csv(cov, sep="\t", header=0, index_col=0)
new = cov.merge(table, how='inner', left_index=True, right_index=True) # get contigs have both gc and coverage
new.to_csv('gc_and_coverage.csv', sep='\t')

## readin for colors of dots
contig_list = list(pd.read_csv('O5-2_bin24_ids.list', squeeze=True, header=None, index_col=None))
#print(contig_list)
#print(type(contig_list))
#print("NODE_37_length_157569_cov_28.822448" in list(contig_list))
#sys.exit()

print(new.GC_content)
print(new.Mean)
#sys.exit()
new = new[new['Mean']<100]
plt.figure(1)
print(set(['blue' if i in contig_list else 'grey' for i in new.index]))
new.plot.scatter(x='GC_content', y='Mean', c=['blue' if i in contig_list else 'grey' for i in new.index], s=1)
plt.xlabel('GC_content')
plt.ylabel('Coverage')
plt.savefig('O5-2_gc_and_coverage_scatter_plot_2500bp_100cov.pdf')

#plt.figure(2)
#new = 




