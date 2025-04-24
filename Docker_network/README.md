# Docker Networking Experiment 🐳🌐

## Overview
Docker Networking allows containers to communicate with each other efficiently. This experiment demonstrates how to create and manage Docker networks, connect containers, and test connectivity between them.

## Prerequisites ✅
Before starting, ensure you have:
- Docker installed ([Download Docker](https://docs.docker.com/get-docker/))
- Basic knowledge of Docker commands

## Step 1: Verify Docker Installation 🛠️
Check if Docker is installed by running:
```sh
docker --version
```
Example Output:
```
Docker version 20.10.17, build 100c701
```

## Step 2: List Existing Docker Networks 🔍
View existing networks:
```sh
docker network ls
```

## Step 3: Create a Custom Docker Network 🌉
```sh
docker network create --driver bridge net-bridge
```
This creates a bridge network named `net-bridge`.

## Step 4: Run Containers on the Custom Network 🏗️
Launch two containers on `net-bridge`:
```sh
docker run -itd --net=net-bridge --name=server-A busybox
```
```sh
docker run -itd --net=net-bridge --name=server-B busybox
```

## Step 5: Retrieve Container IP Addresses 📡
Get `server-A`'s IP:
```sh
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server-A
```
Get `server-B`'s IP:
```sh
docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' server-B
```

## Step 6: Install Ping Utility in Containers ⚙️
By default, BusyBox containers may not have `ping`. Install it:
```sh
docker exec -it server-A sh
```
Inside the container, run:
```sh
apk add --no-cache iputils
exit
```
Repeat for `server-B` if needed.

## Step 7: Test Connectivity Between Containers 🚀
Ping `server-B` from `server-A`:
```sh
docker exec -it server-A ping <server-B-IP>
```
Replace `<server-B-IP>` with the actual IP address from **Step 5**.

Expected output:
```
64 bytes from 192.168.x.x: icmp_seq=1 ttl=64 time=0.064 ms
```

## Step 8: Disconnect and Remove Network ❌
To disconnect a container from a network:
```sh
docker network disconnect net-bridge server-A
```
To remove the network:
```sh
docker network rm net-bridge
```

## Conclusion 🎉
You have successfully created and managed a Docker network, launched containers, retrieved IP addresses, and tested communication between them.

Happy Networking! 🌐🚀