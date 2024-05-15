class Sectioner:
    def __init__(self):
        self.section_iterator = iter([
            'Data Set Visualization',
            'Data Set Information',
            'Cell Null Checking',
            'Duplicate Row Checking',
            'Data Set Descriptive Statistics',
            'Target Variable Balance Checking',
        ])
        self.advancement_message = 'Enter a to advance to '

    def pause_execution(self):
        section = self.section_iterator.__next__()
        while input(self.advancement_message + section + ': ') not in ['a', 'A']:
            pass
