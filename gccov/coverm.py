"""
The :mod:`gccov.coverm` pile up coverm.
"""

# Author: Jie Li <jlli6t near gmail.com>
# License: GNU v3.0
# Copyrigth: 2019

from biosut import gt_exe, gt_file


class CoverM:
    def __init__(self, bam, outfile):
        gt_exe.is_executable("coverm")
        self.bam = bam
        self.outfile = outfile

    def run(self):
        cmd = f"coverm contig --bam-files {self.bam} --methods mean " \
              f"--min-covered-fraction 0 --output-format dense " \
              f"--contig-end-exclusion 0 > {self.outfile}"

        gt_exe.exe_cmd(cmd, shell=True)
        gt_file.check_file_exist(self.outfile, check_empty=True)
