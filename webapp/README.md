

# Docker Instructions

## Building the Image

Docker uses the Dockerfile and the context of the directory you provide to build the image 

```
docker build -t webapp:latest .
```

# Run the Container

Docker run will execute our container and run the CMD specified in the Dockerfile. 

```
docker run --rm -it --name webapp -p 5000:5000 -d webapp
```

View running containers using 

```
docker ps
```

View the stdout from the command using

```
docker logs -f webapp
```

You can stop containers using stop or kill

```
docker stop webapp
```

# Docker-compose Instructions

## Building the Image

Docker uses the Dockerfile and the context of the directory you provide to build the image 

```
Docker-compose build
```

# Run the Container

This will run the containers for all services in the docker-compose file

```
docker-compose up
```


