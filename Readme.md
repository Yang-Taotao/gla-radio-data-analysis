## Radio data analysis
This is a course project for *ASTRO-5010* at *University of Glasgow*.
- Drafted: Mar 15, 2023
- Editted: Mar 29, 2023

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

## Working file structure
Main file:
- main.py               

Data reader modules:
- data_reader.py        

Data processing modules:
- data_handler.py       

Data fitter modules:
- data_fitter.py        

Plotter modules:
- data_plotter.py       

## Supplementary files
Readme:
- Readme.md             

Legacy plotter repo:
- data_legacy.py        
