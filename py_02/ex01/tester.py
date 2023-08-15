from load_csv import load
from aff_life import plot


def main():
    try:
        my_data = load("life_expectancy_years.csv")
        plot(my_data, "France")
        # plot(my_data, "Germany")
    except (KeyError, Exception) as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
