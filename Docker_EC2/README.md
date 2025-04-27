# 📌 Overview

This guide provides a step-by-step approach to deploying a Streamlit app inside a Docker container on an AWS EC2 instance with a custom network setup. It covers:

✅ Setting up a VPC, Subnet, Route Table, and Internet Gateway  
✅ Launching and configuring an EC2 instance  
✅ Installing and configuring Docker  
✅ Transferring project files to EC2  
✅ Running the Streamlit app inside a Docker container  
✅ Managing the Docker container  

---

## 📖 Table of Contents

1️⃣ [Setting Up a VPC, Subnet, Route Table, and Internet Gateway](#1-setting-up-a-vpc-subnet-route-table-and-internet-gateway)  
2️⃣ [Launching and Configuring an EC2 Instance](#2-launching-and-configuring-an-ec2-instance)  
3️⃣ [Connecting to EC2](#3-connecting-to-ec2)  
4️⃣ [Setting Permissions for the PEM Key](#4-setting-permissions-for-the-pem-key)  
5️⃣ [Installing and Configuring Docker](#5-installing-and-configuring-docker)  
6️⃣ [Copying Project Files to EC2](#6-copying-project-files-to-ec2)  
7️⃣ [Building and Running the Docker Container](#7-building-and-running-the-docker-container)  
8️⃣ [Accessing the Streamlit App](#8-accessing-the-streamlit-app)  
9️⃣ [Managing the Docker Container](#9-managing-the-docker-container)  

---

## 1️⃣ Setting Up a VPC, Subnet, Route Table, and Internet Gateway

### 🔹 Create a New VPC

- Go to **AWS Console → VPC Dashboard → Create VPC**
  - **Name**: `MyCustomVPC`
  - **IPv4 CIDR block**: `10.0.0.0/16`

### 🔹 Create a Subnet

- Go to **VPC Dashboard → Subnets → Create Subnet**
  - **Select**: `MyCustomVPC`
  - **Subnet name**: `MyPublicSubnet`
  - **CIDR block**: `10.0.1.0/24`
  - Enable **Auto-assign Public IPv4**

### 🔹 Create an Internet Gateway and Attach to VPC

- **Name**: `MyIGW`
- **Attach it to**: `MyCustomVPC`

### 🔹 Create and Associate a Route Table

- **Name**: `MyPublicRouteTable`
- **Destination**: `0.0.0.0/0`
- **Target**: `MyIGW`
- **Associate with**: `MyPublicSubnet`

---

## 2️⃣ Launching and Configuring an EC2 Instance

### 🔹 Launch an EC2 Instance

- **Name**: `Streamlit-EC2`  
- **AMI**: Amazon Linux 2023  
- **Instance Type**: `t2.micro` (Free Tier)  
- **Key Pair**: Select/Create a key pair  
- **Network**: `MyCustomVPC`  
- **Subnet**: `MyPublicSubnet`  
- **Auto-assign Public IP**: Enabled  
- **Security Group**: Allow  
  - SSH (22)  
  - HTTP (80)  
  - Streamlit (8501)  

---

## 3️⃣ Connecting to EC2

### 🔹 Via EC2 Instance Connect

- Go to **EC2 Dashboard → Select Instance → Connect**
- Choose **EC2 Instance Connect**
- Click **Connect**

---

## 4️⃣ Setting Permissions for the PEM Key

```bash
mv /path/to/your-key.pem ~/your-work-directory/
chmod 600 your-key.pem
