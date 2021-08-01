import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')

# Clean data
# Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset
f25 = df['value'] <= df['value'].quantile(0.025)
f75 = df['value'] >= df['value'].quantile(0.975)
cond = (f25 | f75)
df = df.drop(index=df[cond].index)



def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots()
    fig.set_figheight(6)
    fig.set_figwidth(14)

    ax.plot_date(df.index, df['value'], linestyle="solid", marker=None, color="red")
    ax.set_ylabel('Page Views')
    ax.set_xlabel('Date')
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
  
    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    #show average daily page views for each month grouped by year
    
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar['date']).year
    df_bar['Month'] = pd.DatetimeIndex(df_bar['date']).strftime("%B")
    df_grp = df_bar.groupby(['year', 'Month'])
    # series
    df_grp['value'].apply(lambda x: x.mean())

    # Draw bar plot
    #darkgrid, whitegrid, dark, white, ticks
    sns.set_style("ticks")
    # , palette="rocket"
    list_month = ['January','February','March','April','May','June','July','August','September','October','November','December']
    g = sns.catplot(x="year", kind="bar", hue="Month", y="value", data=df_bar, hue_order = list_month, ci=None, legend=False, palette="hls")
    fig = g.fig
    ax = g.ax    
    ax.set_ylabel('Average Page Views')
    ax.set_xlabel('Years')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', title="Month")
    plt.setp(ax.get_legend().get_texts(), fontsize='8')
    plt.setp(ax.get_legend().get_title(), fontsize='8')
    # Draw bar plot
    plt.tight_layout()
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def fixed_boxplot(*args, label=None, **kwargs):
  sns.boxplot(*args, **kwargs, labels=[label])

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = pd.DatetimeIndex(df_box['date']).year
    df_box['month'] = pd.DatetimeIndex(df_box['date']).strftime("%B")
    df_box['Year'] = df_box['year'] 
    df_box['Month'] = df_box['month'].str.slice(stop=3)
    df_box["Page Views"] = df_box["value"]
    df_box.sort_values(by=['year','date'], ascending=[False, True], inplace=True)
    # Draw box plots (using Seaborn)
    sns.set_style("ticks")
    g = sns.PairGrid(df_box, y_vars=["Page Views"], x_vars=["Year", "Month"], palette="hls")
    g.map(fixed_boxplot)
    fig = g.fig
    fig.set_figheight(6)
    fig.set_figwidth(16)
    fig.axes[0].set_ylabel('Page Views')
    fig.axes[1].set_ylabel('Page Views')
    fig.axes[0].set_title('Year-wise Box Plot (Trend)')
    fig.axes[1].set_title('Month-wise Box Plot (Seasonality)')
    plt.tight_layout()




    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
