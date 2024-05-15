import pandas as pd
from sectioner import Sectioner


def print_section(section):
    print('\n' + section + '\n')


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.expand_frame_repr', False)

    data_frame = pd.read_csv('../dataset/heart_statlog_cleveland_hungary_final.csv')

    sectioner = Sectioner()

    sectioner.pause_execution()
    print_section(str(data_frame.head()))

    sectioner.pause_execution()
    print()
    data_frame.info()
    print()

    sectioner.pause_execution()
    print_section('Null values per column:\n' + str(data_frame.isnull().sum()))

    sectioner.pause_execution()
    print_section('Duplicate rows present: ' + str(data_frame.duplicated().empty))

    sectioner.pause_execution()
    print_section('Descriptive statistics of data set:\n' + str(data_frame.describe().T))

    sectioner.pause_execution()
    print_section('Target variable density per class:\n' + str(data_frame['target'].value_counts(normalize=True)))


if __name__ == '__main__':
    main()
