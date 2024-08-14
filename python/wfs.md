# Windows File System



Windows File System (WFS) is a feature of windows that allows users to run a linux environment on Windows machine without need to have a virtual machine or dual booting.

Important features:

- run different linux distributions
- command line tool such as bash

WSL2 is the default distro that runs as isolated containers inside the WSL2 managed virtual machine and share same network namespace, device tree (/dev/pts) CPU/Kernel/memory/etc. but have its own PID namspace, mount/user/cgroup namespace.



## **Basic commands**

Install WSL

```bash
wsl --install
```

List distributions online

```bash
wsl --list --online
```

Shutdown

```bash
wsl --shutdown
```

Terminate distribution

```bash
wsl --terminate <Distribution Name>
```



Setting up python and pip on wsl (ref. [here](https://learn.microsoft.com/en-us/windows/python/web-frameworks#set-up-your-development-environment))

```bash
#Update packages
sudo apt update && sudo apt upgrade

# Install Python, pip, and venv
sudo apt upgrade python3
sudo apt install python3-pip
sudo apt install python3-venv
```

Create your virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
deactivate
```



## Docker on WSL2

Steps following the installtion option through apt repository. Other installation options can be found here](https://docs.docker.com/engine/install/ubuntu/)

**Setup docker apt repos:**

```bash
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```



**Install latest version:**

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

```



**Check if docker is running**

```bash
 sudo docker run hello-world

```



**Starting and stopping docker:**

```bash
sudo service docker start

```

