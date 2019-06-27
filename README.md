# Think-Play-Hack: World Views

[Preparatory Readings](https://www.dropbox.com/sh/ru4dxh6rr6uqvfl/AADlPVWVEZ1BE4OcxPnZ0dpDa?dl=0)

# Software

We have ready-to-go software stacks for Python with Jupyter and R with RStudio.

## R with RStudio

### Windows

1. [Install Docker](https://download.docker.com/win/stable/Docker%20for%20Windows%20Installer.exe) Note: During the installation *don't* check the "Use Windows containers..." box.
2. Run Docker Desktop. (You may get a message about Hyper-V and Containers that will require a reboot, press "Ok" and wait for the reboot.)
2. `docker run --rm -p 127.0.0.1:8787:8787 -v ${HOME}:/home/rstudio -e DISABLE_AUTH=true thinkplayhack/r_rstudio:latest`
3. Go to `127.0.0.1:8787` in a web browser

### macOS

1. [Install Docker](https://download.docker.com/mac/stable/Docker.dmg)
2. `docker run --rm -p 127.0.0.1:8787:8787 -v ${HOME}:/home/rstudio -e DISABLE_AUTH=true thinkplayhack/r_rstudio:latest`
3. Go to `127.0.0.1:8787` in a web browser

### Linux

1. [Install Docker](https://docs.docker.com/install/) via distribution specifc instructions
2. `docker run --rm -p 127.0.0.1:8787:8787 -v ${HOME}:/home/rstudio -e DISABLE_AUTH=true thinkplayhack/r_rstudio:latest`
3. Go to `127.0.0.1:8787` in a web browser

### SMU ManeFrame II (M2)

1. Get M2 account credentials from Robert Kalescky.
2. [Login into M2 via operating system specific instructions](http://faculty.smu.edu/csc/documentation/access.html)

## Python with Jupyter

