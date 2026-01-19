Quick Start: Using the Probe Designer Web Interface
===================================================

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
                                 

Quick Start: Using the Probe Designer Command-Line Interface (CLI)
==================================================================

This guide explains how to run the probe design pipeline from the command line.

1. Set Up the Environment
-------------------------

a. **Create and activate a Conda environment:**

.. code-block:: bash

   conda create -n probeset python=3.11
   conda activate probeset

b. **Install dependencies:**

.. code-block:: bash

   pip install -r requirements.txt


2. Prepare Your Input
---------------------

- Prepare your gene or probe sequences in FASTA format.
- Only one input type is allowed per run (gene or probe).

3. Basic Usage
--------------

Run the pipeline with either a gene or probe sequence:

**Gene Sequence Example:**

.. code-block:: bash

   python probe_designer.py --gene-sequence ">gene1\nATCG..." --species human --probe-length 30 --max-mismatches 2

**Probe Sequence Example:**

.. code-block:: bash

   python probe_designer.py --probe-sequence ">probe1\nATCG..." --species human --max-mismatches 2

4. Main Options and Defaults
----------------------------

- ``--gene-sequence`` / ``-gs``: Gene sequence in FASTA format (mutually exclusive with --probe-sequence)
- ``--probe-sequence`` / ``-ps``: Probe sequence in FASTA format (mutually exclusive with --gene-sequence)
- ``--species`` / ``-s``: Host organism (**default:** human; options: human, mouse)
- ``--probe-length``: Probe length (**default:** 30; used only for gene input, range: 20–50)
- ``--max-mismatches``: Maximum allowed mismatches (**default:** 2; range: 0–2)
- ``--kmer-length``: K-mer length for safety check (**default:** 14; minimum: 14)
- ``--align-microbiome``: Align against microbiome genomes (**default:** False)
- ``--align-host``: Align against host transcriptome (**default:** False)
- ``--skip-annotation``: Skip gene name annotation (**default:** False)

5. Additional Notes
-------------------

- Input sequences must be in proper FASTA format.
- At least one of ``--align-microbiome`` or ``--align-host`` should be set to True.
- For more options, run:

.. code-block:: bash

   python probe_designer.py --help

6. Output
---------

- Results and logs will be saved in the ``outputs/alignments/`` directory.
        
