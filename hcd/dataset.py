import os

import cv2
import pandas as pd


def rgb_imread(filepath):
    bgr_image = cv2.imread(filepath)
    return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)


class Dataset(object):
    def __init__(self, data_dirpath, csv_filename, images_dirname):
        self.csv_filepath = os.path.join(data_dirpath, csv_filename)
        self.images_dirpath = os.path.join(data_dirpath, images_dirname)

    def read_csv(self):
        return pd.read_csv(self.csv_filepath)

    def image_path(self, id):
        return os.path.join(self.images_dirpath, id + ".tif")

    def read_images_and_labels(self, labels_df):
        image_paths = labels_df["id"].map(self.image_path)
        images = image_paths.map(rgb_imread).to_numpy()
        labels = labels_df["label"].to_numpy()
        return images, labels


class TrainDataset(Dataset):
    def __init__(self, data_dirname):
        super().__init__(data_dirname, "train_labels.csv", "train")


class TestDataset(Dataset):
    def __init__(self, data_dirname):
        super().__init__(data_dirname, "sample_submission.csv", "test")
