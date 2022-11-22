import pandas as pd


def main():
    df = pd.read_csv('../../resources/spotify/dataset.csv', encoding='utf8', skiprows=[1])
    pd.set_option('display.max_rows', None)
    print(df)


if __name__ == '__main__':
    main()
