# Sourcery won't run on `arm` so force the use of `amd64` for the base image.
FROM --platform=linux/amd64 mcr.microsoft.com/devcontainers/python:1-3.13-bullseye AS base

# Install uv for everyone not just the current user.
RUN curl -LsSf https://astral.sh/uv/install.sh | sh \
 && cp /root/.local/bin/uv /usr/local/bin/uv

# Install Google Cloud utilities so we can use GCS.
RUN curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/cloud.google.asc \
 && echo "deb [signed-by=/usr/share/keyrings/cloud.google.asc] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
 && sudo apt-get update \
 && sudo apt-get install --assume-yes google-cloud-cli

# Fixed uv cache to improve the venv build time
RUN mkdir -p /opt/uv-cache
ENV UV_CACHE_DIR=/opt/uv-cache \
    UV_LINK_MODE=copy
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-install-project \
 && uv cache prune --ci
RUN chmod -R 777 /opt/uv-cache

# Add some labels so it looks nice in Github packages.
LABEL org.opencontainers.image.source=https://github.com/joejcollins/admiral-frendor
LABEL org.opencontainers.image.description="admiral-frendor image."
