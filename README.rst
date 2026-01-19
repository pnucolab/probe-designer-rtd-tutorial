SoloMicrobe
=========================

This repository provides comprehensive documentation for the SoloMicrobe tool. 
It includes a detailed user guide for the web interface, instructions for using the command-line interface (CLI), 
and a Docker Compose file for easy local deployment.

Prerequisites
=============

To run the command-line interface or host the web application locally, an OpenCL-compatible device is required. 
OpenCL (Open Computing Language) enables parallel computing across heterogeneous systems and is essential for the
high-performance computational tasks performed by Cas-OFFinder.

System Requirements:
--------------------
• OS: Linux (recommended); should work on macOS with minor changes.
• Disk / RAM: Enough space for reference genomes and alignment outputs
• Conda / mamba: to create the probeset environment from conda_environment.yml.
• Python: 3.11 (environment uses Python 3.11).
• Node.js / npm: Node >=16 and npm for the frontend
• Redis: a Redis server available for Celery broker/back-end (default redis://localhost:6379/1).
• Docker: docker / docker-compose if you prefer containerized deployment.
• Python pip deps: FastAPI, Uvicorn, Celery, Redis client, Biopython, pandas, numpy, requests, lxml, pydantic, etc. See requirements.txt.
• Alignment & utilities: samtools, gffread, RazerS3 — required for probe alignment and processing 


Citations
=========



License
=======

Copyright (C) 2026 Mekonnen Abyot Melkamu and Jeongbin Park

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see https://www.gnu.org/licenses/.
