
#####################################################
#													#
# scatter.py - plot scatter bubbles					#
#													#
#####################################################

import matplotlib
import matplotlib.pyplot as plt
import Bio
from Bio import SeqIO
import os
import pandas as pd


class scatter:
	def __init__(self, data, outdir, bins_dir=None, suffix='fa', scale=False):
		self.data = data
		self.bins_dir = bins_dir
		self.suffix = suffix
		self.scale = scale
		self.outdir = outdir

	def plot(self):
		if self.bins_dir:
			full_contigs_color = self._color_set()
		else:
			full_contigs_color = ['grey'] * len(data)
		plt.figure(1)
		if self.scale:
			self.data.plot.scatter(x='GC_content', y='Coverage',
								c=full_contigs_color, linewidths=.5,
								edgecolors='k', alpha=.5,
								s=self.data['Seq_length']/10000)
		else:
			self.data.plot.scatter(x='GC_content', y='Coverage',
								c=full_contigs_color,
								s=1)
		plt.xlabel('GC_content')
		plt.ylabel('Coverage')
		plt.savefig(self.outdir + 'scatter_bubbles.pdf')
		

	def _color_set(self):
		flag = 0
		contigs_color = pd.DataFrame()
		color_sets = ['blue', 'red', 'yellow', 'green', 'orange', 'purple', 'pink', 'black']
		for f in os.listdir(self.bins_dir):
			if f.endswith(self.suffix):
				#print(f)
				#print(color_sets[flag])
				f_ids = SeqIO.to_dict(SeqIO.parse(os.path.join(self.bins_dir, f), 'fasta')).keys()
				#print(f_ids)
				f_ids = pd.DataFrame(index=f_ids, columns=['color'], data=color_sets[flag])
				contigs_color = pd.concat([contigs_color, f_ids])
				flag += 1
		print(contigs_color)
		# then assign grey to all unbinned contigs
		
		full_contigs_color=[contigs_color.color.loc[i] if i in contigs_color.index else 'grey' for i in self.data.index]
		print('You are plotting with color : ', set(full_contigs_color))
		return full_contigs_color


