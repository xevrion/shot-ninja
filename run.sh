#!/bin/bash

# Get the current user's Python path (not root's)
PYTHON_PATH=$(which python3)

# Run with sudo but use the user's Python
sudo "$PYTHON_PATH" main.py
