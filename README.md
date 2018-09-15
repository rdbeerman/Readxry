# Readxry
Readxry is made for interpreting .xry files from the Leybold X-ray apparatus. The .xry files are saved in plain text but have a non-standard format, readxry inteprets this format and plots the relevant data.

## Features
Readxry currently offers the following features, subject to change:

* Import data files.
* Display Beta settings.
* Plot Rate as a function of Beta.
* Save plots as jpeg/png.

Planned features are:

* Transfer beta to wavelength for different crystals.
* Plot multiple measurement series.
* Save data as .csv.

## Hardware
Readxry is made for use with .xry files the Leybold x-ray Apparatus series.

## Dependencies
Readxry is written in Python 3.6, it's dependencies are:

* tkinter
* numpy
* matplotlib