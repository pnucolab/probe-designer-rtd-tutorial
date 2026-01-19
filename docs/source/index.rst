SoloMicrobe
==========================

**SoloMicrobe** is a microbial probe designer tool. It is a Pipeline that designs, filters, scores, and reports oligonucleotide probes for input sequences to target microbial transcripts while checking against host/microbiome references. It produces candidate and "safe" probes (with scoring) to support microbial spatial transcriptomics studies.

Quick Start to use the web interface
------------------------------------

1. Navigate to https://mpd.pnucolab.com/?view=upload
2. Default settings:

   - Host Organism: Human
   - Target Transcriptome: Human Transcriptome
   - Probe Length (bp): 30
   - K-mer Length (bp): 14
   - Max Mismatches: 2

3. Click Submit to process the sample file.
4. For custom analysis, paste FASTA-formatted sequence text (gene or probe sequences) into the web UI.







.. toctree::
   :maxdepth: 4
   :caption: Contents

   quickstart
   userguide
