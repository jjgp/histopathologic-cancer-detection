#!/usr/bin/env bash

envs_hcd_kaggle_path () {
    echo "$(conda info --envs | sed 's/*//' | tr -s ' ' | cut -d ' ' -f2 | grep "envs/hcd$")/bin/kaggle"
}

# Check if kaggle is available in PATH. If not, check the hcd conda environment.
KAGGLE_PATH="$(which kaggle)"
KAGGLE_PATH="${KAGGLE_PATH:-$(envs_hcd_kaggle_path)}"

if [ ! -x "$KAGGLE_PATH" ]; then
    echo "Kaggle CLI not found."
    exit
fi

$KAGGLE_PATH competitions download -c histopathologic-cancer-detection -p data/
