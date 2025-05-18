import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    #Use Pandas to import the data from epa-sea-level.csv.
    df = pd.read_csv("Sea Level Predictor/epa-sea-level.csv")
    # Create scatter plot
    #Use matplotlib to create a scatter plot using the Year column as the x-axis and the CSIRO Adjusted Sea Level column as the y-axis.
    #fig, ax = plt.subplots(figsize=(16, 6))

    plt.scatter(df["Year"],df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    #Use the linregress function from scipy.stats to get the slope and y-intercept of the line of best fit. Plot the line of best fit over the top of the scatter plot. Make the line go through the year 2050 to predict the sea level rise in 2050.
    pred_1 = linregress(df["Year"],df["CSIRO Adjusted Sea Level"])
    years_1 = np.arange(1880, 2051, dtype=np.float64) 
    y_pred_1 = pred_1.slope * years_1 + pred_1.intercept
    plt.plot(years_1,y_pred_1 )

    # Create second line of best fit
    df_200 = df[ df["Year"] >= 2000 ]
    pred_2 = linregress(df_200["Year"],df_200["CSIRO Adjusted Sea Level"])
    years_2 = np.arange(2000, 2051, dtype=np.float64) 
    y_pred_2 = pred_2.slope * years_2 + pred_2.intercept
    plt.plot(years_2,y_pred_2 )
    
    # Add labels and title
    plt.title('Rise in Sea Level', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Sea Level (inches)', fontsize=12)

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

