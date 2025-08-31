Overview
========

Aim
---

Measure actively transcribed functions in microbial communities and link expression to taxa and pathways.

Inputs
------

- Raw paired-end RNA-seq FASTQ files (rRNA-depleted)
- Metadata (samples, treatments)
- Optional reference genomes or gene catalogs

Outputs
-------

- QC metrics
- rRNA removal stats
- Counts mapped to genes/pathways
- Differential activity results
- Visualizations

Pipeline Outline
----------------

1. Data access (SRA/ENA) & metadata
2. QC & pre-processing (quality trimming, adapters)
3. rRNA depletion in silico (if needed)
4. Read mapping vs. assembly strategy
5. Functional profiling (gene/pathway quantification)
6. Taxonomic profiling (optional, expression-weighted)
7. Differential analysis & visualization
