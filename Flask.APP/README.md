# Docker Commands — MLOps Learning Journey 🐳

This README documents the essential Docker commands I learned while containerizing a Flask multiplication-table application and publishing its image to Docker Hub.

## 📌 Project Details

- **Application:** Flask Multiplication Table App
- **Containerization:** Docker
- **Image Registry:** Docker Hub
- **Docker Hub Repository:** [`rakshacc/multiplication-table-app`](https://hub.docker.com/r/rakshacc/multiplication-table-app)
- **Image Tag:** `v1`

---

## 1. Verify Docker Installation

Check the installed Docker version:

```powershell
docker --version
```

Check whether the Docker engine is running:

```powershell
docker info
```

---

## 2. Build a Docker Image

Navigate to the directory containing the `Dockerfile` in VS Code.

```powershell
docker build -t multiplication-table-app .
```

**What it does:**
- Reads the instructions in the Dockerfile.
- Installs the required dependencies.
- Packages the application into a Docker image.

List available local images:

```powershell
docker images
```

---

## 3. Log In to Docker Hub

```powershell
docker login
```

Authenticates Docker with Docker Hub so that images can be uploaded to your account.

---

## 4. Tag the Docker Image

```powershell
docker tag multiplication-table-app:latest rakshacc/multiplication-table-app:v1
```

**What it does:**

Assigns a Docker Hub repository name and version tag to the local image.

**Image naming format:**

```text
username/repository-name:tag
```

Example:

```text
rakshacc/multiplication-table-app:v1
```

---

## 5. Push the Image to Docker Hub

```powershell
docker push rakshacc/multiplication-table-app:v1
```

**What it does:**

Uploads the image layers to Docker Hub, allowing the image to be retrieved from other machines.

View the repository:

[Docker Hub — multiplication-table-app](https://hub.docker.com/r/rakshacc/multiplication-table-app)

---

## 6. Pull an Image from Docker Hub

```powershell
docker pull rakshacc/multiplication-table-app:v1
```

**What it does:**

Downloads the specified image from Docker Hub into the local Docker image store.

Verify the downloaded image:

```powershell
docker images
```

If the image is already present and up to date, Docker may not need to download it again.

---

## 7. Run a Docker Container

```powershell
docker run -d --name multiplication-table -p 5000:5000 rakshacc/multiplication-table-app:v1
```

**Command breakdown:**

| Option | Purpose |
|---|---|
| `docker run` | Creates and starts a container |
| `-d` | Runs the container in the background |
| `--name` | Assigns a container name |
| `-p 5000:5000` | Maps host port 5000 to container port 5000 |

Open the application in your browser:

http://localhost:5000

---

## 8. Container Management Commands

### List running containers

```powershell
docker ps
```

### List all containers

```powershell
docker ps -a
```

### View container logs

```powershell
docker logs multiplication-table
```

### Stop a running container

```powershell
docker stop multiplication-table
```

### Start a stopped container

```powershell
docker start multiplication-table
```

### Remove a stopped container

```powershell
docker rm multiplication-table
```

### Remove a local image

```powershell
docker rmi multiplication-table-app:latest
```

Only remove an image when it is no longer needed and no remaining container depends on it.

---

## 9. Update and Publish a New Image Version

When the application code changes, build and publish a new version.

### Build the updated image

```powershell
docker build -t multiplication-table-app .
```

### Tag it as version 2

```powershell
docker tag multiplication-table-app:latest rakshacc/multiplication-table-app:v2
```

### Push version 2

```powershell
docker push rakshacc/multiplication-table-app:v2
```

### Pull version 2 on another machine

```powershell
docker pull rakshacc/multiplication-table-app:v2
```

Using version tags makes it easier to identify and deploy specific application versions.

---

## 10. Complete Docker Workflow

```text
Flask Application
       |
       v
Create Dockerfile
       |
       v
docker build
       |
       v
Local Docker Image
       |
       v
docker tag
       |
       v
docker push
       |
       v
Docker Hub
       |
       v
docker pull
       |
       v
docker run
       |
       v
Running Application
```

---

## 🎯 Key Concepts Learned

- Docker images and containers
- Dockerfiles and image building
- Image tagging and versioning
- Docker Hub authentication
- Pushing and pulling images
- Port mapping
- Container logs and lifecycle management

## 🚀 Next Steps in MLOps

- Deploy the Docker image to AWS EC2.
- Explore Amazon ECR for container image storage.
- Learn Kubernetes for container orchestration.
- Implement CI/CD pipelines for automated builds and deployments.
- Deploy machine learning models using containers.

---

**Author:** Raksha C C

**GitHub:** [Raksha-3063](https://github.com/Raksha-3063)

**MLOps Repository:** [Model_deployment_MLOPS](https://github.com/Raksha-3063/Model_deployment_MLOPS)
