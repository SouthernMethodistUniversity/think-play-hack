# Docker Setup for Personal Machines

## Initial Setup

### Windows

1. [Install Docker](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) Note: During the installation *don't* check the "Use Windows containers..." box.
2. Run Docker Desktop. (You may get a message about Hyper-V and Containers that will require a reboot, press "Ok" and wait through several reboots.)
3. Run Windows PowerShell and the application instructions below. (You may get a message about sharing your C:\ drive with Docker, accept.)

### macOS

1. [Install Docker](https://download.docker.com/mac/stable/Docker.dmg).
2. Run Terminal (/Applications/Utilities/Terminal) and the application instructions below.

### Linux

1. [Install Docker](https://docs.docker.com/install/) via distribution specifc instructions.
2. Run Terminal and the application instructions below.

## R with RStudio

### Windows

1. In Windows PowerShell run: `docker run --rm -p 127.0.0.1:8787:8787 -v ${HOME}:/home/rstudio -e DISABLE_AUTH=true thinkplayhack/r_rstudio:latest` .
2. Go to [127.0.0.1:8787](http://127.0.0.1:8787) in a web browser.

### macOS & Linux

1. In Terminal run: `docker run --rm -p 127.0.0.1:8787:8787 -v ${HOME}:/home/rstudio -e DISABLE_AUTH=true thinkplayhack/r_rstudio:latest`.
2. Go to [127.0.0.1:8787](http://127.0.0.1:8787) in a web browser.

## Python with Jupyter

### Windows

1. In Windows PowerShell run: `docker run --rm -p 127.0.0.1:8888:8888 -v ${HOME}:/home/jovyan thinkplayhack/python_jupyter:latest`.
2. Go to [127.0.0.1:8888](http://127.0.0.1:8888) in a web browser.

### macOS & Linux

1. In Terminal run: `docker run --rm -p 127.0.0.1:8888:8888 -v ${HOME}:/home/jovyan thinkplayhack/python_jupyter:latest`.
2. Go to [127.0.0.1:8888](http://127.0.0.1:8888) in a web browser.

