import matplotlib.pyplot as plt


def plot(data_frame, desired_country, c2):
    """
    Plots the dataset based on a parameter what will be searched.
    """
    # Find the row (line) that matches the desired country
    o_row = data_frame[data_frame[0] == c2]
    selected_row = data_frame[data_frame[0] == desired_country]
    if not selected_row.empty and not o_row.empty:
        year = data_frame.iloc[0, 1:].astype(int)
        # Extract numerical values for plotting (excluding the country name)
        values = selected_row.iloc[:, 1:].values.flatten().astype(int)
        values2 = o_row.iloc[:, 1:].values.flatten().astype(int)
        # Plot the values
        plt.plot(year, values, label=desired_country)
        plt.plot(year, values2, label=c2)
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title('Population Projections')
        plt.legend()
        plt.show()
    else:
        print(f"No data found for {desired_country}")
