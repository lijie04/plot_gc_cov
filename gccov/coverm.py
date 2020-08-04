
"""
The :mod:`gccov.coverm` plot scatter bubbles.
"""

# Author: Jie Li <mm.jlli6t@gmail.com>
# License: GNU v3.0
# Copyrigth: 2019

import os
import sys
from biosut import gt_exe, gt_file

class coverm:
	def __init__(self, bam, outfile):
		gt_exe.is_executable('coverm')
		self.bam = bam
		self.outfile = outfile

	def run(self):
		cmd = ['coverm', 'contig', '--bam-files', self.bam, '--methods', 'mean',
				'--min-covered-fraction', '0', '--output-format', 'dense',
				'--contig-end-exclusion', '0']
		#proc = subprocess.Popen(cmd, shell=True, stdout=self.outfile, encoding='utf-8')
		print(self.outfile)
		with open(self.outfile, 'w') as outf:
			gt_exe.exe_cmd(cmd)
		gt_file.check_exist(self.outfile, check_empty=True)
