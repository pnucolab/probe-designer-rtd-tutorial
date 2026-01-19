How to Use the Command-Line Interface (CLI)
===========================================

The command-line interface (CLI) provides a flexible and scriptable way to run the probe design pipeline locally. This guide covers environment setup, input preparation, command usage, parameter explanations, and output interpretation.

1. Environment Setup
--------------------

a. **Create and activate a Conda environment:**

.. code-block:: bash

   conda create -n probeset python=3.11
   conda activate probeset

b. **Install dependencies:**

.. code-block:: bash

   pip install -r requirements.txt

c. **Ensure binaries are available:**
   - The CLI requires `gffread` and `razers3` to be in your `PATH` or in the `bin/` directory.

2. Input Preparation
--------------------

- **Gene Sequence Input:**  
  Prepare your gene sequence(s) in FASTA format. Each entry must start with a header line (beginning with `>`), followed by the nucleotide sequence.

- **Probe Sequence Input:**  
  Prepare your probe sequences in FASTA format. Each probe should have a unique header.

- **Only one input type (gene or probe) is allowed per run.**

**Example: Gene Sequence FASTA**

.. code-block:: text

   >gene1
   ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC

**Example: Probe Sequence FASTA**

.. code-block:: text

   >probe_1|start=1|end=20|gene1
   ATGCGTACGTAGCTAGCTAG
   >probe_2|start=21|end=40|gene1
   CTAGCTAGCTAGCTAGCTAG

3. Basic Usage
--------------

Run the pipeline with either a gene or probe sequence:

**Gene Sequence Example:**

.. code-block:: bash

   python probe_designer.py --gene-sequence ">gene1\nATCG..." --species human --probe-length 30 --max-mismatches 2 --align-host

**Probe Sequence Example:**

.. code-block:: bash

   python probe_designer.py --probe-sequence ">probe1\nATCG..." --species human --max-mismatches 2 --align-host

**Input from File:**

.. code-block:: bash

   python probe_designer.py --gene-sequence "$(cat my_gene.fasta)" --species mouse --align-host

**Input from Standard Input:**

.. code-block:: bash

   cat my_probes.fasta | python probe_designer.py --probe-sequence-stdin --species human --align-host

4. Main Options and Defaults
----------------------------

- ``--gene-sequence`` / ``-gs``: Gene sequence in FASTA format (mutually exclusive with --probe-sequence)
- ``--probe-sequence`` / ``-ps``: Probe sequence in FASTA format (mutually exclusive with --gene-sequence)
- ``--gene-sequence-stdin``: Read gene sequence from standard input
- ``--probe-sequence-stdin``: Read probe sequence from standard input
- ``--species`` / ``-s``: Host organism (**default:** human; options: human, mouse)
- ``--probe-length``: Probe length (**default:** 30; used only for gene input, range: 20–50)
- ``--max-mismatches``: Maximum allowed mismatches (**default:** 2; range: 0–2)
- ``--kmer-length``: K-mer length for safety check (**default:** 14; minimum: 14)
- ``--align-microbiome``: Align against microbiome genomes (**default:** False; add this flag to enable)
- ``--align-host``: Align against host transcriptome (**default:** False; add this flag to enable)
- ``--parallelism`` / ``-p``: Number of parallel worker threads (**default:** all available)
- ``--skip-annotation``: Skip gene name annotation (**default:** False; add this flag to skip)
- ``--task-id``: Custom task/job ID for organizing outputs

**To see all options and help:**

.. code-block:: bash

   python probe_designer.py --help

5. Example Workflows
--------------------

**A. Design probes from a gene and align to human and gut microbiome:**

.. code-block:: bash

   python probe_designer.py --gene-sequence "$(cat my_gene.fasta)" --species human --probe-length 30 --max-mismatches 2 --align-host --align-microbiome

**B. Analyze a set of custom probes against mouse transcriptome:**

.. code-block:: bash

   python probe_designer.py --probe-sequence "$(cat my_probes.fasta)" --species mouse --max-mismatches 1 --align-host

**C. Use a specific k-mer length and skip annotation:**

.. code-block:: bash

   python probe_designer.py --gene-sequence "$(cat my_gene.fasta)" --kmer-length 16 --skip-annotation --align-host

6. Output Interpretation
------------------------

- Results and logs are saved in the ``outputs/alignments/`` directory, organized by job/task ID.
- Key output files may include:
  - ``filtered_probe_alignments.sam``: Filtered alignments
  - ``filtered_probe_alignments_annotated.sam``: Annotated alignments (if annotation enabled)
  - ``safe_probes_scores.txt``: Probe scoring results
  - ``kmer_matches_report.txt``: K-mer safety report
  - ``pipeline_log.txt``: Log of the pipeline run

7. Troubleshooting and Tips
---------------------------

- **Input errors:** Ensure your FASTA files are properly formatted and contain only valid nucleotide characters.
- **Missing tools:** If you see errors about missing `gffread` or `razers3`, ensure they are in your `PATH`.
- **Resource usage:** For large jobs, ensure you have sufficient memory and disk space.
- **Parallelism:** Use the `--parallelism` option to control the number of worker threads for faster processing on multi-core systems.
- **Job organization:** Use the `--task-id` option to assign a custom name to your job for easier tracking.
