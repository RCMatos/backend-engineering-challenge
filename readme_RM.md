#	**BACKEND-ENGINEERING-CHALLENGE**
#	RODRIGO MATOS


##	Requirements

###Check if java is installed
**java has to be installed**
chech if java is installed by typing
java -version

###Check is anaconda is installed
anaconda to ease management of python libs (to install: https://www.anaconda.com/distribution/)

###Check if libraries are installed
**The following scripts were made using:**
pyspark (to install: pip install pyspark). In my case I used version '2.4.3'
numpy, is installed as part of the anaconda bundled and should be up to date. In my case I used version '1.16.2'
pandas, is installed as part of the anaconda bundled and should. In my case I used version '0.24.2'

###Check if the path is recognized by the system
Make sure that anaconda path is added to user variables, in my case I added C:\Users\Rodrigo\Anaconda3 to path
on the command shell write python. If the path to the python.exe was sucessfull it should open the python shell.
Make sure that hadoop libs are downloaded and added path, in my case I added C:\Users\Rodrigo\Hadoop\Bin to path

###Summary
**by running the Bat file**
All of the above condition should be met before going further for the scripts to work. 
If some of the changes aren't met please do the change, close this file and reboot your computer
**by running in anaconda using spyder IDE**
All of the above condition should be met except section **Check if the path is recognized by the system** before going further for the scripts to work. 
If some of the changes aren't met please do the change, close this file and reboot your computer


##	Usage
### Bat file
To run the code using pre-defined vars just double click on the bat file
### Command line
To run the code:

1-open the command line

2-Navigate to the folder where the scripts were downloaded

3-Create dummy data by running:

>>python create_dummy_data.py time_unit time_val

>>to create dummy data we can pass two types of variable time_unit  and time_val.

>>>-time_unit has to be in "seconds" or "minutes"

>>>-time_val has to be a given integer number

>>>-both parameters must be specified

>>create_dummy_data.py seconds 30

>>Creating dummy data using parameters time_unit=seconds and time_val=30

4-Analyse the data

>>python get_KPI.py time_unit time_val analysis_type

>>to analyse data we can pass three types of variables time_unit, time_val and analysis_type.

>>>-time_unit has to be in "seconds" or "minutes"

>>>-time_val has to be a given sinteger number

>>>-analysis_type this is a parameter to define the partition for determining the average delievery time

>>>It can take the values source_language or target_language or source_target_language or all_recs

>>>-all parameters above must be specified

>>get_KPI.py seconds 30 all_recs

>>Analysing data using parameters time_unit=seconds, time_val=30,analysis_type=all_recs

