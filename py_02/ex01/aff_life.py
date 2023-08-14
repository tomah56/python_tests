import matplotlib.pyplot as plt


def plot(data_frame, desired_country):
    """
    Plots the dataset based on a parameter what will be searched.
    """
    # Find the row (line) that matches the desired country
    selected_row = data_frame[data_frame[0] == desired_country]
    if not selected_row.empty:
        year = data_frame.iloc[0, 1:].astype(int)
        # Extract numerical values for plotting (excluding the country name)
        values = selected_row.iloc[:, 1:].values.flatten().astype(float)
        # Plot the values
        plt.plot(year, values)
        plt.xlabel('Year')
        plt.ylabel('Life Expectancy')
        plt.title(f'{desired_country} Life Expectancy Projections')
        plt.show()
    else:
        print(f"No data found for {desired_country}")
