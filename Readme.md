## Radio data analysis
This is a course project for *ASTRO-5010* at *University of Glasgow*.

## Data set
We employ the data obtained from:
1. NoRP: Nobeyama Radio Polarimeters
2. RSTN: Radio Solar Telescope Network

## Purpose
We conduct basic level data analysis and plotting to understand:
1. Gyrosynchrotron emissions
2. Plasma emissions

## Steps
We will perform the tasks with the following steps:
1. Load NoRP data set
2. Convert time array data to standard format
3. Filter out valid data readouts
4. Filter out quiet sun noise at assigned freq
5. Plot freq based flux data against time
6. Load RSTN data
7. Fit gyrosynchrotron emission
8. Fit plasma emission

## File structure
Main file:
- main.py               ## main script

Data modules:
- data_loader.py        ## To load csv files
- data_norp_handler.py  ## To handle files related to NoRP data
- data_rstn_handler.py  ## To handle files related to RSTN data

Plotter modules:
- data_plotter.py       ## To plot figures

Readme:
- Readme.md             ## Simple readme file