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
        ])
        self.__advancement_message = 'Enter \'a\' to advance to '

    def pause_execution(self):
        try:
            section = self.__section_iterator.__next__()
        except StopIteration:
            section = 'nothing'
        while input(self.__advancement_message + section + ': ') not in ['a', 'A']:
            pass
