# Running python code in Docker container

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/adamfordyce11/python-container)

## Setup

1. Install Python version > 3.9 and create a virtual environment.
2. Install Docker or a similar container runtime.

## Build the container

```bash
docker build . -t test
```

## Test the container can be started and the script runs

```bash
docker run -it test:latest /bin/bash
# src/print_script.py
Value: 10
# exit
```

## Run the container for a longer period

```bash
container_id=$(docker run -it --rm --detach test:latest sleep 1000)
```

This will run the container for 1000 seconds allowing for further testing with Docker, i.e.:

```bash
docker exec $container_id pytest tests/test_print_script.py
docker exec $container_id src/print_script.py
docker logs $container_id
```

After testing the container can be stopped using the following:

```bash
docker stop $container_id
```

## Deactivate the Virtual Environment

After finishing testing this container, deactivate the virtual environment

```bash
deactivate
```
