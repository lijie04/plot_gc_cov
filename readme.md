gccov is for plotting gc content and coverage and visualize it.
Basically, it calculate the GC content of each sequence, then readin the coverage of each sequences, if you provide -bins_dir, then it will scatter different color on each fasta file you provide with -bins_dir

dependencies:
coverm (0.3.2). Developed under coverm-v0.3.2
python packages: pandas (0.25.3), matplotlib (3.1.2), seaborn (0.8.1), Bio (1.72)
if you want to test:
You can try with the test data from /test/ /path/to/gccov --contigs test.fasta --coverage test.coverage -prefix test -bins_dir $PWD -contig_len 0 If you want to plot dot as bubbles: /path/to/gccov --contigs test.fasta --coverage test.coverage -prefix test -bins_dir $PWD -contig_len 0 -scale If you want calculate coverage and plot: /path/to/gccov --contigs test.fasta --bam-file test.bam -prefix test -bins_dir $PWD -contig_len 0 -scale If you don't have dots want to color, you can just leave -bins_dir alone: /path/to/gccov --contigs test.fasta --bam-file test.bam -prefix test -contig_len 0 -scale

Some detailed explainations:
--contigs: it means a fasta format file for script to calculate GC content. --coverage: it means a pre-calculated coverage file, at least some of the sequences in --contigs you want to show in the final plot. --bam-file: sorted bam file as input to calculate coverage of references -bins_dir: this is optional. With fasta files end with -suffix contained in -bins_dir, you will get fancy bubbles that colored in different color. For example, if you provide two fa files in -bins_dir, they contain 10 and 9 sequences respectively, then the 10 and 9 sequences will be colored with different color in final plot while other dots are grey.

#Next plans:

add an option to choose solid circle or hollow circle
add pysam
