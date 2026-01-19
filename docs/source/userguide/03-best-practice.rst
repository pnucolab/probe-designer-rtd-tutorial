General Best Practices for Using the Probe Designer Pipeline
===========================================================

To ensure reliable, accurate, and efficient results when using the Probe Designer pipeline (via web interface or CLI), follow these best practices:

1. Input Preparation
--------------------

- **FASTA Format:**  
  Always use a valid FASTA format for gene and probe sequences. Each entry must start with a header line (`>`) followed by the sequence.

- **Sequence Quality:**  
  Remove non-standard characters. Use high-quality, full-length coding sequences.

- **Descriptive Headers:**  
  For probes, include metadata (e.g., start/end positions, gene IDs) in the header for easier tracking and downstream analysis.

- **Input Size:**  
  For very large genes or probe sets, consider splitting into smaller jobs to avoid long processing times.

2. Parameter Selection
----------------------

- **Target Selection:**  
  Select both host and relevant microbiome targets to minimize cross-hybridization, especially for host-associated studies.

3. Resource Management
----------------------

- **System Resources:**  
  Ensure sufficient memory, CPU, and disk space, especially for large datasets or when running multiple jobs in parallel.

- **Parallelism:**  
  Use the `--parallelism` option (CLI) to optimize performance on multi-core systems.

- **Job Organization:**  
  Use the `--task-id` option (CLI) or save job IDs (web) to keep track of your analyses and results.

4. Troubleshooting
------------------

- **Input Errors:**  
  Double-check the input format and content if you encounter errors or failed jobs.

- **Dependency Issues:**  
  Ensure all required tools (gffread, razers3) are accessible.
