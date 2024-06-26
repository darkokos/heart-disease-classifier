import matplotlib.pyplot as plt
import os
from pathlib import Path
import seaborn as sns
from sklearn.metrics import confusion_matrix


class DescriptiveStatisticsPlotter:
    def __init__(self, data_frame):
        self.__data_frame = data_frame
        self.__plot_directory = '../plots'
        sns.set_style('whitegrid')

    @property
    def data_frame(self):
        return self.__data_frame

    @data_frame.setter
    def data_frame(self, data_frame):
        self.__data_frame = data_frame

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
            sns.histplot(self.__data_frame[x_label], ax=ax, bins=bins, kde=True, palette='coolwarm')
            ax.set_title(f'Distribution of {y_label}')
            ax.set_label(x_label)
            ax.set_ylabel(y_label)

            self.__save_and_show_plot(x_label, name)
        except KeyError:
            print('Key error')

    def plot_histogram(self, label, y_label, bins, name):
        fig, ax = plt.subplots()
        try:
            sns.histplot(self.__data_frame[label], bins=bins, palette='coolwarm')
            ax.set_title(y_label)

            self.__save_and_show_plot(label, name)
        except KeyError:
            print('Key error')

    def plot_boxplot(self, x_label, y_label, name):
        fig, ax = plt.subplots()
        try:
            sns.boxplot(self.__data_frame[x_label], ax=ax, hue_norm=x_label)
            ax.set_title(y_label)
            ax.set_xlabel(x_label)
            ax.set_ylabel(y_label)

            self.__save_and_show_plot(x_label, name)
        except KeyError:
            print('Key error')

    def plot_correlation_heatmap(self, title, name):
        plt.figure(figsize=(10, 8))

        correlation_matrix = self.__data_frame.corr(numeric_only=True)
        sns.heatmap(correlation_matrix, vmin=-1, vmax=1, fmt='.2f', cmap='coolwarm', annot=True, linewidths=.5)

        plt.title(title, fontsize=20)
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)

        self.__save_and_show_plot('', name)

    def plot_confusion_matrix(self, model, y_test, y_pred, name):
        plt.figure(figsize=(8, 6))

        sns.heatmap(confusion_matrix(y_test, y_pred), fmt='d', cmap='coolwarm', cbar=False, annot=True)

        plt.title('Confusion Matrix', fontsize=20)
        plt.xlabel('Predicted classes')
        plt.ylabel('True classes')

        self.__save_and_show_plot(model, name)

    def plot_barplot(self, data):
        plt.figure(figsize=(13, 6))

        plt.barh(list(data.keys()), list(data.values()))

        plt.xlim(0, 1)
        plt.title('Model Accuracies')
        plt.xlabel('Accuracy')

        plt.gca().invert_yaxis()

        self.__save_and_show_plot('', 'accuracies')

    def plot_feature_importances(self, model_name, feature_importances):
        feature_importances.plot(kind='bar', figsize=(10, 12))

        plt.title(f'Feature importances in {model_name}')
        plt.xlabel('Features')
        plt.ylabel('Importance')
        plt.xticks(rotation=45)
        plt.yticks(rotation=0)

        self.__save_and_show_plot('', model_name + '_feature_importances')
