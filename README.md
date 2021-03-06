# Histopathologic Cancer Detection

This project applies learnings from the [FourthBrain Machine Learning Engineering cirriculum](https://www.fourthbrain.ai/machine-learning-engineer)
to a previous Kaggle competition. The competition involves identifiying metastic cancer
from images. Vist the [overview](https://www.kaggle.com/c/histopathologic-cancer-detection/overview)
page on Kaggle to see the competition details.

## Getting Started

### Installing dependencies

If installing on a Mac with an M1 processor, you should follow the instructions to use
the [tensorflow-metal PluggableDevice](https://developer.apple.com/metal/tensorflow-plugin/)
for accelerated training. It does require using macOS Monterey and [Miniforge](https://github.com/conda-forge/miniforge).
Given the prerequisites listed in the Apple developer docs, use the following command
to create the `conda` environment:

```
conda env create -f enrivonment.m1.yml
```

If using another processor or OS then simply create the `conda` environment with:

```
conda env create -f enrivonment.yml
```

The project does have a [`.devcontainer`](https://code.visualstudio.com/docs/remote/containers)
setup they may be used to run the project in a dockerized environment or on [GitHub Codespaces](https://github.com/features/codespaces).

### Downloading the dataset

The `kaggle` CLI is installed with the `conda` environment. To download the dataset,
make sure to first obtain [API credentials](https://github.com/Kaggle/kaggle-api#api-credentials).
A VS Code task is available to download the dataset.

### Using `pre-commit`

This project uses the [pre-commit](https://pre-commit.com/) to automate tedium and
enforce code quality standards. The `pre-commit` dependency is available in the `conda`
environments. To install the `pre-commit` git hook run:

```
pre-commit install
```

It may be useful to run `pre-commit` outside of a `git` hook. To do so run read up on
the usage:

```
pre-commit run --help
```

### Unit testing

The `conda` environments include [`pytest`](https://docs.pytest.org/en/6.2.x/contents.html#)
and [`testbook`](https://testbook.readthedocs.io/en/latest/index.html). This allows for
the unit testing of notebooks in addition to python modules. The tests may also be ran
by simply using `pytest` or the VS Code UI.
