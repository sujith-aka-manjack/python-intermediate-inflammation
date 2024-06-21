"""Module containing mechanism for calculating standard deviation between datasets."""

import glob
import os
import numpy as np

from inflammation import models, views
# import models, views


class CSVDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def get_data_files(self):
        self.data_file_paths = glob.glob(
            os.path.join(self.data_dir, "inflammation*.csv")
        )
        if len(self.data_file_paths) == 0:
            raise ValueError(
                f"No inflammation csv's found in path {self.data_file_paths}"
            )
        data = map(models.load_csv, self.data_file_paths)
        return list(data)


class JSONDataSource:
    def __init__(self, data_dir):
        self.data_dir = data_dir

    def get_data_files(self):
        self.data_file_paths = glob.glob(
            os.path.join(self.data_dir, "inflammation*.csv")
        )
        if len(self.data_file_paths) == 0:
            raise ValueError(
                f"No inflammation csv's found in path {self.data_file_paths}"
            )
        data = map(models.load_json, self.data_file_paths)
        return list(data)


def compute_standard_deviation_by_day(data):
    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)
    return daily_standard_deviation


# def get_data_files(data_dir):
#     data_file_paths = glob.glob(os.path.join(data_dir, 'inflammation*.csv'))
#     if len(data_file_paths) == 0:
#         raise ValueError(f"No inflammation csv's found in path {data_dir}")
#     data = map(models.load_csv, data_file_paths)
#     return list(data)


def analyse_data(data_source):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    data = data_source.get_data_files()
    daily_standard_deviation = compute_standard_deviation_by_day(data)
    print(daily_standard_deviation)

    # graph_data = {
    #     'standard deviation by day': daily_standard_deviation,
    # }
    # views.visualize(graph_data)

    return daily_standard_deviation
