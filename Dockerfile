FROM ubuntu:20.04

RUN apt-get update && apt-get install -yq --no-install-recommends \
	stressapptest && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /opt

