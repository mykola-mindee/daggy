#FROM tensorflow/tensorflow:2.8.2-gpu
FROM tensorflow/tensorflow@sha256:fffa0c1556a257afdac73137bb342e323346d75b5ba091b833151fb5d4b4bfb9 AS execute_locally

ARG USER_ID=1000
ARG GROUP_ID=1000
ARG USER=mindee
ARG GRANT_SUDO=1

ENV USER="${USER}" \
    USER_ID="${USER_ID}" \
    GROUP_ID="${GROUP_ID}" \
    GRANT_SUDO="${GRANT_SUDO}" \
    HOME="/home/${USER}" \
    FLIT_ROOT_INSTALL=1

# Install Docker in the Container
# Using the convenience script
RUN apt-get update && \
    apt-get install --yes curl && \
    curl -sSL https://get.docker.com/ | sh && \
    apt-get update && \
    apt-get install --yes \
    # - install some useful tools for development
    openssh-client git nano vim sudo curl wget iputils-ping \
    # - install libmagic-dev for magic package (common)
    libmagic-dev \
    # - dependencies for shapely
    libgeos-dev \
    # - install opencv dependencies
    libgl1-mesa-dev libsm6 libxext6 libxrender-dev && \
    # - clean docker container and add locales
    apt-get clean && rm -rf /var/lib/apt/lists/* && \
    # - Create mindee user with USER_ID=1000 and in the 'users' group
    # - and make sure these dirs are writable by the `users` group.
    sed -i.bak -e 's/^%admin/#%admin/' /etc/sudoers && \
    sed -i.bak -e 's/^%sudo/#%sudo/' /etc/sudoers && \
    useradd -l -m -s /bin/bash -N -u "${USER_ID}" "${USER}" && \
    chmod g+w /etc/passwd && \
    usermod -aG docker mindee && \
    pip3 install --upgrade pip flit

WORKDIR "${HOME}/work/"

COPY pyproject.toml pyproject.toml
COPY README.md README.md
COPY ./src ./src/

# Change pip index URL to codeartifact
RUN --mount=type=secret,id=CODEARTIFACT_URL,required=true pip config set global.index-url $(cat /run/secrets/CODEARTIFACT_URL) && \
    flit install --deps production && \
    rm -r pyproject.toml README.md src

COPY start.sh /usr/local/bin
CMD ["start.sh"]

ENV CLEARML_AGENT_SKIP_PIP_VENV_INSTALL="/usr/bin/python3" \
    CLEARML_AGENT_SKIP_PYTHON_ENV_INSTALL=1 \
    CLEARML_AGENT_LOCAL_PATH_TO_REPO="${HOME}/work/"


FROM execute_locally as execute_remotely

COPY . "${HOME}/work/"
