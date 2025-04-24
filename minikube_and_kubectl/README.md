# Minikube & Kubernetes Setup Guide 🚀

This guide helps you set up and manage a local Kubernetes cluster using Minikube and `kubectl`. You'll deploy an Nginx web server and expose it as a service.

## 📌 Prerequisites
Ensure the following are installed on your system:
- **Minikube** (Runs Kubernetes locally)
- **kubectl** (Command-line tool to manage Kubernetes clusters)
- **Docker** (If using the Docker driver for Minikube)

## 📥 Installation
### 🔹 Install Minikube
#### **Windows (Using Chocolatey)**:
```powershell
choco install minikube -y
```
#### **Linux**:
```sh
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
#### **macOS (Using Homebrew)**:
```sh
brew install minikube
```

### 🔹 Install `kubectl`
#### **Windows (Using Chocolatey)**:
```powershell
choco install kubernetes-cli -y
```
#### **Linux/macOS**:
```sh
curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/darwin/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
```

## 🚀 Start Minikube
### **1️⃣ Start the Cluster**
```powershell
minikube start --driver=docker
```
- If you have virtualization enabled, you can also use:
```powershell
minikube start --driver=virtualbox
```

### **2️⃣ Verify Minikube is Running**
```powershell
minikube status
kubectl get nodes
```
Expected output:
```
NAME       STATUS   ROLES    AGE   VERSION
minikube   Ready    master   Xs    vX.Y.Z
```

## 🛠 Deploy an Application
### **3️⃣ Deploy an Nginx Web Server**
```powershell
kubectl create deployment nginx --image=nginx
```

### **4️⃣ Expose the Deployment as a Service**
```powershell
kubectl expose deployment nginx --type=NodePort --port=80
```

### **5️⃣ Get the Service URL**
```powershell
minikube service nginx --url
```
Example output:
```
http://127.0.0.1:XXXXX
```
Open the given URL in a browser to see the Nginx server.

## 📊 Managing Kubernetes Resources
### **6️⃣ View Running Pods**
```powershell
kubectl get pods
```

### **7️⃣ Scale the Deployment**
Increase the replicas to 3:
```powershell
kubectl scale deployment nginx --replicas=3
```
Verify the scaling:
```powershell
kubectl get pods
```

### **8️⃣ Delete Deployment & Service**
```powershell
kubectl delete service nginx
kubectl delete deployment nginx
```

## 🛠 Troubleshooting
### ❌ `minikube start` fails due to virtualization issues
- Ensure **VT-X/AMD-v** is enabled in BIOS
- Try running with Docker instead:
  ```powershell
  minikube start --driver=docker
  ```

### ❌ `kubectl get nodes` returns connection refused
- Start Minikube if it's not running:
  ```powershell
  minikube start
  ```

### ❌ Minikube service not accessible
- Run:
  ```powershell
  minikube tunnel
  ```
- Ensure ports are correctly mapped

## 🎯 Summary
✅ Installed Minikube & `kubectl`
✅ Created a local Kubernetes cluster
✅ Deployed and scaled an Nginx web server
✅ Managed Kubernetes resources

Minikube is a great way to test Kubernetes locally before moving to production! 🚀

---
**Happy Kubernetes-ing!** 😊

