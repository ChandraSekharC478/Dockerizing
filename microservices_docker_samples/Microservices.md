# Dockerizing Microservices Samples

This repository contains Dockerfiles and configurations to **dockerize** various **microservices applications** built using different tech stacks. It demonstrates the **best practices** for creating **multi-stage Dockerfiles**, optimizing builds for production environments, and providing clear guidance for running these services in Docker containers.

---

## 🧑‍💻 Tech Stacks Covered

1. **Node.js (JavaScript/TypeScript)**
2. **Python (Flask/Django)**
3. **Java (Spring Boot with Maven)**
4. **.NET Core (ASP.NET)**

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:

* [Docker](https://www.docker.com/products/docker-desktop)
* A terminal or command prompt

---

### 🚦 Run Microservices

Each folder contains a **Dockerfile** to build and run the corresponding app.

To build and run any microservice:

1. Navigate to the directory containing the Dockerfile.

   ```bash
   cd /path/to/your-app-directory
   ```

2. Build the Docker image:

   ```bash
   docker build -t <your-image-name> .
   ```

3. Run the Docker container:

   ```bash
   docker run -p <host-port>:<container-port> <your-image-name>
   ```

---

## 📝 Dockerfiles

### **1. Node.js Application (JavaScript/TypeScript)**

```dockerfile
# Stage 1: Build
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build  # optional for React/Vue/TS projects

# Stage 2: Run
FROM node:18-alpine
WORKDIR /app
COPY --from=build /app ./
RUN addgroup app && adduser -S -G app app
USER app
EXPOSE 3000
CMD ["node", "app.js"]
```

---

### **2. Python Application (Flask/Django)**

```dockerfile
# Stage 1: Build
FROM python:3.10-slim as build
WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# Stage 2: Run
FROM python:3.10-slim
WORKDIR /app
COPY --from=build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

### **3. Java Application (Spring Boot with Maven)**

```dockerfile
# Stage 1: Build
FROM maven:3.8.6-openjdk-17 AS build
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline
COPY . .
RUN mvn clean package -DskipTests

# Stage 2: Run
FROM openjdk:17-jdk-slim
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "app.jar"]
```

---

### **4. .NET Core Application (ASP.NET)**

```dockerfile
# Stage 1: Build
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
WORKDIR /src
COPY . .
RUN dotnet restore
RUN dotnet publish -c Release -o /app/publish

# Stage 2: Run
FROM mcr.microsoft.com/dotnet/aspnet:6.0
WORKDIR /app
COPY --from=build /app/publish .
EXPOSE 5000
ENTRYPOINT ["dotnet", "MyApp.dll"]
```

---

## 🔒 Best Practices

* **Multi-stage builds**: Optimizes the image size by excluding build dependencies and using minimal runtime images.
* **Use of `--from=build`**: This ensures that only the required files are copied into the final image, keeping it lightweight.
* **Dockerignore**: Ensures unnecessary files (e.g., `node_modules`, `.git`) aren’t included in the Docker context, improving build speed.

---

## 🚧 Future Improvements

* Integrate **Docker Compose** to manage multi-container applications and dependencies (e.g., linking a Node.js app with a database).
* Add CI/CD pipelines for automated building and deployment.

---



## 💬 Contributing

Feel free to open an issue or create a pull request if you have any improvements or suggestions!

---
