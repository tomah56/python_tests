from load_csv import load
from aff_pop import plot


def convert_to_number(value):
    if 'M' in value:
        return float(value.replace('M', '')) * 1_000_000
    elif 'k' in value:
        return float(value.replace('k', '')) * 1_000
    elif 'B' in value:
        return float(value.replace('B', '')) * 1_000_000_000
    else:
        return float(value)


def main():
    try:
        my_data = load("population_total.csv")
        df = my_data.copy()
        for col in df.columns[1:]:
            df[col] = df[col].apply(convert_to_number)
        plot(df, "Iran", "Hungary", 2000)
    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
