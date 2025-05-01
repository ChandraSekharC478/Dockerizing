# 🚀 GoLang Docker Build – Multi-Stage vs Normal

This project showcases two different approaches to containerizing a GoLang application using Docker:
1. **Multi-Stage Build**
2. **Normal (Single-Stage) Build**

The goal is to demonstrate how multi-stage builds can drastically reduce image size by excluding unnecessary build-time dependencies.

---

## 🐳 Dockerfile: Multi-Stage Build

```dockerfile
# BASE IMAGE
FROM ubuntu AS build

RUN apt-get update && apt-get install -y golang-go

ENV GO111MODULE=off

COPY . .

RUN CGO_ENABLED=0 go build -o /app .

# FINAL IMAGE
FROM scratch

COPY --from=build /app /app

ENTRYPOINT [ "/app" ]
```

📦 **Built Image**: `chandhra005/goloangappmultistagebuild:latest`  
📉 **Image Size**: `3.18MB`

---

## 🐘 Dockerfile: Normal Build

```dockerfile
# BASE IMAGE
FROM ubuntu AS build

RUN apt-get update && apt-get install -y golang-go

ENV GO111MODULE=off

COPY . .

RUN CGO_ENABLED=0 go build -o /app .

ENTRYPOINT [ "/app" ]
```

📦 **Built Image**: `chandhra005/goloangapp:latest`  
📈 **Image Size**: `942MB`

---

## 🔧 Build Instructions

### Multi-Stage Build
```bash
docker build -t chandhra005/goloangappmultistagebuild -f Dockerfile.multi .
```

### Normal Build
```bash
docker build -t chandhra005/goloangapp -f Dockerfile.normal .
```

---

## ▶️ Run the Application

```bash
docker run --rm chandhra005/goloangappmultistagebuild
```

---

## 📝 Key Takeaway

| Build Type      | Image Size |
|-----------------|------------|
| Multi-Stage     | 3.18 MB    |
| Normal          | 942 MB     |

✅ The **multi-stage build** reduces the image size by over **99%**, creating a minimal, production-ready image.

This technique is especially useful for:
- Deployments to cloud platforms
- Reducing CI/CD pipeline time
- Enhancing security by removing unnecessary layers

---

## 📚 References

- [Docker Multi-Stage Builds Docs](https://docs.docker.com/develop/develop-images/multistage-build/)
- [GoLang Docker Best Practices](https://golangdocs.com/golang-docker)

---

## 🙌 Author

**Chandrasekhar**  
[LinkedIn](https://www.linkedin.com/in/your-profile) | [DockerHub](https://hub.docker.com/u/chandhra005)