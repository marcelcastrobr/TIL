# TIL  - Windows File System



Windows File System (WFS) is a feature of windows that allows users to run a linux environment on Windows machine without need to have a virtual machine or dual booting.

Important features:

- run different linux distributions
- command line tool such as bash

WSL2 is the default distro that runs as isolated containers inside the WSL2 managed virtual machine and share same network namespace, device tree (/dev/pts) CPU/Kernel/memory/etc. but have its own PID namspace, mount/user/cgroup namespace.



**Basic commands**

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

