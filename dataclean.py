class DataCleaning:
    def __init__(self, data):
        self.data = data

    def check_data_types(self):
        return self.data.dtypes

    def check_missing_values(self):
        return self.data.isnull().sum()

    # Additional method to handle missing values (example: fill with median for numeric columns)
    def fill_missing_values(self, fill_strategy='median'):
        for column in self.data.select_dtypes(include='number').columns:
            if fill_strategy == 'median':
                self.data[column].fillna(self.data[column].median(), inplace=True)
            elif fill_strategy == 'mean':
                self.data[column].fillna(self.data[column].mean(), inplace=True)
        print("Missing values filled.")
