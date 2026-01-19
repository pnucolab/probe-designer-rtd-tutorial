How to Deploy Source Code on Local Machines
===========================================

This section provides step-by-step instructions for deploying the Probe Designer pipeline on your local machine. Two deployment methods are covered:

- **A. Native (manual) deployment using Conda and Python**
- **B. Containerized deployment using Docker Compose**

A. Native Deployment (Conda & Python)
-------------------------------------

1. **Clone the Repository**

.. code-block:: bash

   git clone https://github.com/pnucolab/probe-designer.git
   cd probeset/microbe_genome

2. **Create and Activate a Conda Environment**

.. code-block:: bash

   conda create -n probeset python=3.11
   conda activate probeset

3. **Install Python Dependencies**

.. code-block:: bash

   pip install -r requirements.txt


4. **Start the Backend API**

.. code-block:: bash

  uvicorn backend.main_app:app --host 0.0.0.0 --port 8000 --reload
 
  celery -A backend.celery_worker worker --loglevel=info  

5. **Start the Frontend**

.. code-block:: bash

   cd frontend
   npm install --no-audit 
   npm run dev -- --host

   # The frontend will be available at http://localhost:5173/

6. **Access the Application**

- Frontend: http://localhost:5173/
- Backend API: http://localhost:8000/

B. Docker Compose Deployment
----------------------------

Docker Compose provides a convenient way to deploy all services (backend, frontend, Celery worker, Redis) with a single command.

1. **Install Docker and Docker Compose**

- [Docker installation guide](https://docs.docker.com/get-docker/)
- [Docker Compose installation guide](https://docs.docker.com/compose/install/)

2. **Clone the Repository**

.. code-block:: bash

   git clone https: //github.com/pnucolab/probe-designer.git
   cd probeset/microbe_genome

3. **Start All Services**

.. code-block:: bash

   docker-compose up --build -d

   # This will build and start all containers in the background.

4. **View Logs**

.. code-block:: bash

   docker-compose logs -f

5. **Stop All Services**

.. code-block:: bash

   docker-compose down

6. **Access the Application**

- Frontend: http://localhost:4000/
- API Docs: http://localhost:4000/docs

**Note:** The default ports may be changed in `docker-compose.yml` or the frontend/backend configuration files.

C. Additional Notes and Tips
----------------------------

- **Configuration:**  
  Environment variables such as `CELERY_BROKER_URL`, `CELERY_RESULT_BACKEND`, and `ALLOWED_ORIGINS` can be set in the environment or in a `.env` file for Docker Compose.

- **Persistent Data:**  
  Output files and logs are stored in the `outputs/alignments/` directory. For Docker deployments, consider mounting a local volume for persistent storage.

- **Customizing Ports:**  
  If you need to change the default ports, edit `docker-compose.yml` and the frontend/backend configuration files accordingly.

- **Rebuilding Images:**  
  If you change the source code or dependencies, rebuild the containers:

  .. code-block:: bash

     docker-compose build

- **Updating Dependencies:**  
  For native deployments, re-run `pip install -r requirements.txt` and `conda install ...` as needed.

