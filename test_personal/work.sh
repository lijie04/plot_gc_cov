#less /30days/s4506266/projects/2.liutao_6samples/1.4samples_metagenome/8.gtdbtk_taxonomy_of_bins/coverm/O5-2/bins_coverage_abundance.prof|cut -f 1,6 > O5-2_Contigs_coverage
#grep \> O5-2_bin.24.fa|sed 's/>//g'  > O5-2_bin24_ids.list

#./../plot_gc_cover.py --contigs O5_contigs_more500.fasta --coverage O5-2_Contigs_coverage -prefix O5-2_gc_and_coverage_scatter_plot_2500bp_60cov  -bins_dir $PWD -cov_width 0-60
export PATH=/90days/s4506266/softwares/coverm-x86_64-unknown-linux-musl-0.3.2/:$PATH
#./../bin/gccov --contigs O5_contigs_more500.fasta -prefix test -bins_dir $PWD -cov_width 0 -scale --bam-file O5-2_mapping_contigs.srt.bam
./../bin/gccov --contigs hk_eff_contigs_500.fasta -prefix test_hk_eff -cov_width 0 -scale --bam-file hk_eff_mapping_contigs_uniq_hits.bam_srt
