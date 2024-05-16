from descriptive_statistics_plotter import DescriptiveStatisticsPlotter
import pandas as pd
from sectioner import Sectioner
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def configure_pandas():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)
    pd.set_option('display.expand_frame_repr', False)


def print_section(section):
    print('\n' + section + '\n')


def main():
    configure_pandas()
    data_frame = pd.read_csv('../dataset/heart_statlog_cleveland_hungary_final.csv')

    sectioner = Sectioner()
    plotter = DescriptiveStatisticsPlotter(data_frame)

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
    plotter.plot_histogram('target', 'Target Balance', 2, 'target_balance')
    print_section('Target variable density per class:\n' + str(data_frame['target'].value_counts(normalize=True)))

    sectioner.pause_execution()
    continuous_variables = ['age', 'resting bp s', 'cholesterol', 'max heart rate', 'oldpeak']
    continuous_y_labels = ['Age', 'Resting Blood Pressure (mm Hg)', 'Total Cholesterol (mg/dl)',
                           'Maximum Heart Rate Achieved', 'ST Depression Induced By Excercise']
    continuous_names = ['age', 'resting_bp_s', 'total_cholesterol', 'maximum_heart_rate_achieved',
                        'st_depression_induced_by_excercise']
    for (variable, label, name) in zip(continuous_variables, continuous_y_labels, continuous_names):
        plotter.plot_continuous_distribution(variable, label, name, 20)
    print()

    sectioner.pause_execution()
    discrete_variables = ['sex', 'chest pain type', 'fasting blood sugar', 'resting ecg', 'exercise angina', 'ST slope']
    discrete_y_labels = ['Sex', 'Chest Pain Type', 'Fasting Blood Sugar', 'Resting ECG', 'Exercise Induced Angina',
                         'Peak ST Segment']
    discrete_names = ['sex', 'chest_pain_type', 'fasting_blood_sugar', 'resting_ecg', 'exercise_angina', 'st_slope']
    for (variable, label, name) in zip(discrete_variables, discrete_y_labels, discrete_names):
        plotter.plot_discrete_distribution(variable, label, name)
    print()

    sectioner.pause_execution()
    average_cholesterol_without_zeroes = data_frame[data_frame['cholesterol'] != 0]['cholesterol'].mean()
    print_section(f'{round(sum(data_frame['cholesterol'] == 0) / len(data_frame['cholesterol']) * 100, 3)}% of '
                  f'cholesterol values are 0, replacing with average...\nThe average is: '
                  f'{average_cholesterol_without_zeroes}')
    data_frame.replace({'cholesterol': 0}, average_cholesterol_without_zeroes, inplace=True)
    plotter.plot_boxplot('cholesterol', 'Corrected Cholesterol', 'corrected_cholesterol')

    sectioner.pause_execution()
    average_oldpeak_without_negatives = data_frame[data_frame['oldpeak'] >= 0]['oldpeak'].mean()
    print_section(f'{round(sum(data_frame['oldpeak'] < 0) / len(data_frame['oldpeak']) * 100, 3)}% of oldpeak values '
                  f'are negative, replacing with average...\nThe average is: {average_oldpeak_without_negatives}')
    data_frame.replace({'oldpeak': 0}, average_oldpeak_without_negatives, inplace=True)
    plotter.plot_boxplot('oldpeak', 'Corrected Oldpeak', 'corrected_oldpeak')

    sectioner.pause_execution()
    average_blood_pressure_without_zeroes = data_frame[data_frame['resting bp s'] != 0]['resting bp s'].mean()
    print_section(f'{round(sum(data_frame['resting bp s'] == 0) / len(data_frame['resting bp s']) * 100, 3)}% of '
                  f'blood pressure values are 0, replacing with average...\nThe average is: '
                  f'{average_blood_pressure_without_zeroes}')
    data_frame.replace({'resting bp s': 0}, average_blood_pressure_without_zeroes, inplace=True)
    plotter.plot_boxplot('resting bp s', 'Corrected Blood Pressure', 'corrected_resting_bp_s')

    plotter.data_frame = data_frame

    sectioner.pause_execution()
    plotter.plot_correlation_heatmap('Correlation Heatmap', 'correlation_heatmap')
    print()

    sectioner.pause_execution()
    print_section('Splitting data into training and test sets...')
    X = data_frame.drop('target', axis=1)
    y = data_frame['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.3, random_state=42)
    print('Finished splitting data into training and test sets...')

    print_section('Scaling data...')
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    print('Finished scaling data...')


if __name__ == '__main__':
    main()
