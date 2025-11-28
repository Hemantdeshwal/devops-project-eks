# DevOps Project – Flask on AWS EKS with Terraform & GitHub Actions

A production-style DevOps project that deploys a containerized Flask web application to an Amazon EKS cluster using Docker, Kubernetes, Terraform, Amazon ECR, and GitHub Actions CI/CD.[web:326][web:328]

## Architecture

- **Application**: Python Flask app with a simple creative UI and JSON API.[web:326]
- **Containerization**: Docker image built from `services/flask-app/Dockerfile`.
- **Orchestration**: Kubernetes manifests in `k8s/` (ConfigMap, Deployment, Services) deploy the app to a cluster.
- **Infrastructure as Code**: Terraform in `terraform/` provisions:
  - VPC + subnets
  - EKS cluster with managed node group
- **Image registry**: Amazon ECR stores versioned Docker images.
- **CI/CD**: GitHub Actions workflow builds and pushes images to ECR and deploys to EKS on every push to `master`.[web:267][web:272]

## Tech Stack

- **Languages**: Python (Flask)
- **Containers**: Docker
- **Kubernetes**: Amazon EKS
- **IaC**: Terraform (AWS provider + official EKS/VPC modules)[web:343]
- **CI/CD**: GitHub Actions
- **Cloud**: AWS (EKS, ECR, IAM, VPC)

## Repository Structure

.
├── services/
│ └── flask-app/
│ ├── app.py # Flask app
│ ├── Dockerfile # Image build
│ ├── requirements.txt
│ └── templates/
│ └── index.html # Frontend UI
├── k8s/
│ ├── configmap.yaml # App configuration
│ ├── deployment.yaml # Deployment + resources
│ ├── service.yaml # NodePort service
│ └── service-lb.yaml # LoadBalancer service for public access
├── terraform/
│ ├── main.tf # VPC + EKS cluster
│ ├── variables.tf
│ └── outputs.tf
└── .github/
└── workflows/
└── ci-cd.yml # Build → ECR → EKS pipeline

text

## How to Run Locally (Dev)

1. Build and run Docker:

cd services/flask-app
docker build -t flask-microservice:local .
docker run -p 3000:3000 flask-microservice:local

text

2. Open `http://localhost:3000` in your browser.

## How to Deploy to EKS (Infra + App)

1. **Provision EKS with Terraform**:

cd terraform
terraform init
terraform apply

text

2. **Configure `kubectl` for EKS**:

aws eks update-kubeconfig --region ap-south-1 --name devops-creative-eks
kubectl get nodes

text

3. **Deploy Kubernetes manifests**:

cd ../k8s
kubectl apply -f configmap.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f service-lb.yaml

text

4. **Get the public URL**:

kubectl get svc flask-app-lb

text

Open the `EXTERNAL-IP` (Load Balancer DNS) in your browser over HTTP.

## CI/CD with GitHub Actions

The workflow in `.github/workflows/ci-cd.yml`:

1. Runs on push to `master`.
2. Configures AWS credentials from GitHub Secrets.
3. Logs in to Amazon ECR.
4. Builds the Docker image from `services/flask-app/` and pushes it to ECR.
5. Updates the running EKS deployment image and waits for rollout success.[web:267][web:272]

Required repository secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_ACCOUNT_ID`
- `AWS_REGION`
- `ECR_REPOSITORY`
- `EKS_CLUSTER_NAME`

