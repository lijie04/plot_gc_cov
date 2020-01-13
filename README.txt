# gccov is for plotting gc content and coverage/abundance and visualize it.
Basically, it calculate the GC content of each sequence, then readin the coverage of each sequences, if you provide -bins_dir, then it will scatter different color on each fasta file you provide with -bins_dir

# if you want to test:
You can try with the test data from /test/
/path/to/gccov.py --contigs test.fasta --coverage test.coverage -prefix test -bins_dir $PWD -contig_len 0

# Some detailed explainations:
--contigs: it means a fasta format file for script to calculate GC content. \n
--coverage: it means a pre-calculated coverage file, at least some of the sequences in --contigs you want to show in the final plot. \n
--bam-file: sorted bam file as input to calculate coverage of references \n
-bins_dir: this is optional. With fasta files end with -suffix contained in -bins_dir, you will get fancy bubbles that colored in different color. For example, if you provide two fa files in -bins_dir, they contain 10 and 9 sequences respectively, then the 10 and 9 sequences will be colored with different color in final plot while other dots are grey. \n



