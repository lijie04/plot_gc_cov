

#####################################################
##												   ##
# seqs_utils.py -- fasta and fastq files utils	   ##
##												   ##
#####################################################


import Bio
from Bio.SeqIO.FastaIO import SimpleFastaParser
from Bio.SeqIO.QualityIO import FastqGeneralIterator
from pandas import DataFrame

from .system_utils import check_file_exists


class gc:
	_gc_dict = {}
	def __init__(self, seqs, len_cutoff=2500):
		self.seqs = seqs
		check_file_exists(self.seqs)
		self.len_cutoff = len_cutoff
		print(len_cutoff)

	def count_fasta_gc(self):
		with open(self.seqs) as fasta_handle:
			# use low-level parser to speed up when dealing with large data
			for title, seq in SimpleFastaParser(fasta_handle):
				if len(seq) > self.len_cutoff:
					self._gc_dict[title] = [self._count_string_gc(seq.upper()), len(seq)]
		#	print(self._gc_dict)
			return self._reform()

	def count_fastq_gc(self):
		with open(self.seqs) as fastq_handle:
			# use low-level parser to speed up when dealing with large data
			for title, seq, qual in FastqGeneralIterator(fastq_handle):
				if len(seq) >= self.len_cutoff:
					self._gc_dict[title] = self._count_string_gc(seq)
			return self._reform()
	
	def _count_string_gc(self, string):
#		_total_gc = string.count('G') + string.count('C')+string.count('g') + string.count('c')
		_total_gc = string.count('G') + string.count('C')
		return round(_total_gc/len(string)*100., 2) # round to reduce float

	def _reform(self):
		return DataFrame.from_dict(self._gc_dict, orient='index', columns=['GC_content', 'Seq_length'])
		



