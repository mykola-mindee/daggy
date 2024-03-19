#!/bin/bash

# exit when any command fails
set -e

# Test exp-manager is installed
if ! [ -x "$(command -v exp-manager)" ]; then
    echo 'Error: exp-manager is not installed. Please install it using:' >&2
    echo 'pip install mindee-exp-manager' >&2
    exit 1
else
    exp-manager build
fi

# keep track of the last executed command
trap 'last_command=$current_command; current_command=$BASH_COMMAND' DEBUG
# echo an error message before exiting
trap 'echo "\"${last_command}\" command filed with exit code $?."' EXIT


CLEARML_CONF=$HOME/clearml.conf

if [[ -f "$CLEARML_CONF" ]]; then
    echo "$CLEARML_CONF exists."
    echo "Mount file in container"
    MOUNT_CLEARML_CONF="--mount type=bind,source=$CLEARML_CONF,target=/home/mindee/clearml.conf"
fi


USER_ID=$(id -u)
GROUP_ID=$(id -g)

sudo docker run -it \
    --gpus all \
    -v $(pwd):/home/mindee/work/ `# Mount current directory in container` \
    -v /tmp/:/tmp/ \
    -v ~/.Xauthority:/home/mindee/.Xauthority \
    `# Mount docker socket to be able to build a docker image inside` \
    -v /var/run/docker.sock:/var/run/docker.sock \
    `# Mount Datasets folder` \
    -v /mnt/team_data:/mnt/team_data:ro \
    $MOUNT_CLEARML_CONF \
    -e DISPLAY=$DISPLAY \
    -e QT_X11_NO_MITSHM=1 \
    `# Set same container IP than host. Useful if you launch Docker through ssh -X` \
    --net=host \
    `# Map host user to docker user. See start.sh script` \
    -e USER_ID=$(id -u) \
    -e GROUP_ID=$(id -g) \
    --name {{cookiecutter.project_name}} \
    --rm \
    {{cookiecutter.project_name}}:execute_locally \
    "start.sh" "$@"
