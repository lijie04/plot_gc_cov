# plot_gc_cover is for plotting gc and coverage/abundance and visualize it. 
#
# for test
#./../plot_gc_cover.py --contigs test.fasta --coverage test.coverage -prefix test -bins_dir $PWD  -contig_len 0
#
# --contigs : you should provide a fasta format file for script to calculate GC content
# --coverage : you should provide a pre-calculated coverage file, at lease the fastas you want in the final result should pre-calculated coverage
# -bins_dir : This is supposed to be a directory contains fasta files which end with -suffix you provide, then references from these fastas will be colored in different color in final plot.
#
#
