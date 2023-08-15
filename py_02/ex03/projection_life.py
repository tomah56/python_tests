import matplotlib.pyplot as plt


def get_value(data, target_year):
    year = data.iloc[0, 1:].astype(int)
    if year.isin([target_year]).any():
        index = year[year == target_year].index[0]
    else:
        index = 0
    value = data[index]
    return value


def plot(data_life, data_gdp, target_year):
    """
    Plots the dataset based on a parameter what will be searched.
    """
    values_life = get_value(data_life, target_year)
    values_gdp = get_value(data_gdp, target_year)
    valid_indices = ~values_life.isna() & ~values_gdp.isna()
    values_life_valid = values_life[valid_indices][1:]
    values_gdp_valid = values_gdp[valid_indices][1:]
    # print(values_life_valid)
    plt.scatter(values_gdp_valid, values_life_valid, color='blue', marker='o')
    plt.xlabel('Gross domestic product')
    plt.ylabel('Life Expectancy')
    plt.title(target_year)
    plt.xscale('log')
    plt.show()
