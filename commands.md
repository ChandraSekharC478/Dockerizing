
## 🐳 Commonly Used Docker Commands

### 1. **Check Docker version**

```bash
docker --version
```

✅ *Example Output:*
`Docker version 24.0.2, build cb74dfc`

---

### 2. **Pull an image from Docker Hub**

```bash
docker pull nginx
```

✅ *Example:*
Downloads the latest official NGINX image.

---

### 3. **Run a container**

```bash
docker run -d --name web-server -p 8080:80 nginx
```

✅ *Example:*
Runs an NGINX container in detached mode, mapping port 8080 on host to port 80 in container.

---

### 4. **List running containers**

```bash
docker ps
```

✅ *Example Output:*
Shows container ID, image name, ports, and status.

---

### 5. **List all containers (including stopped ones)**

```bash
docker ps -a
```

---

### 6. **Stop a running container**

```bash
docker stop web-server
```

---

### 7. **Remove a container**

```bash
docker rm web-server
```

---

### 8. **Remove an image**

```bash
docker rmi nginx
```

---

### 9. **List Docker images**

```bash
docker images
```

---

### 10. **View logs of a container**

```bash
docker logs web-server
```

---

### 11. **Execute a command in a running container**

```bash
docker exec -it web-server bash
```

✅ *Example:*
Opens an interactive shell inside the running container.

---

### 12. **Inspect details of a container or network**

```bash
docker inspect web-server
```

---

### 13. **Build an image from Dockerfile**

```bash
docker build -t my-app .
```

---

### 14. **Create a Docker network**

```bash
docker network create my-network
```

---

### 15. **Connect a container to a network**

```bash
docker network connect my-network web-server
```

---
**Happy Learning!🚀**
