Microservices Deployment on AWS EKS
This repository contains a sample Flask microservice deployed on AWS EKS using Terraform, Docker, Kubernetes, Helm, and GitHub Actions CI/CD. Additionally, Prometheus is deployed for cluster monitoring and exposed via a LoadBalancer.
Table of Contents
•	Overview
•	Architecture
•	Setup and Deployment Steps
•	Terraform Configuration
•	Kubernetes Manifests
•	Prometheus Deployment
•	GitHub Actions Workflow
•	Accessing the Services
________________________________________
Overview
This project demonstrates a fully automated deployment of a Python Flask microservice to a managed EKS cluster, with cluster monitoring using Prometheus. The workflow includes:
1.	Building a Docker image for the Flask app.
2.	Pushing the image to GitHub Container Registry (GHCR).
3.	Provisioning EKS resources using Terraform.
4.	Deploying the microservice to Kubernetes.
5.	Deploying Prometheus using Helm and exposing it via ELB.
6.	Exposing the Flask service via a LoadBalancer for public access.
________________________________________



Architecture
The deployment consists of the following components:
•	AWS EKS Cluster – Managed Kubernetes cluster for container orchestration.
•	Node Group – EC2 instances to run Kubernetes pods.
•	Terraform – Infrastructure as code tool to provision EKS, VPC, subnets, and IAM roles.
•	Docker – Containerization of the Flask microservice.
•	Kubernetes – Deployment and service manifests to run the application.
•	Helm – Package manager used to deploy Prometheus.
•	GitHub Actions – CI/CD pipeline to automate build, push, and deployment.
•	Prometheus – Monitoring and metrics collection for the cluster.
________________________________________

Setup and Deployment Steps:

1.Clone the repository:
git clone https://github.com/mostafasery/microservices.git
cd microservices


2.Build and push Docker image:
The Flask app is containerized and pushed to GitHub Container Registry:
docker build -t ghcr.io/mostafasery/microservices:latest .
docker push ghcr.io/ mostafasery /microservices:latest


3.Provision EKS Cluster using Terraform
Initialize Terraform and apply configuration:
  terraform init
  terraform apply -auto-approve

This creates:
•	VPC, Subnets, Security Groups
•	EKS Cluster
•	Node Group
•	IAM Roles for Kubernetes authentication
To destroy resources after testing:
  terraform destroy -auto-approve


4.Configure Kubernetes access
Update kubeconfig to connect to the EKS cluster:
aws eks --region us-east-1 update-kubeconfig --name my-eks-cluster

5.Apply Kubernetes manifests
Create namespace, deployment, and service:
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

6.Deploy Prometheus using Helm
Add the Helm repository and install Prometheus:
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus --namespace prometheus --create-namespace

7.Expose Prometheus via LoadBalancer
Update Prometheus service type to LoadBalancer to access it externally:
kubectl patch svc prometheus-server -n prometheus -p '{"spec": {"type": "LoadBalancer"}}'
kubectl get svc -n monitoring
Use the EXTERNAL-IP from the service to access Prometheus metrics in a browser.
Use port 9090

8.Verify deployments
Check pods and services:
kubectl get pods -n microservices
kubectl get svc -n microservices
kubectl get pods -n monitoring
kubectl get svc -n monitoring

9.Access the Flask app
The LoadBalancer service exposes the app on port 80. Use the EXTERNAL-IP from kubectl get svc to access it in a browser.
________________________________________
Terraform Configuration
The Terraform setup provisions:
•	AWS VPC, subnets, and security groups
•	EKS cluster and node group
•	IAM roles and Kubernetes RBAC
Key Terraform files:
•	main.tf – EKS cluster and node group
•	variables.tf – Input variables
•	outputs.tf – Cluster and node group info
________________________________________
Kubernetes Manifests
1.	Namespace – k8s/namespace.yaml
2.	Deployment – k8s/deployment.yaml
3.	Service – k8s/service.yaml
The deployment references the Docker image from GHCR and the service exposes port 80 to the public using ELB loadbalancer service type of AWS
________________________________________
Prometheus Deployment
Prometheus is deployed using Helm in the monitoring namespace and exposed with a ELB LoadBalancer to monitor cluster metrics.
Key commands:
helm install prometheus prometheus-community/prometheus --namespace monitoring --create-namespace
kubectl patch svc prometheus-server -n monitoring -p '{"spec": {"type": "LoadBalancer"}}'
________________________________________
GitHub Actions Workflow
The CI/CD pipeline automates:
1.	Docker image build and push to GHCR
2.	Terraform apply to provision infrastructure
3.	Kubernetes deployment for Flask microservice
Workflow file location: .github/workflows/deploy.yml
________________________________________
Accessing the Services

•	Flask App: Use the EXTERNAL-IP of the microservice LoadBalancer.
App URL: 
http://ad582a901404247848a0ec2f36afffbb-899759492.us-east-1.elb.amazonaws.com/products
http://ad582a901404247848a0ec2f36afffbb-899759492.us-east-1.elb.amazonaws.com/users

•	Prometheus: Use the EXTERNAL-IP of the Prometheus server LoadBalancer.
Prometheus URL:
http://a762ac00939084e46a12501d0ae1b6a0-1650531739.us-east-1.elb.amazonaws.com:9090/
