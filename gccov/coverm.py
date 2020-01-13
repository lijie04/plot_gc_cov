
###########################################################
#
# coverm.py - use this to pileup coverm from bam files  ###
#
###########################################################

import os
import sys
import subprocess
from .system_utils import check_software

class coverm:
	def __init__(self, bam, outfile):
		check_software('coverm')
		self.bam = bam
		self.outfile = outfile
	def run(self):
		cmd = ['coverm', 'contig', '--bam-files', self.bam, '--methods', 'mean', 
				'--min-covered-fraction', '0', '--output-format', 'dense',
				'--contig-end-exclusion', '0']
		#proc = subprocess.Popen(cmd, shell=True, stdout=self.outfile, encoding='utf-8')
		print(self.outfile)
		with open(self.outfile, 'w') as outf:
			proc = subprocess.Popen(cmd, stdout=outf)
		
		proc.wait()
		

		if proc.returncode !=0:
			sys.exit('Error encountered while running coverm')
		if not os.path.isfile(self.outfile):
			sys.exit('No output of coverm.')

