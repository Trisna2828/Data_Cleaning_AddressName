# Data_Cleaning_AddressName
This is an example of how I use Python to clean and manipulate the spatial data attribute (Address Name) in Bahasa Indonesia
# Begin With Collecting Problems
Knowledge of our data is the fundamental part before we can indentify the problem. After problems collected, we have to clean the small problem, the typo !
# First little step to Clean
I do some cleaning process, small steps, to Clean the wrong word, double space, and another Typo
![](https://github.com/Trisna2828/Data_Cleaning_AddressName/blob/main/src/Address_1.JPG)
# Start to Clean the Address Structure
This is the fun part, we need to have a good problem solving thingking, how to manage the problem into a cleaning process, what the main problem, and whats the sub problem, so we can filter our data, into a different conditions, then at the end, each of the condition has it's own solution. So, It just like a root cause analysis on Machine Learning (in a simple form)
![](https://github.com/Trisna2828/Data_Cleaning_AddressName/blob/main/src/Address_2.JPG)
![](https://github.com/Trisna2828/Data_Cleaning_AddressName/blob/main/src/Address_3.JPG)
# Blend All Together Into A Tool
Since I working with spatial data, with a static structure, I put all the functions into a model builder. Model Builder is a tool we can create on ArcGIS Desktop software for spatial data, to create a collection of functions, to finish certain tasks, we can call it a processing model.
With this model, I can run all of cleaning process again and again, for every data stored from the data operation team, daily. I can simply put the python functions into each of step in the model builder. 
In case If I run a regular data points instead of spatial data, I also being able to run the process on a Jupyter Notebook using Pandas.
![](https://github.com/Trisna2828/Data_Cleaning_AddressName/blob/main/src/Address_Model.JPG)

# Run the Tool
First lets pretend we want to clean the address of Restaurants data set in Jakarta
![](https://github.com/Trisna2828/Data_Cleaning_AddressName/blob/main/src/Restaurant_PSQL.JPG)
Run the tool in ArcGIS

