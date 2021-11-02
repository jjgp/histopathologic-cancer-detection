# Histopathologic Cancer Detection

This project applies learnings from the [FourthBrain Machine Learning Engineering cirriculum](https://www.fourthbrain.ai/machine-learning-engineer)
to a previous Kaggle competition. The competition involves identifiying metastic cancer
from images. Vist the [overview](https://www.kaggle.com/c/histopathologic-cancer-detection/overview)
page on Kaggle to see the competition details.

## Getting Started

### Installing dependencies

If installing on a Mac with an M1 processor, you can should follow the instructions to
use the [tensorflow-metal PluggableDevice](https://developer.apple.com/metal/tensorflow-plugin/)
for accelerated training. It does require using macOS Monterey and Miniforge. Given the
advice from the Apple developer docs, use the following command to create the `conda`
environment:

```
conda env create -f enrivonment.m1.yml
```

If using another processor or OS then simply create the `conda` environment with:

```
conda env create -f enrivonment.yml
```

### Using `pre-commit`

...Need to add tidbit of how to use pre-commit

- https://github.com/jjgp/hiring-manager/blob/main/.pre-commit-config.yaml
- https://pre-commit.com/

### Downloading dataset

The `kaggle` CLI is installed with the `conda` environment. To download the dataset,
make sure to first obtain the [API credentials](https://github.com/Kaggle/kaggle-api#api-credentials).
A VS Code task is available to download the dataset.

### Tensorflow Plugin - Metal

[Getting Started with tensorflow-metal PluggableDevice](https://developer.apple.com/metal/tensorflow-plugin/)

### Working with VS Code

- https://code.visualstudio.com/docs/python/environments
- https://medium.com/analytics-vidhya/efficient-way-to-activate-conda-in-vscode-ef21c4c231f2
- https://medium.com/@udiyosovzon/how-to-activate-conda-environment-in-vs-code-ce599497f20d
- https://github.com/microsoft/vscode-dev-containers
