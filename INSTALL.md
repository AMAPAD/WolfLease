# WolfLease Installation Guide

## Method 1: Traditional Setup

### Prerequisites

1. The project uses Python 3, so make sure that [Python](https://www.python.org/downloads/) and [Pip](https://pip.pypa.io/en/stable/installation/) are preinstalled.
2. Git

### Steps

1. Clone the GitHub repository on your local system. Please make sure Git is installed in the system. After cloning the repository, move into it with the help of the `cd` command:

   ```bash
   git clone https://github.com/subodh30/WolfLease.git
   cd WolfLease
   ```

2. It's a good practice to create a virtual environment to store your project's dependencies separately from the global ones. You can install `virtualenv` with:

   ```bash
   pip3 install virtualenv
   ```

3. Run the following command in the base directory of this project. This will create a new folder `project_env` in your project directory:

   ```bash
   python3 -m venv project_env
   ```

4. Now activate the virtual environment:

   ```bash
   source project_env/bin/activate
   ```

5. Use `pip` to install all requirements of the project listed in the `requirements.txt` file:

   ```bash
   pip3 install -r requirements.txt
   ```

6. Run the backend server:

   ```bash
   python3 manage.py runserver
   ```

7. Run the frontend (in a new terminal):
   ```bash
   cd streamlit_app
   streamlit run app.py
   ```

## Method 2: Docker Setup

### Prerequisites

1. [Docker](https://docs.docker.com/get-docker/)
2. [Docker Compose](https://docs.docker.com/compose/install/)

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/subodh30/WolfLease.git
   cd WolfLease
   ```

2. Build and run with Docker Compose:

   ```bash
   docker compose up --build
   ```

   This will:

   - Start the MariaDB database
   - Launch the Django backend API (available at http://localhost:8000)
   - Start the Streamlit frontend (available at http://localhost:8501)

### Stopping the Application

```bash
docker compose down
```

OR

to remove all data including the database:

```bash
docker compose down -v
```
