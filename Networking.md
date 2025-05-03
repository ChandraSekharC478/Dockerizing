# Docker Networking – Complete Guide with Demos by Chandrasekhar

## 🧩 What Problem Does Docker Networking Solve?

Containers are designed to be isolated. While this is great for security and resource separation, it becomes an issue when containers need to talk to each other—for example, a frontend container communicating with a backend or database. Docker networking solves this by enabling:

* **Inter-container communication** (e.g., frontend ↔ backend)
* **Access to the host system** (e.g., accessing local files or ports)
* **Cluster-wide communication** across multiple machines (using Swarm/Overlay)

Docker provides several networking modes—**bridge, custom bridge, host, overlay, and macvlan**—to enable different communication scenarios while maintaining control and security.

---

## 📘 Overview

Docker networking enables containers to communicate with each other, with the host, and with external systems. In this guide, we’ll cover Docker’s key network types with clear demos and diagrams.

---

## 🌉 Bridge Networking (Default)

This is Docker's default network mode. It connects containers to an internal virtual bridge called `docker0`, allowing communication among containers and between containers and the host.

```bash
docker network ls
```

```
NETWORK ID     NAME      DRIVER
xxxxxxxxxxxx   bridge    bridge
xxxxxxxxxxxx   host      host
xxxxxxxxxxxx   none      null
```

### 🧪 Demo 1: Default Bridge

1. Create two containers:

   ```bash
   docker run -it --name login ubuntu:latest
   docker run -it --name logout ubuntu:latest
   ```
2. Inside `login`, install ping:

   ```bash
   apt-get update && apt-get install iputils-ping -y
   ```
3. Ping `logout` by name:

   ```bash
   ping logout
   ```

✅ **Result**: Communication is successful because both containers are on the default bridge.

---

## 🔒 Custom Bridge Network

You can isolate containers by placing them in a separate user-defined bridge network.

### Creating a Custom Bridge:

```bash
docker network create -d bridge my_bridge
```

Now run containers in this custom network:

```bash
docker run -d --net=my_bridge --name db training/postgres
```

### 🧪 Demo 2: Isolated Network

1. Create a network:

   ```bash
   docker network create secure-network
   ```
2. Launch a container in that network:

   ```bash
   docker run -d --name finance --network=secure-network nginx:latest
   ```
3. Check network and container IPs:

   ```bash
   docker inspect login
   docker inspect logout
   docker inspect secure-network
   ```
4. Try pinging between containers from different networks (will fail).

✅ **Result**: Containers on different bridge networks cannot talk until explicitly connected.

🔧 **Fix**:

```bash
docker network connect secure-network login
```

📊 **Diagram**:
![Custom Bridge](https://user-images.githubusercontent.com/43399466/217748680-8beefd0a-8181-4752-a098-a905ebed5d2a.png)

---

## 🏠 Host Networking

This mode lets containers share the host’s network stack. The container does **not** get its own IP—services inside are accessible via the host’s IP.

### 🧪 Demo 3: Host Network

```bash
docker run -d --name host-demo --network=host nginx:latest
```

```bash
docker inspect host-demo
```

✅ **Result**: No IP address is assigned to the container. It uses the host’s network.

📌 Example: If host IP is `192.168.1.100`, NGINX is reachable at `http://192.168.1.100:80`

⚠️ **Note**: Host network reduces isolation, so use cautiously.

---

## 🌐 Overlay Networking

Used in Docker Swarm for multi-host communication. Containers running on different machines can connect as if they were on the same network.

✅ Great for scalable microservices across clusters.

---

## 🧭 Macvlan Networking

This allows containers to appear as separate physical devices on the network. They get their own MAC and IP from the LAN.

✅ Ideal when containers need to be accessed directly on the physical network.

---

## ✅ Summary Table

| Network Type     | Isolation | Communication Scope         | IP Assignment   | Use Case                         |
| ---------------- | --------- | --------------------------- | --------------- | -------------------------------- |
| Bridge (default) | Medium    | Same host (default bridge)  | Docker-assigned | General use, safe default        |
| Custom Bridge    | Strong    | Same host (user-defined)    | Custom-assigned | Isolated networking scenarios    |
| Host             | Low       | Shares host’s stack         | Host's IP       | Max performance, less isolation  |
| Overlay          | Medium    | Multi-host (Swarm)          | Virtual IP      | Cluster-wide communication       |
| Macvlan          | Low       | LAN (acts like a real host) | LAN-assigned IP | Expose container directly to LAN |

---

Happy learning and teaching! 🚀
