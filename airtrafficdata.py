class DataLoader:
    def __init__(self, filepath):
        self.filepath = filepath

    def load_data(self):
        try:
            data = pd.read_csv(self.filepath)
            print("Data loaded successfully.")
            return data
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
