
# Building the Image

Docker uses the Dockerfile and the context of the directory you provide to build the image 

```
docker build -t docker-crash-course:latest .
```

# Run the Container


## Run with CMD

Docker run will execute our container and run the CMD specified in the Dockerfile. 

```
docker run --name docker-crash-course -d docker-crash-course:latest
```

View running containers using 

```
docker ps
```

View the stdout from the command using

```
docker logs -f docker-crash-course
```

You can stop containers using stop or kill

```
docker kill docker-crash-course
```

## Overwrite the CMD

Overwrite the command by using providing your own command. Note the ENTRYPOINT will still run unless overwritten with --entrypoint. 

```
docker run -it docker-crash-course:latest bash
```
