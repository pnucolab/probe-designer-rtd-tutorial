How to Use the Web Interface
============================

The web interface provides an intuitive way to submit gene or probe sequences for probe design, configure analysis parameters, and download results. This section describes the general workflow, recommended preprocessing steps, and best practices for optimal results.

General Overview
----------------

1. **Access the Web Interface**

   - Open your web browser.
   - Navigate to https://mpd.pnucolab.com/?view=upload

2. **Choose Input Type**

   - Select either "Gene Sequence" or "Probe Sequence" at the top of the form.
   - Only one input type can be used per submission.

3. **Paste Your Sequence**

   - Paste your sequence(s) in FASTA format into the large text box.
   - If left empty, an example sequence will be used.
   - For multiple sequences, each must have its own header line (starting with ``>``).

4. **Configure Targets**

   - Select the "Host Organism" (Human or Mouse).
   - Optionally, enable "Additional Microbiome" and select a microbiome group (e.g., Human Gut Microbiome).
   - At least one of "Host" or "Microbiome" must be selected.

5. **Set Parameters (Optional)**

   - For gene input: Set "Probe Length" (default: 30; range: 20–50).
   - Set "K-mer Length" (default: 14; minimum: 14).
   - Set "Max Mismatches" (default: 2; range: 0–2).

6. **Submit the Job**

   - Click the "Submit" button.
   - The interface will display job status and progress.
   - When the job is complete, download the result files from the links provided.

Preprocessing Steps and Recommendations
---------------------------------------

1. **Sequence Quality and Format**

   - Ensure all input sequences are in valid FASTA format.
   - Remove any non-standard characters or ambiguous bases (only A, T, C, G, N are accepted).
   - For gene input, use full-length coding sequences or transcripts for best results.
   - For probe input, ensure each probe is on a separate entry with a unique header.

2. **Input Size and Complexity (recommended but not mandatory)**

   - For large or highly repetitive sequences, consider splitting into smaller regions to avoid long processing times.
   - Avoid submitting excessively long sequences in a single job unless necessary.

3. **Parameter Selection**

   - Default parameters are suitable for most use cases.
   - For higher specificity, reduce "Max Mismatches" or increase "K-mer Length".
   - For broader detection, increase "Max Mismatches" or decrease "K-mer Length".

4. **Target Selection**

   - Select the host and/or microbiome targets relevant to your study.
   - For host-associated microbiome studies, enabling both host and microbiome filtering is recommended to avoid cross-hybridization.

5. **Result Interpretation**

   - Download and review the output files.
   - Use the provided links to visualize alignments or further analyze probe specificity.

Best Practices
--------------

- **Check Input Format:** Always validate your FASTA files before submission.
- **Use Descriptive Headers:** For probe sequences, include metadata (e.g., start/end positions, gene IDs) in the header for easier tracking.
- **Monitor Job Status:** Large jobs may take several minutes. You may close the browser tab if needed, but **be sure to save your job ID**. To retrieve your results later, simply return to the web interface and visit:

  ``https://mpd.pnucolab.com/?job_id={your_job_id}``

  The page will automatically display the status and results for your job.
