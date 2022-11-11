''' In this program i am trying to compare the population of different
countries given by user with three different graphs line graph,bar graph,
pie chart for the years 2010,2011,2012,2013,2014,2015'''

#Importing the required modules for the program
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#This method draws the pie chart with the given data
def piechart(x , label , titl):
    plt.figure()
    #pie function to draw the pie chart
    plt.pie(x , labels = label , autopct = "%1.1f%%")
    plt.title(titl)
    plt.legend(loc = "lower right")
    plt.show()
    
#this method draws the line graph for the given countries
def lineplot(x , y , no_countries , countries):
    plt.figure()
    for i in range(no_countries):
        #simple plot method draws the line plot
        plt.plot(x , y[0][i] , label = countries[i])
    plt.legend(loc = "upper right")
    plt.xlabel("Years")
    plt.ylabel("Population")
    plt.show()

#this method draws the bar graph for the given countries in the period of 2010 - 2015
def barplots(X , countries , no_of_countries):
    plt.figure()
    #creating a dictionary with the population and countries
    databar = dict(zip(countries , X))
    databar.update({"Years" : [2010,2011,2012,2013,2014,2015]})
    #Creating a data frame from the dict and drawing the bar plot
    pd.DataFrame(databar).plot.bar(x = "Years")
    plt.ylabel("Population")
    #using legend method for showing the country labels on the graph
    plt.legend(loc = "upper right")
    plt.show()

#Reading the data from the Data.csv using pandas
data = pd.read_csv("D:\\virtual machine\\PopulationData.csv")

#Creating the data frame with the data read from  the Data.csv
df = pd.DataFrame(data)

#Renaming the columns as 2010,2011,2012,2013,2014,2015 as it is easy to use
df=df.rename(columns = {"2010 [YR2010]" : "2010" , "2011 [YR2011]" : "2011" , "2012 [YR2012]" : "2012" , "2013 [YR2013]" : "2013" , "2014 [YR2014]" : "2014" , "2015 [YR2015]" : "2015"})

#selecting only the population rows from the whole dataset as this dataset is vast
datar = df.loc[df["Series Name"] == "Population, total"]

#selecting the data only the columns of countrycode and from years 2010-2015
datar = datar[["Country Code" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015"]]

#replacing all the non zero values to 0 as the population cannot be less than 0
datar = datar.replace(to_replace=".." , value="0")

#convertng the population to numeric values
datar[["2010","2011","2012","2013","2014","2015"]] = datar[["2010","2011","2012","2013","2014","2015"]].apply(pd.to_numeric)

#creating a list containing total population of the world for each specific years
tot = [datar["2010"].sum(),datar["2011"].sum(),datar["2012"].sum(),datar["2013"].sum(),datar["2014"].sum(),datar["2015"].sum()]

#an empty list for getting the population of countries of different years
x_values = []

#empty list for storing the country codes given by the user to compare
country_codes = []

#taking value from user how many countries he want to compare
no_countries = int(input("how many countries do you want to compare:"))

'''This loop takes the values of country codes and creating a list of population
of that country in the years from 2010-2015 ''' 
for i in range(no_countries):
    country_code = input("Enter Country code:")
    country_codes.append(country_code)
    data_need = datar.loc[datar["Country Code"] == country_code]
    x=[int(data_need["2010"]),int(data_need["2011"]),int(data_need["2012"]),int(data_need["2013"]),int(data_need["2014"]),int(data_need["2015"])]
    x_values.append(x)
    
    ''' preparing a list for pie chart by calculating and storing the values
    of the remaining population excluding the user given countries'''
    for i in range(6):
        tot[i] = tot[i]-x[i]

# list of years
y = ["2010","2011","2012","2013","2014","2015"]

#Calling the lineplot method 
lineplot(y , [x_values] , no_countries , country_codes)

''' In this for loop i am trying to draw 6 different pie charts for the 
populaation of different years for the given countries'''
for i in range(6):
    required_val_to_pie = []
    for j in range(no_countries):
        required_val_to_pie.append(x_values[j][i])
        
    #crearting a list of population in different years of the given countries
    #for using that in pie chart 
    required_val_to_pie.append(tot[i])
    piechart(np.array(required_val_to_pie) , country_codes + ["Rest Population"] , y[i])

#Calling the barplots method
barplots(x_values , country_codes , no_countries)