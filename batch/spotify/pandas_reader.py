import pandas as pd
import time


def main():
    start = time.time()
    df = pd.read_csv('../../resources/spotify/dataset.csv', encoding='utf8', skiprows=[1])
    pd.set_option('display.max_rows', None)
    print(df)
    end = time.time()
    print(f'Total time taken to run: {(end - start) * 1000}ms')


if __name__ == '__main__':
    main()
