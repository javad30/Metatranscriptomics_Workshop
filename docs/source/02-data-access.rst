Obtaining Data
==============

You can either bring your own FASTQ files or download public datasets.

Public Repositories
-------------------

- NCBI SRA
- ENA (European Nucleotide Archive)
- MG-RAST (for some community projects)

Example (SRA tools)
-------------------

.. code-block:: bash

   prefetch SRRXXXXXXX
   fasterq-dump SRRXXXXXXX -O fastq/ --split-files --threads 8

Metadata
--------

Always prepare a **metadata.tsv** with at least:

- SampleID
- Condition
- Replicate
- Batch
