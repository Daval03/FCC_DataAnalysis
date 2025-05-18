import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("Page View Time Series Visualizer/fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# # Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
lower_bound = df['value'].quantile(0.025)  # 2.5% inferior
upper_bound = df['value'].quantile(0.975)  # 97.5% superior

df = df[(df['value'] >= lower_bound) & (df['value'] <= upper_bound)] 

#Create a draw_line_plot function that uses Matplotlib to draw a line chart similar to "examples/Figure_1.png". 
#The title should be Daily freeCodeCamp Forum Page Views 5/2016-12/2019. 
#The label on the x axis should be Date and the label on the y axis should be Page Views.
def draw_line_plot():
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    start_date = pd.to_datetime('2016-05-01')
    end_date = pd.to_datetime('2019-12-31')
    filtered_df = df.loc[(df.index >= start_date) & (df.index <= end_date)]
    # Draw line plot
    fig, ax = plt.subplots()
    ax.plot(filtered_df)
    ax.set_xlabel("Date")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_ylabel("Page Views")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df.index = pd.to_datetime(df.index, format='%Y-%m-%d')
    df_bar = df.groupby([df.index.year,df.index.month])["value"].mean()
    df_bar.index.names = ["year", "month"]
    df_plot = df_bar.unstack(level='month')

    # Draw bar plot
    fig, ax = plt.subplots(figsize=(14, 7))
    years = df_plot.index
    months = df_plot.columns
    n_months = len(months)
    bar_width = 0.5 / n_months
    month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    for i, month in enumerate(months):
        ax.bar(
            [y + i * bar_width for y in range(len(years))],  
            df_plot[month],                                  
            width=bar_width,
            label=f'{month_order[i]}'
        )
    ax.set_xlabel('Years', fontsize=12)
    ax.set_ylabel('Average Page Views', fontsize=12)
    ax.set_xticks([y + (n_months * bar_width) / 2 - bar_width for y in range(len(years))])
    ax.set_xticklabels(years)
    ax.legend(title='Months', bbox_to_anchor=(1.05, 1))
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(data=df_box, x='year', y='value', ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)', fontsize=14)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylabel('Page Views', fontsize=12)

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                   'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(data=df_box, x='month', y='value', order=month_order, ax=ax2)
    ax2.set_title('Month-wise Box Plot (Seasonality)', fontsize=14)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.set_ylabel('Page Views', fontsize=12)


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
