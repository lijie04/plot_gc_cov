# gccov is for plotting gc content and coverage/abundance and visualize it. 
#
# for test
#./../gccov.py --contigs test.fasta --coverage test.coverage -prefix test -bins_dir $PWD  -contig_len 0

Basically, it calculate the GC content of each sequence, then readin the coverage of each sequences, if you provide -bins_dir, then it will scatter different color on each fasta file you provide with -bins_dir

Next plan:
0. add dot size scale, bubbles?
1. add a coverage/abundance calculation module
