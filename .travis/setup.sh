#!/usr/bin/env bash

# Python requirements
pip install requests

# Install libraries needed for blender
sudo apt-get update
sudo apt-get install -y --no-install-recommends \
    curl \
    bzip2 \
    libfreetype6 \
    libgl1-mesa-dev \
    libglu1-mesa \
    libxrender1 \
    libxi6 \
    ca-certificates \
    unzip
sudo apt-get -y autoremove
sudo rm -rf /var/lib/apt/lists/*

# Download blender
sudo mkdir -p /usr/local/blender
sudo chmod -R 0777 /usr/local/blender

curl -SL "http://download.blender.org/release/Blender$BLENDER_MAJOR/blender-$BLENDER_VERSION-linux-glibc219-x86_64.tar.bz2" -o blender.tar.bz2
tar -jxvf blender.tar.bz2 -C /usr/local/blender --strip-components=1

rm blender.tar.bz2
