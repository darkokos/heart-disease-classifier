from descriptive_statistics_plotter import DescriptiveStatisticsPlotter
import pandas as pd
from sectioner import Sectioner


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


if __name__ == '__main__':
    main()
