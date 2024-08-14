# Conda and Miniconda

Conda **allows you to create separate environments, each containing their own files, packages, and package dependencies**. The contents of each environment do not interact with each other. 

Miniconda is a free minimal installer for [conda](https://docs.anaconda.com/).  It is a small bootstrap version of Anaconda that includes only conda, Python, the packages they both depend on, and a small number of other useful packages (like pip, zlib, and a few others).



## Installing miniconda on [WFS](./wfs.md) (Windows File System)



```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
# yes yes
source ~/.bashrc
rm Miniconda3-latest-Linux-x86_64.sh

# to ensure WSL can start normally without an active conda env
conda config --set auto_activate_base false
```



## Create a new conda environment

```bash
# version
conda --version

# Installing python 3.10 in environment named "py310"
conda create -n py310 python=3.10

# Activating environment
conda activate py310
		
```



## Other useful commands

```bash
# List environments
conda env list

# Installing packages on environment
conda install -n yourenvname [package]

#Deactivate environment
conda deactivate

# Delete unused environments
conda remove -n yourenvname -all

```



## Python requirements.txt and conda

It is common to use requirements.txt to specify a list of python packages.

But when working with conda, pip is not installed by default. 

Thus if not installed you will end up using the pip installed at userlevel. This is not recommended as you will install all requirements to the python in your global environment.



### Installing pip on conda environment

```bash
# Install pip
conda install pip

# Install requirements.txt file
pip install -r requirements.txt

```

