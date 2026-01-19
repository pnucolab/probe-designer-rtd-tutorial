SoloMicrobe
==========================

**SoloMicrobe** is a microbial probe designer tool. It is a Pipeline that designs, filters, scores, and reports oligonucleotide probes for input sequences to target microbial transcripts while checking against host/microbiome references. It produces candidate and "safe" probes (with scoring) to support microbial spatial transcriptomics studies.

Quick Start to use the web interface
------------------------------------

This guide explains how to use the Probe Designer web interface to submit your gene or probe sequences and download results.

1. Open the Web Interface
-------------------------

- Open your web browser.
- Go to: https://mpd.pnucolab.com/?view=upload
  

2. Submit a Job
---------------

1. **Choose Input Type:**

   Select either *Gene Sequence* or *Probe Sequence* at the top of the form.

2. **Paste Your Sequence:**

   Paste your FASTA-formatted sequence into the large text box.
   (If you leave it empty, an example will be used.)

3. **Configure Targets:**

   - Select the *Host Organism* (default: **Human**).
   - Optionally, check *Additional Microbiome* and choose a microbiome group.
   - At least one of *Host* or *Microbiome* must be selected.

4. **Set Parameters (Optional):**

   - (For gene input) Set *Probe Length* (default: **30**; range: 20–50).
   - Set *K-mer Length* (default: **14**; minimum: 14).
   - Set *Max Mismatches* (default: **2**; range: 0–2).

5. **Submit:**

   Click the *Submit* button.
   The page will show the job status and progress.

3. Download Results
-------------------

- When your job is complete, download the result files from the links shown on the page.




.. toctree::
   :maxdepth: 4
   :caption: Contents

   quickstart
   userguide
