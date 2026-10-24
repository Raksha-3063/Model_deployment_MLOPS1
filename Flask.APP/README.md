# Flask Multiplication Table App 🐍🐳

A simple Flask web application that accepts a number from the user and generates its multiplication table from 1 to 10. This project is part of my hands-on **MLOps learning journey**, focusing on Docker containerization and Docker Hub.

## 🚀 Project Overview

The application allows users to enter a number through a web interface and displays its multiplication table. It is built using Python and Flask and packaged into a Docker image for portability and deployment.

## 🛠️ Tech Stack

- **Python** — Application logic
- **Flask** — Web framework
- **HTML** — User interface
- **Docker** — Application containerization
- **Docker Hub** — Docker image storage and distribution

## 📂 Project Structure

```text
Flask.APP/
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Raksha-3063/Model_deployment_MLOPS.git
cd Model_deployment_MLOPS
```

Navigate to the Flask project directory if it is inside a subfolder.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the application

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## 🐳 Run with Docker

### 1. Build the Docker image

```bash
docker build -t multiplication-table-app .
```

### 2. Run the container

```bash
docker run -d --name multiplication-table -p 5000:5000 multiplication-table-app
```

Open http://localhost:5000 to use the application.

### 3. View the running container

```bash
docker ps
```

### 4. Stop the container

```bash
docker stop multiplication-table
```

## 📦 Docker Hub

The Docker image is published on Docker Hub.

**Image:** `rakshacc/multiplication-table-app:v1`

Pull the image:

```bash
docker pull rakshacc/multiplication-table-app:v1
```

Run the pulled image:

```bash
docker run -d --name multiplication-table -p 5000:5000 rakshacc/multiplication-table-app:v1
```

## 🎯 Learning Outcomes

- Built a web application using Flask.
- Created a Dockerfile to package the application.
- Built and tagged a Docker image.
- Ran the application inside a Docker container.
- Pushed and pulled Docker images using Docker Hub.
- Practiced the fundamentals of containerization as part of an MLOps workflow.

## 🔮 Future Improvements

- Deploy the container to AWS EC2 or Google Cloud.
- Set up CI/CD for automated builds and deployments.
- Add automated testing.
- Explore Kubernetes for container orchestration.

---

**Author:** Raksha C C

**GitHub:** [Raksha-3063](https://github.com/Raksha-3063)

**MLOps Repository:** [Model_deployment_MLOPS](https://github.com/Raksha-3063/Model_deployment_MLOPS)