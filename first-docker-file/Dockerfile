
# Use the latest Ubuntu image
FROM ubuntu:latest 

# Set the working directory in the container to /app
WORKDIR /app

# copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt

RUN apt-get update && apt-get install -y python3 python3-pip

# cmd
CMD ["python3","app.py"]


