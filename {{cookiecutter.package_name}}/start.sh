#!/bin/bash
# Inspired from
# https://github.com/jupyter/docker-stacks/blob/25f9aa078919bce5aad3f01da36f2268f441fb77/base-notebook/start.sh
# Copyright (c) Jupyter Development Team.
# Copyright (c) Mindee.
# Distributed under the terms of the Modified BSD License.

set -e

# The _log function is used for everything this script wants to log. It will
# always log errors and warnings, but can be silenced for other messages
# by setting VERBOSE environment variable.
_log () {
    if [[ "$*" == "ERROR:"* ]] || [[ "$*" == "WARNING:"* ]] || [[ "${VERBOSE}" == "" ]]; then
        echo "$@"
    fi
}
_log "Entered start.sh with args:" "$@"


# Default to starting bash if no command was specified
if [ $# -eq 0 ]; then
    cmd=( "bash" )
else
    cmd=( "$@" )
fi

# If the container started as the root user, then we have permission to refit
# the jovyan user, and ensure file permissions, grant sudo rights, and such
# things before we run the command passed to start.sh as the desired user
# (USER).
#
if [ "$(id -u)" == 0 ] ; then
    # Environment variables:
    # - USER: the desired username and associated home folder
    # - USER_ID: the desired user id
    # - GROUP_ID: a group id we want our user to belong to
    # - GRANT_SUDO: a boolean ("1" or "yes") to grant the user sudo rights

    # Ensure the desired user (USER) gets its desired user id (USER_ID) and its desired group (GROUP_ID)
    if [ "${USER_ID}" != "$(id -u "${USER}")" ] || [ "${GROUP_ID}" != "$(id -g "${USER}")" ]; then
        _log "Update ${USER}'s UID:GID to ${USER_ID}:${GROUP_ID}"
        # Ensure the desired group's existence
        if [ "${GROUP_ID}" != "$(id -g "${USER}")" ]; then
            groupadd --force --gid "${GROUP_ID}" --non-unique "${NB_GROUP:-${USER}}"
        fi
        # Recreate the desired user as we want it
        userdel "${USER}"
        useradd --home "/home/${USER}" --uid "${USER_ID}" --gid "${GROUP_ID}" --groups 100 --no-log-init "${USER}"
    fi

    if [ -S "/var/run/docker.sock" ]; then
        # Change permission on docker socket to be able to build docker image
        chown "${USER_ID}" /var/run/docker.sock
    fi

    # Optionally ensure the desired user get filesystem ownership of it's home
    # folder and/or additional folders
    _log "Ensuring /home/${USER} is owned by ${USER_ID}:${GROUP_ID}"
    chown "${USER_ID}:${GROUP_ID}" "/home/${USER}"

    # Optionally grant passwordless sudo rights for the desired user
    if [[ "$GRANT_SUDO" == "1" || "$GRANT_SUDO" == "yes" ]]; then
        _log "Granting ${USER} passwordless sudo rights!"
        echo "${USER} ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers.d/added-by-start-script
    fi

    exec sudo --preserve-env --set-home --user "${USER}" \
        PATH="${PATH}" \
        PYTHONPATH="${PYTHONPATH:-}" \
        "${cmd[@]}"

# The container didn't start as the root user, so we will have to act as the
# user we started as.
else
    _log "WARNING: container must be started as root to fix users permissions!"
fi
