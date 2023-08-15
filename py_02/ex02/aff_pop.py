import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from matplotlib.ticker import MultipleLocator


def millions_formatter(x, pos):
    return f"{x / 1000000:.0f}M"


def plot(data_frame, country_1, country_2, target_year):
    """
    Plots the dataset based on a parameter what will be searched.
    """
    # Find the row (line) that matches the desired country
    elect_row_2 = data_frame[data_frame[0] == country_2]
    select_row_1 = data_frame[data_frame[0] == country_1]
    if not select_row_1.empty and not elect_row_2.empty:
        year = data_frame.iloc[0, 1:].astype(int)
        index = year.shape[0]
        if year.isin([target_year]).any():
            index = year[year == target_year].index[0]
            print(index)
        else:
            print("Not critical Error: year not found")
        year_range = range(1800, target_year + 1)
        # Extract numerical values for plotting (excluding the country name)
        values = select_row_1.iloc[:,
                                   1:(index + 1)].values.flatten().astype(int)
        values2 = elect_row_2.iloc[:,
                                   1:(index + 1)].values.flatten().astype(int)
        # Plot the values
        plt.plot(year_range, values, label=country_1)
        plt.plot(year_range, values2, label=country_2)
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend()
        interval = 20000000  # Specify the interval value
        locator = MultipleLocator(interval)
        plt.gca().yaxis.set_major_locator(locator)
        formatter = FuncFormatter(millions_formatter)
        plt.gca().yaxis.set_major_formatter(formatter)
        plt.show()
    else:
        print(f"No data found for {country_1}")
