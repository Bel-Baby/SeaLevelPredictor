import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Import the data
    df = pd.read_csv('epa-sea-level.csv')

    # Create a scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Get the slope and y-intercept of the line of best fit
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit
    x = np.arange(min(df['Year']), 2051)
    plt.plot(x, slope * x + intercept, color='red')

    # Get the slope and y-intercept of the line of best fit for the data from 2000 onwards
    recent_df = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])

    # Plot the line of best fit for the data from 2000 onwards
    x_recent = np.arange(min(recent_df['Year']), 2051)
    plt.plot(x_recent, slope_recent * x_recent + intercept_recent, color='green')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
    
    predict_sea_level()