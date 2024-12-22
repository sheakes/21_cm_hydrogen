# 21_cm_hydrogen

My very first astro code!

Having just finished my first computing course in Fall 2021 CPSC:103 Systematic Program Design I intended to put my new skills in programming to astronomical data.

Using previously data collected from the open source radio telescope PICTOR (https://pictortelescope.com/) based in Athens, Greece I computed the dopler shift for hydrogen clouds in the constellation of Cygnus. The radio telescope was pointed at zenith and specifically at a galactic long./lat. of 72 degrees 15 minutes/ 6 degrees 55 minutes although the PICTOR telescope has a field of view of approximately 9 degrees and would include most of the Cygnus constellation.

After submitting the observation request I received the following email.

Your observation has been carried out by PICTOR successfully!
Observation name: Short Duration Observation 3
Observation datetime: 2021-10-06 20:07:34 (UTC+3)
Center frequency: 1420000000.0 Hz
Bandwidth: 1000000 Hz
Sample rate: 1000000 samples/sec
Number of channels: 2048
Number of bins: 100
Observation duration: 60 sec
Observation ID: 99775993

And was sent the following graphs, analysis, and a csv file of the data recorded.
![image](https://user-images.githubusercontent.com/89617602/232857533-e861bb92-f109-49f5-84b7-8b486c1d83c3.png)

Using some simple import csv code, astropy, and matplotlib packages. I emulated the above frequency graphic and printed the following.
![Relative Power vs Frequency](https://user-images.githubusercontent.com/89617602/232877342-3e6a0035-cf35-4070-8940-70eda7416efc.png)

Using the dopler shift formula Velocity = (c*rest frequency/shifted freqency)-c where c is 3e+8 m/s I calculated that the hydrogen clouds were moving towards observatory at approximately 86 km/s due to wavelength being blueshifted.

