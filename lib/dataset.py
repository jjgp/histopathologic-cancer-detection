import os

import cv2
import numpy as np
import pandas as pd


def rgb_imread(filepath):
    bgr_image = cv2.imread(filepath)
    return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)


class Dataset(object):
    def __init__(self, data_dirpath, csv_filename, images_dirname, npy_filename):
        self.csv_filepath = os.path.join(data_dirpath, csv_filename)
        self.images_dirpath = os.path.join(data_dirpath, images_dirname)
        self.npy_filepath = os.path.join(data_dirpath, npy_filename)

    def image_path(self, id):
        return os.path.join(self.images_dirpath, id + ".tif")

    def read_csv(self):
        return pd.read_csv(self.csv_filepath, index_col="id")

    def read_image(self, id):
        return rgb_imread(self.image_path(id))

    def read_images_and_labels(self, labels_df):
        images = None
        if os.path.exists(self.npy_filepath):
            images = np.load(self.npy_filepath, allow_pickle=True)
        else:
            values = labels_df.index.to_numpy()
            images = np.array(list(map(self.read_image, values)))
            np.save(self.npy_filepath, images)
        labels = labels_df["label"].to_numpy()
        return images, labels


class TrainDataset(Dataset):
    def __init__(self, data_dirname):
        super().__init__(data_dirname, "train_labels.csv", "train", "train.npy")


class TestDataset(Dataset):
    def __init__(self, data_dirname):
        super().__init__(data_dirname, "sample_submission.csv", "test", "test.npy")
