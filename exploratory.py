import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


class ExploratoryDataAnalysis:
    def __init__(self, data):
        self.data = data

    def plot_histogram(self, column, bins=30, title="Histogram"):
        plt.figure(figsize=(10, 6))
        sns.histplot(self.data[column], bins=bins, kde=True)
        plt.title(title)
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.show()

    def plot_time_series(self, date_column, target_column, title="Time Series Plot"):
        plt.figure(figsize=(12, 6))
        self.data.groupby(date_column)[target_column].sum().plot()
        plt.title(title)
        plt.xlabel(date_column)
        plt.ylabel(target_column)
        plt.show()

    def plot_bar(self, category_column, value_column, title="Bar Plot"):
        plt.figure(figsize=(12, 6))
        sns.barplot(x=category_column, y=value_column, data=self.data)
        plt.title(title)
        plt.xlabel(category_column)
        plt.ylabel(value_column)
        plt.xticks(rotation=45)
        plt.show()

    def plot_box(self, category_column, value_column, title="Box Plot"):
        plt.figure(figsize=(12, 6))
        sns.boxplot(x=category_column, y=value_column, data=self.data)
        plt.title(title)
        plt.xlabel(category_column)
        plt.ylabel(value_column)
        plt.xticks(rotation=45)
        plt.show()

    def plot_scatter(self, x_column, y_column, title="Scatter Plot"):
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x=x_column, y=y_column, data=self.data)
        plt.title(title)
        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.show()
