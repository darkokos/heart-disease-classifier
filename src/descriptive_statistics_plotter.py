import matplotlib.pyplot as plt
import os
from pathlib import Path
import seaborn as sns


class DescriptiveStatisticsPlotter:
    def __init__(self, data_frame):
        self.__data_frame = data_frame
        self.__plot_directory = '../plots'
        sns.set_style('whitegrid')

    def __save_and_show_plot(self, label, name):
        dir_path = os.path.join(self.__plot_directory, label)
        Path(dir_path).mkdir(parents=True, exist_ok=True)

        file_path = os.path.join(dir_path, f'{name}.png')
        plt.savefig(file_path)
        plt.show()

    def plot_discrete_distribution(self, x_label, y_label, name):
        fig, ax = plt.subplots()
        try:
            sns.countplot(data=self.__data_frame, x=x_label, ax=ax, hue='target', palette='coolwarm')
            ax.set_title(f'Distribution of {y_label}')
            ax.set_xlabel(x_label)
            ax.set_ylabel('Frequency')
            ax.legend(title='target', loc='upper left')

            self.__save_and_show_plot(x_label, name)
        except KeyError:
            print('Key error')

    def plot_continuous_distribution(self, x_label, y_label, name, bins):
        fig, ax = plt.subplots()
        try:
            sns.histplot(self.__data_frame[x_label], ax=ax, bins=bins, kde=True)
            ax.set_title(f'Distribution of {y_label}')
            ax.set_label(x_label)
            ax.set_ylabel(y_label)

            self.__save_and_show_plot(x_label, name)
        except KeyError:
            print('Key error')

    def plot_histogram(self, label, y_label, bins, name):
        fig, ax = plt.subplots()
        try:
            sns.histplot(self.__data_frame[label], bins=bins)
            ax.set_title(y_label)

            self.__save_and_show_plot(label, name)
        except KeyError:
            print('Key error')
