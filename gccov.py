#!/usr/bin/env python

import seqs_utils
from seqs_utils import gc
#from bam_utils import check
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import argparse
from system_utils import check_file_exists,check_files_exist,make_full_path,check_path_exists
import os
from scatter import scatter

def read_pars(args):

	p = argparse.ArgumentParser(description=__doc__)
	p.add_argument('--contigs', dest='contigs', required=True, 
				help='contigs/scaffolds for GC content')
	p.add_argument('--coverage', dest='coverage', required=True,
				help='coverage file, with column name Coverage')
	p.add_argument('-scale', dest='scale', default=False, action='store_true',
				help='set to scale scatter dots with your scaffolds/contigs length')
	p.add_argument('-prefix', dest='prefix', default='gc_coverage',
				help='prefix of outputs, [gc_coverage]')
	p.add_argument('-contig_len', dest='contig_len', default=2500, type=float,
				help='contig length cutoff for GC content and plot, [2500]')
	p.add_argument('-cov_width', dest='cov_width', default='0', type=str,
				help='cov range you want to plot, for example 0-100, single 0 means all, [0]')
	p.add_argument('-bins_dir', dest='bins_dir', default=None,
				help='bins dir to color genomes you provide')
	p.add_argument('-suffix', dest='suffix', default='fa',
				help='suffix of bins if you profile -bins_dir, [fa]')
	p.add_argument('-o', dest='outdir', default=os.getcwd(),
				help='output dir')

	return vars(p.parse_args())


if __name__ == '__main__':
	pars = read_pars(sys.argv)
	check_files_exist([pars['contigs'], pars['coverage']])
	if pars['bins_dir']:check_path_exists(pars['bins_dir'])
	outdir = make_full_path(pars['outdir'])
	final_gc = gc(pars['contigs'], pars['contig_len'])
	gc_table = final_gc.count_fasta_gc()
	gc_table = pd.DataFrame.from_dict(gc_table, orient='index', columns=['GC_content', 'Seq_length'])
	
	#print(gc_table)

	gc_table.to_csv(outdir + pars['prefix'] + "_gc_content.txt", sep="\t")
	
	cov = pd.read_csv(pars['coverage'], sep="\t", header=0, index_col=0)
	# get contigs have both gc and coverage
	new = cov.merge(gc_table, how='inner', left_index=True, right_index=True)
	new.to_csv(outdir + pars['prefix'] +'_gc_and_coverage.csv', sep='\t')
	
	if '-' in pars['cov_width']:
		cov_width = [float(i) for i in pars['cov_width'].split('-')]
		new = new[(new.Coverage >= cov_width[0]) & (new.Coverage <= cov_width[1])]
		
	scatter_plot = scatter(new, outdir, pars['bins_dir'], pars['suffix'], pars['scale'])
	scatter_plot.plot()

	os.rename(outdir+'scatter_bubbles.pdf', outdir+pars['prefix']+'.pdf')



