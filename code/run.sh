#! /bin/bash

# Go to existing directory 
cd ~

# Create a new directory called 'drone_data'
mkdir drone_data

# Change into directory 'drone_data'
cd drone_data

# Get data from CyVerse Data Store 
wget https://de.cyverse.org/dl/d/7DB350A5-1EAB-4532-9C35-79AE08B9D9FF/2.27.20_P4_15m_RGB.tar.gz

# Decompress tar file containing imagery file
tar -xvf 2.27.20_P4_15m_RGB.tar.gz

# remove the tar file (not needed anymore following decompressing)
rm 2.27.20_P4_15m_RGB.tar.gz

