
# Building the Image

Docker uses the Dockerfile and the context of the directory you provide to build the image 

```
docker build -t webapp:latest .
```

# Run the Container


## Run with CMD

Docker run will execute our container and run the CMD specified in the Dockerfile. 

```
docker run --name webapp -p 5000 -d webapp
```

View running containers using 

```
docker ps
```

View the stdout from the command using

```
docker logs -f web
```

You can stop containers using stop or kill

```
docker kill web
```

## Overwrite the CMD

Overwrite the command by using providing your own command.

```
docker run -it web bash
```
