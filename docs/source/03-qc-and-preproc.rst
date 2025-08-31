QC and Pre-processing
=====================

Steps
-----

1. Inspect quality with **FastQC** / **MultiQC**.
2. Trim adapters and low-quality bases using **fastp** or **cutadapt**.
3. Optionally remove host reads by mapping to the host genome.

Example (fastp)
---------------

.. code-block:: bash

   fastp -i sample_R1.fastq.gz -I sample_R2.fastq.gz \
         -o clean_R1.fastq.gz -O clean_R2.fastq.gz \
         --detect_adapter_for_pe --thread 8 --html fastp_report.html
