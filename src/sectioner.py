class Sectioner:
    def __init__(self):
        self.__section_iterator = iter([
            'Data Set Visualization',
            'Data Set Information',
            'Cell Null Checking',
            'Duplicate Row Checking',
            'Data Set Descriptive Statistics',
            'Target Variable Balance Checking',
            'Continuous Variable Distribution Plots',
            'Discrete Variable Distribution Plots',
            'Cholesterol Correction',
            'Oldpeak Correction',
            'Blood Pressure Correction',
            'Generating Correlation Matrix With Heatmap',
            'Data Set Preparation For Model Training',
            'Naive Bayes Classification',
            'Naive Bayes Result Overview',
            'Random Forest Classification',
            'Random Forest Result Overview',
            'Decision Tree Classification',
            'Decision Tree Result Overview',
            'Extra Trees Classification',
            'Extra Trees Result Overview',
            'Artificial Neural Network Classification',
            'Artificial Neural Network Result Overview',
            'Models Comparison',
            'Retrospect'
        ])
        self.__advancement_message = 'Enter \'a\' to advance to '

    def pause_execution(self):
        try:
            section = self.__section_iterator.__next__()
        except StopIteration:
            section = 'nothing'
        while input(self.__advancement_message + section + ': ') not in ['a', 'A']:
            pass
