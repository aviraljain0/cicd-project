# 🚀 Automated CI/CD Pipeline with GitHub Actions

![CI/CD Pipeline](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue?logo=github-actions)
![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker)
![AWS EC2](https://img.shields.io/badge/Cloud-AWS%20EC2-FF9900?logo=amazon-aws)
![Python](https://img.shields.io/badge/Backend-Python%20Flask-3776AB?logo=python)
![Status](https://img.shields.io/badge/Status-Live-brightgreen)

> A fully automated CI/CD pipeline that builds, tests, and deploys a Dockerized Flask web application to AWS EC2 on every code push — with zero manual intervention.

---

## 📌 Project Overview

This project implements a complete **Continuous Integration and Continuous Deployment (CI/CD)** pipeline using industry-standard DevOps tools. Every time code is pushed to the `main` branch, GitHub Actions automatically:

1. Runs automated tests
2. Builds a Docker image
3. Pushes the image to Docker Hub
4. Deploys the updated app to AWS EC2
5. Performs a health check with auto-rollback on failure

**Live App:** `http://35.172.179.46:5000`

---

## 🏗️ Architecture

```
Developer pushes code
        ↓
   GitHub Repository
        ↓
   GitHub Actions (CI/CD)
   ┌────────────────────────────────────┐
   │  Job 1: Run Tests (pytest)         │
   │           ↓                        │
   │  Job 2: Build & Push Docker Image  │
   │           ↓                        │
   │  Job 3: Deploy to AWS EC2          │
   │    → Pull new image                │
   │    → Stop old container            │
   │    → Start new container           │
   │    → Health check + rollback       │
   └────────────────────────────────────┘
        ↓
   App Live on AWS EC2 🌍
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python Flask** | Web application framework |
| **Docker** | Containerization of the application |
| **Docker Hub** | Container image registry |
| **GitHub Actions** | CI/CD automation pipeline |
| **AWS EC2** | Cloud server for deployment |
| **AWS CloudWatch** | Monitoring and metrics |
| **pytest** | Automated testing |

---

## 📁 Project Structure

```
cicd-project/
│
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Actions CI/CD workflow
│
├── tests/
│   └── test_app.py           # Automated tests
│
├── app.py                    # Flask web application
├── Dockerfile                # Docker image instructions
├── requirements.txt          # Python dependencies
├── .dockerignore             # Files to exclude from Docker
├── .gitignore                # Files to exclude from Git
└── README.md                 # Project documentation
```

---

## ⚙️ CI/CD Pipeline — 3 Jobs

### Job 1: Run Tests
```yaml
- Checks out the code
- Sets up Python 3.11
- Installs dependencies
- Runs pytest test suite
```

### Job 2: Build & Push Docker Image
```yaml
- Builds Docker image from Dockerfile
- Logs into Docker Hub using secrets
- Pushes image tagged as 'latest'
```

### Job 3: Deploy to AWS EC2
```yaml
- SSHes into EC2 server
- Pulls latest Docker image
- Stops and removes old container
- Starts new container on port 5000
- Runs health check on /health endpoint
- Rolls back to previous version if health check fails
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Docker Desktop
- AWS Account (Free Tier)
- GitHub Account
- Docker Hub Account

### 1. Clone the repository
```bash
git clone https://github.com/aviraljain0/cicd-project.git
cd cicd-project
```

### 2. Create virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run locally
```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

### 5. Run tests
```bash
pytest tests/ -v
```

---

## 🐳 Docker

### Build image locally
```bash
docker build -t cicd-app .
```

### Run container locally
```bash
docker run -p 5000:5000 cicd-app
```

### Pull from Docker Hub
```bash
docker pull aviral8349/cicd-app:latest
```

---

## ☁️ AWS Setup

### EC2 Instance
| Setting | Value |
|---------|-------|
| OS | Ubuntu Server 22.04 LTS |
| Instance Type | t2.micro (Free Tier) |
| Storage | 20 GB gp3 |
| Open Ports | 22 (SSH), 80 (HTTP), 443 (HTTPS), 5000 (App) |

### CloudWatch Monitoring
- **Namespace:** `CICDProject`
- **Metrics tracked:** CPU usage, Memory usage, Disk usage
- **Log group:** `cicd-project-logs`

---

## 🔐 GitHub Secrets Required

Go to **GitHub repo → Settings → Secrets and variables → Actions** and add:

| Secret Name | Description |
|-------------|-------------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Your Docker Hub password |
| `EC2_HOST` | Your EC2 Public IPv4 address |
| `EC2_SSH_KEY` | Contents of your .pem private key file |

---

## 📸 Project Screenshots

### Step 1 — Flask App Setup
| Screenshot | Description |
|-----------|-------------|
| ![SS1](screenshots/ss1_vscode_app.png) | VS Code with app.py open |
| ![SS2](screenshots/ss2_localhost.png) | App running on localhost:5000 |
| ![SS3](screenshots/ss3_health.png) | Health endpoint returning JSON |

### Step 2 — Docker
| Screenshot | Description |
|-----------|-------------|
| ![SS4](screenshots/ss4_dockerfile.png) | Dockerfile in VS Code |
| ![SS5](screenshots/ss5_docker_build.png) | Docker build success |
| ![SS6](screenshots/ss6_docker_run.png) | App running via Docker |
| ![SS7](screenshots/ss7_docker_desktop.png) | Docker Desktop containers |

### Step 3 — AWS EC2
| Screenshot | Description |
|-----------|-------------|
| ![SS8](screenshots/ss8_ec2_running.png) | EC2 instance running on AWS |
| ![SS9](screenshots/ss9_ssh.png) | SSH connection to EC2 |
| ![SS10](screenshots/ss10_docker_ec2.png) | Docker installed on EC2 |
| ![SS11](screenshots/ss11_app_ec2.png) | App live on EC2 IP |

### Step 4 — GitHub Actions
| Screenshot | Description |
|-----------|-------------|
| ![SS12](screenshots/ss12_workflow.png) | deploy.yml workflow file |
| ![SS13](screenshots/ss13_pipeline_running.png) | Pipeline running in Actions tab |
| ![SS14](screenshots/ss14_all_green.png) | All 3 jobs green ✅✅✅ |
| ![SS15](screenshots/ss15_dockerhub.png) | Image pushed to Docker Hub |

### Step 5 — Auto Deploy
| Screenshot | Description |
|-----------|-------------|
| ![SS16](screenshots/ss16_commit_green.png) | Commit with green checkmark |
| ![SS17](screenshots/ss17_pipeline_success.png) | Full pipeline success with timings |
| ![SS18](screenshots/ss18_v2_live.png) | Version 2.0 live on EC2 |

### Step 6 — Monitoring & Rollback
| Screenshot | Description |
|-----------|-------------|
| ![SS19](screenshots/ss19_cloudwatch.png) | CloudWatch metrics dashboard |
| ![SS20](screenshots/ss20_rollback.png) | Rollback mechanism in workflow |

### Final Result
| Screenshot | Description |
|-----------|-------------|
| ![SS21](screenshots/ss21_github_repo.png) | GitHub repo with all project files |
| ![SS22](screenshots/ss22_final_app.png) | Final live app on AWS EC2 |

---

## 🔄 How Rollback Works

```
New code pushed
      ↓
Pipeline deploys new container
      ↓
Health check hits /health endpoint
      ↓
  ┌─────────────┐
  │ Check pass? │
  └─────────────┘
    ↓ YES              ↓ NO
Deployment         Stop new container
successful! ✅     Restart old container
                   Exit with error ❌
                   (pipeline marked failed)
```

---

## 📊 Pipeline Performance

| Job | Average Time |
|-----|-------------|
| Run Tests | ~10 seconds |
| Build & Push Docker Image | ~20 seconds |
| Deploy to AWS EC2 | ~16 seconds |
| **Total** | **~46 seconds** |

---

## 🎯 Key Learnings

- Setting up end-to-end CI/CD automation using GitHub Actions
- Containerizing Python applications with Docker
- Deploying and managing applications on AWS EC2
- Writing automated tests with pytest
- Implementing health checks and rollback mechanisms
- Monitoring cloud infrastructure with AWS CloudWatch
- Managing secrets securely in GitHub

---

## 👨‍💻 Author

**Aviral Jain**
- GitHub: [@aviraljain0](https://github.com/aviraljain0)
- Docker Hub: [aviral8349](https://hub.docker.com/u/aviral8349)
- Internship: IBM Innovation Center for Education — Cloud & DevOps Intern

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ as part of IBM Innovation Center for Education Summer Internship 2026*
