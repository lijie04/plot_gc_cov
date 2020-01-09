# gccov is for plotting gc content and coverage/abundance and visualize it. 
#
# for test
#
#./../gccov.py --contigs test.fasta --coverage test.coverage -prefix test -bins_dir $PWD  -contig_len 0
#
# some explainations:
# --contigs : you should provide a fasta format file for script to calculate GC content
# --coverage : you should provide a pre-calculated coverage file, at lease the fastas you want in the final result should pre-calculated coverage
# -bins_dir : This is supposed to be a directory contains fasta files which end with -suffix you provide, then references from these fastas will be colored in different color in final plot.
#

Basically, it calculate the GC content of each sequence, then readin the coverage of each sequences, if you provide -bins_dir, then it will scatter different color on each fasta file you provide with -bins_dir

Next plan:
1. add a coverage/abundance calculation module

