Supported File Format
=====================

The Probe Designer pipeline accepts input sequences in **FASTA format**. This format is required for both gene and probe sequence inputs.

FASTA Format Details
--------------------

- Each sequence entry begins with a header line starting with the ``>`` character, followed by a sequence identifier and optional description.
- The sequence itself is provided on one or more lines immediately following the header.

**Example: Gene Sequence**

.. code-block:: text

   >gene1 description
   ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC

**Example: Probe Sequence**

.. code-block:: text

   >probe_1|start=1|end=20|gene1
   ATGCGTACGTAGCTAGCTAG
   >probe_2|start=21|end=40|gene1
   CTAGCTAGCTAGCTAGCTAG

Requirements
------------

- **No blank lines** between header and sequence.
- **No special characters** in the sequence (only A, T, C, G, or N).
- **Consistent line endings** (Unix ``\n`` or Windows ``\r\n`` are both accepted).
- **Multiple sequences** can be included in a single file, each with its own header.

For probe input, the header may include metadata such as start/end positions and transcript IDs, but this is optional.

Required Tools for CLI and Local Deployment
===========================================

To run the CLI and deploy the pipeline locally, the following tools and dependencies are required:

Python Environment
------------------

- **Python 3.11** (recommended; minimum 3.8)
- **Conda** (for environment management)
- **Required Python packages:**  
  Install via ``pip install -r requirements.txt``

Bioinformatics Tools
--------------------

- **Samtools** (for SAM/BAM file manipulation; install via Bioconda)
- **gffread** (for GTF/GFF file parsing; install via Bioconda)
- **razers3** (for fast short-read mapping; included in ``bin/`` directory or install via Bioconda)


Installation Commands
---------------------

.. code-block:: bash

   # Create and activate environment
   conda create -n probeset python=3.11
   conda activate probeset

   # Install Python dependencies
   pip install -r requirements.txt


Directory Structure
-------------------

- ``bin/``: Contains executables (gffread, razers3, etc.)
- ``core/``: Core Python modules for probe design and scoring
- ``gene_sequences/``: Input gene sequences
- ``probe_sequences/``: Input probe sequences
- ``outputs/alignments/``: Output files and logs

Additional Notes
----------------

- Ensure all required binaries are in your ``PATH`` or the ``bin/`` directory.
- For large datasets, sufficient disk space and memory are recommended.
- For web deployment, additional tools such as **FastAPI**, **Celery**, and **Redis** are required 
