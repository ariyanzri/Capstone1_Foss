---
title: "CyVerse FOSS 2021 Team B Project"
site: bookdown::bookdown_site
output: html_document
---

# CyVerse FOSS 2021 Team B Project

## Purpose
We sought out to apply multiple skills learned during the Spring 2021 CyVerse FOSS (Foundational Open Science Skills) Workshop as a team in a simple, but effective project. These skills include use of GitHub, GitHub pages, running a virtual machine with Atmosphere, pulling a script from GitHub repo, running a script employing Docker to perform a specific task (e.g., open metadata for a RGB drone image of lettuce from the PhytoOracle Project).

### Project Script and Steps
A paired down version of this information is available in the [Project GitHub code directory](https://github.com/ariyanzri/Capstone1_Foss/tree/main/code).

These steps are assuming use of a virtual machine to perform task, possibly deployed from [CyVerse Atmosphere](https://atmo.cyverse.org). Please follow these steps to reproduce the results and perform project task (e.g., view image metadata).

1. Install Docker
  
 ```sudo snap install docker```
 
 - ```sudo \``` gives super user privileges
 - ```snap \``` is a call to a Linux package manager
 - ```install docker``` will install Docker on a virtual machine 
 
2. Pull this Docker image from DockerHub to run Python script
 
```sudo docker pull ariyanzarei/foss_image```

 - ```sudo \``` gives super user privileges
 - ```docker pull \``` Docker command to pull a container image from a DockerHub repo
 - ```ariyanzarei/foss_image``` DockerHub repo and container image name to pull (will default to 'latest' tag)

3.  Clone this GitHub repository to virtual machine ```/home``` workspace.
  
```sudo git clone https://github.com/ariyanzri/Capstone1_Foss.git```

- ```sudo git clone \``` Git command to clone/copy a remote GitHub repo
- ```https://github.com/ariyanzri/Capstone1_Foss.git``` URL to GitHub repo to clone

4. Change directory to folder that contains script to run 
 
```cd [path to git]/Capstone1_Foss/code```

- ```cd \``` Linux command to change directory
- ```[path to git]/Capstone1_Foss/code``` You will have to provide path (fill in []) depending on where the GitHub repo was cloned to, then navigate to 'code' folder

5. Change permissions of the run file and make it executable
  
```sudo chmod +x run.sh```

- ```sudo chmod +x \``` Call used to change the access permissions of file system object (script) and executable (```+x``` flag)
- ```run.sh``` Shell script to be run to perform task

6. Run this file to download the tar file and unzip it (_tar file is 3.22GB_)
 
```./run.sh```

7. Run the code file to visualize

**Note:** Prior to running Docker, the file paths to the drone_data directory may need to be updated in the ```visualize.py``` script.

Use ```sudo nano [path to local git repo]/Capstone1_Foss/code/visualize.py``` to update the ```drone_data``` directory path with the GNU nano text editor.

```sudo docker run -v /home:/home -it ariyanzarei/foss_image python3 [path to local git repo]/Capstone1_Foss/code/visualize.py```

 - ```sudo \``` gives super user privileges
 - ```docker run \``` Docker command to run a specified container image from a DockerHub repo
 - ```-v /home:/home \``` Set the volume of the container
 - ```-it \``` Docker run flag to make container interative
 - ```ariyanzarei/foss_image \``` DockerHub repo and container image name to run
 - ```python3 \``` Software to run in container (in this case Python version 3)
 - ```[path to local git repo]/Capstone1_Foss/code/visualize.py``` Path and directory to Python script to perform task

### Acknowledgement
The imagery used in our project was graciously supplied by the PhytoOracle Project. PhytoOracle is a scalable, modular data pipeline for phenomics research. It uses CCTools’ Makeflow and WorkQueue distributed task management frameworks.

PhytoOracle is licensed under the [MIT License](https://github.com/LyonsLab/PhytoOracle/blob/master/LICENSE).

For more information, please visit the PhytoOracle [Read the Docs website](https://phytooracle.readthedocs.io/en/latest/contents.html), which is partially built on code initially developed by the TERRA-REF project and AgPipeline team.

This material based upon work supported by Cyverse & CCTools. Cyverse is based upon work supported by the National Science Foundation under Grant Numbers: DBI-0735191, DBI-1265383, DBI-1743442. CCTools is based upon work supported by the National Science Foundation under Grant Numbers: CCF-0621434 and CNS-0643229.
