#!/usr/bin/env python

#f="test.fasta"
f = 'O5_contigs_more500.fasta'
cov = 'O5-1_Contigs_coverage'
broca1='O5-1_brocadia_ids_bin23.list'
broca2='O5-1_brocadia_ids_bin40.list'

import seqs_utils
from seqs_utils import gc
#from bam_utils import check
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

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
broca1 = list(pd.read_csv(broca1, squeeze=True, header=None, index_col=None))
broca2 = list(pd.read_csv(broca2, squeeze=True, header=None, index_col=None))

#print(contig_list)
#print(type(contig_list))
#print("NODE_37_length_157569_cov_28.822448" in list(contig_list))
#sys.exit()

print(new.GC_content)
print(new.Mean)
#sys.exit()
new = new[new['Mean']<100]
plt.figure(1)
#print(set(['blue' if i in brocadia_contigs else 'grey' for i in new.index]))
c = []
for i in new.index:
	if i in broca1:
		c.append('red')
	elif i in broca2:
		c.append('blue')
	else:
		c.append('grey')
#new.plot.scatter(x='GC_content', y='Mean', c=['red' if i in broca1 'blue' if i in broca2 else 'grey' for i in new.index], s=1)
new.plot.scatter(x='GC_content', y='Mean', c=c, s=1)
plt.xlabel('GC_content')
plt.ylabel('Coverage')
plt.savefig('O5-1_gc_and_coverage_scatter_plot_2500bp_100cov.pdf')

#plt.figure(2)
#new = 




