# UltraBoost Dashboard Installation
This repository is maintained by BoostNova as a companion for users of [UltraBoost](https://github.com/MohamedMagdy90/UltraGrid), the open source framework for building high-frequency crypto trading bots.
## Requirements
Cloud Server or local machine
* Minimum of at least 2vCPU and 8 GB memory or more (On AWS, this is a `t2.large` instance)
* Linux / MacOS / Windows*
* For Windows users, make sure to install WSL2 as well as a Linux distro like Ubuntu and run the commands listed below in a Linux terminal and **NOT** in the Windows Command prompt or Powershell.
## Installation
### Method 1 - Docker (Recommended)
This is the **recommended** install procedure for normal users
1 - Install dependencies:
* [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
2 - Clone repo and navigate to the created directory
```bash
git clone https://github.com/MohamedMagdy90/ultraboost-dashboard.git
cd ultraboost-dashboard
```
3 - Run with Docker Compose
```bash
docker-compose up -d
```
Proceed to the **Launch Dashboard** section
### Method 2 - Source
This method is only recommended if you are a developer and want to make changes to the code.
1 - Install dependencies:
* [Docker Engine](https://docs.docker.com/engine/install/ubuntu/)
* [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://www.anaconda.com/):
2 - Clone repo and navigate to the created directory
```bash
git clone https://github.com/MohamedMagdy90/ultraboost-dashboard.git
cd ultraboost-dashboard
```
3 - Create `conda` environment and install dependencies
```bash
make install
```
4 - Activate the isolated 'conda' environment
```bash
conda activate ultraboost-dashboard
```
5 - Start the dashboard
```bash
make run
```
Don't forget to run the UltraBoost Backend API separately for this to work.
Proceed to the **Launch Dashboard** section
## Launch the Dashboard
Open a web browser and navigate to <https://localhost:8501> to view the Dashboard.
If you are using a cloud server or VPS, replace localhost with the IP of your server. You may need to edit the firewall rules to allow inbound connections to the necessary ports.
## Updating
Before updating, make sure to stop any running instances first
### Docker
To update - make sure you are in the `ultraboost-dashboard` folder then run:
```bash
docker-compose pull
docker-compose up -d
```
This will pull any latest images and recreate the Docker containers.
### Source
To update the `ultraboost-dashboard` source for latest version, run:
```bash
cd ultraboost-dashboard
git pull
```
Once updated, start up the dashboard again:
```bash
make run
```
To update the environment, run:
```bash
make uninstall
make install
```
This will remove the `conda` environment and recreate it.
## Troubleshooting
For Dashboard issues, please open a ticket on our [Github page](https://github.com/MohamedMagdy90/ultraboost-dashboard)
### Docker permissions
If you get an error like `Permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock`, run this command to enable Docker permissions:
```bash
sudo chmod 666 /var/run/docker.sock
```
---
**UltraBoost Dashboard** - Built with BoostNova