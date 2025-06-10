# Sourcery and gcsfuse won't run on `arm` so force the use of `amd64` for the base image.
FROM --platform=linux/amd64 mcr.microsoft.com/devcontainers/python:1-3.12-bullseye AS base

# Install LaTeX (just for the presentation really).
RUN apt-get --quiet update \
 && apt-get install --assume-yes texlive-latex-extra texlive-extra-utils latexmk \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Add some labels so it looks nice in Github packages.
LABEL org.opencontainers.image.source=https://github.com/joejcollins/admiral-frendor
LABEL org.opencontainers.image.description="admiral-frendor image."
