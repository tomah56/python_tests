from load_csv import load
from projection_life import plot


def convert_to_number(value):
    if isinstance(value, str):
        if 'M' in value:
            return float(value.replace('M', '')) * 1_000_000
        elif 'k' in value:
            return float(value.replace('k', '')) * 1_000
        elif 'B' in value:
            return float(value.replace('B', '')) * 1_000_000_000
        else:
            return float(value)
    else:
        return int(value)


def main():
    try:
        data_life = load("life_expectancy_years.csv")
        df = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        data_gdp = df.copy()
        for col in data_gdp.columns[1:]:
            data_gdp[col] = data_gdp[col].apply(convert_to_number)
        plot(data_life, data_gdp, 1900)
    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
