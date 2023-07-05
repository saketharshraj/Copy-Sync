# Cloud-Sync Typing Tool Installation Guide

Follow the instructions below to download and install the Cloud-Sync Typing Tool on your Linux system.

## Prerequisites

- You should have `sudo` access on your system to move the binary to `/usr/local/bin`.

## Installation Steps

Open your terminal and execute the following commands:

```bash
# Download the binary using wget
wget https://github.com/saketharshraj/Copy-Sync/releases/download/MAJOR/copy_sync

# Make the downloaded file executable
chmod +x copy_sync

# Move it to /usr/local/bin or another directory on the PATH
sudo mv copy_sync /usr/local/bin/
