# Visualizing Drone Images

In this part of our repository, we developed a number of scripts by which we can download, unzip and visualize a complete drone dataset. Please follow these steps to reproduce the results and visualize the codes. 

Steps to run the code
* Install docker  
 ```sudo snap install docker```. 
* Pull this docker from docker hub to run the code with  
```sudo docker pull ariyanzarei/full_geocorrection```
* Install Exif reader on the machine  
```sudo apt install exif```
* Clone this github repository.  
```git clone https://github.com/ariyanzri/Capstone1_Foss.git```
* Change directory to   
```cd [path to git]/Capstone1_Foss/code```.
* Change permissions of the run file and make it executable  
```chmod +x run.sh```
* Run this file to download the tar file and unzip it  
```./run.sh```
* Run the code file to visualize  
```sudo docker run -v /home:/home -it ariyanzarei/imerg_deep_learning python3 [path to local git repo]/Capstone1_Foss/code/visualize.py```
