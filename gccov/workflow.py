"""
The :mod:`gccov.workflow` pileup the workflow.
"""

# Author: Jie Li <mm.jlli6t@gmail.com>
# License: GNU v3.0
# Copyrigth: 2019

import os
import sys
import argparse

import pandas as pd
from biosut.gt_path import real_path

from biosut import gt_file, gt_path
from biosut.io_seq import gc_to_dict

from gccov.scatter import scatter
from gccov.coverm import coverm
from gccov.version import Version

def read_arg(args):

	p = argparse.ArgumentParser(description=Version.show_version())
	required_argument = p.add_argument_group('Required arguments')

	required_argument.add_argument('--contigs', required=True,
								help='contigs/scaffolds for GC content')

	mutual_required_argument = p.add_argument_group('Mutually exclusive required argument')
	mutual_rgs = mutual_required_argument.add_mutually_exclusive_group(required=True)
	mutual_rgs.add_argument('--coverage', nargs='+',
						help='one or two coverage file, with one column coverage')
	mutual_rgs.add_argument('--bam_file', nargs='+',
						help='one or two sorted bam file')

	optional_arguments = p.add_argument_group('Optional arguments')
	optional_arguments.add_argument('-scale', default=False, action='store_true',
					help='set to scale scatter dots with your scaffolds/contigs length')
	optional_arguments.add_argument('-size', default=1, type=float,
					help='bubles relative size you want, default is 1, you can set to 1.5, 3, 5 or so')
	optional_arguments.add_argument('-prefix', default='gc_coverage',
					help='prefix of outputs, [gc_coverage]')
	optional_arguments.add_argument('-contig_len', default=0, type=float,
					help='contig length cutoff for GC content and plot, [0]')
	optional_arguments.add_argument('-cov_width', default='0', type=str,
					help='cov range you want to plot, for example 0-100, single 0 means all, [0]')
	optional_arguments.add_argument('-gc_width', default='0', type=str,
					help='gc ratio range you want to plot, for example 0-80, single 0 means all, [0]')
	optional_arguments.add_argument('-bins_dir', default=None,
					help='bins dir to color genomes you provide')
	optional_arguments.add_argument('-suffix', default='fa',
					help='suffix of bins if you profile -bins_dir, [fa]')
	optional_arguments.add_argument('-outdir', default=os.getcwd(),
					help='output dir')
	return p.parse_args()

class stream:

	def exe(args):
		arg = read_arg(args)
		outdir = gt_path.sure_path_exist(arg.outdir)
		gc_table = gc_to_dict(arg.contigs, len_cutoff=0, length=True)

		gc_table = pd.DataFrame.from_dict(gc_table).T
		gc_table.columns = ['gc_count', 'seq_length']
		gc_table['gc_ratio'] = gc_table.gc_count/gc_table.seq_length*100.
		print("Finished get GC content.\n")

		gc_table.to_csv(outdir +'/'+ arg.prefix + '_gc_content.txt', sep='\t')
		flag = 0
		if arg.bam_file:
			if len(arg.bam_file) == 1:
				cov = os.path.join(outdir, arg.prefix+'.coverage')
				coverm_pile = coverm(arg.bam_file, cov)
				coverm_pile.run()
			else:
				flag = 1
				cov1 = os.path.join(outdir, arg.prefix+os.path.basename(arg.bam_file[0]) + '.coverage')
				cov2 = os.path.join(outdir, arg.prefix+os.path.basename(arg.bam_file[1]) + '.coverage')
				coverm_pile = coverm(arg.bam_file[0], cov1)
				coverm_pile.run()
				coverm_pile = coverm(arg.bam_file[1], cov2)
				coverm_pile.run()
		else:
			if len(arg.coverage) == 1:
				cov = arg.coverage
			else:
				cov1 = arg.coverage[0]
				cov2 = arg.coverage[1]
		if flag:
			gt_file.check_file_exist(cov1, cov2, check_empty=True)
			cov1 = pd.read_csv(cov1, sep="\t", header=0, index_col=0)
			cov1.columns = ['coverage1']
			gc_cov = gc_table.merge(cov1, how='inner', left_index=True, right_index=True)
			cov2 = pd.read_csv(cov2, sep="\t", header=0, index_col=0)
			cov2.columns = ['coverage2']
			print('Finished get Coverage.\n')
			gc_cov = gc_cov.merge(cov2, how='inner', left_index=True, right_index=True)
		else:
			gt_file.check_file_exist(cov, check_empty=True)
			cov = pd.read_csv(cov, sep="\t", header=0, index_col=0)
			#print(cov)
			cov.columns = ['coverage']
			print('Finished get Coverage.\n')
			# get contigs have both gc and coverage
			gc_cov = gc_table.merge(cov, how='inner', left_index=True, right_index=True)
		gc_cov.to_csv(outdir + '/' + arg.prefix +'_gc_and_coverage.csv', sep='\t')

		new = gc_cov[gc_cov.seq_length >= arg.congit_len]
		if '-' in arg.cov_width:
			cov_width = [float(i) for i in arg.cov_width.split('-')]
			new = new[(new.coverage >= cov_width[0]) & (new.coverage <= cov_width[1])]

		if '-' in arg.gc_width:
			gc_width = [float(i) for i in arg.gc_width.split('-')]
			new = new[(new.gc_ratio >= gc_width[0]) & (new.gc_ratio <= gc_width[1])]

		for f in gt_file.find_files(arg.bin_dir, suffix=arg.suffix):
			for i in io_seq.seq_to_dict(f).keys():
				if i not in new.index:
					new = new.append(gc_cov.loc[i])

		scatter_plot = scatter(new, outdir+'/'+arg.prefix+'.pdf', \
								arg.bins_dir, arg.suffix, arg.scale, \
								arg.size, flag=flag)
#		scatter_plot = scatter(new, outdir+pars['prefix']+'.pdf', **pars)
		scatter_plot.plot()
