#!/bin/bash

# Check if Python is installed and the version is 3.6 or higher
if ! command -v python3 &>/dev/null || ! python3 -c "import sys; assert sys.version_info >= (3, 6)" 2>/dev/null; then
    echo "Python 3.6 or higher is required. Please install or update Python."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &>/dev/null; then
    echo "pip3 is required. Please install pip3."
    exit 1
fi

# Install required Python packages
pip3 install -r requirements.txt

# Create an alias or symlink for the ai-git-commit command
if [[ "$SHELL" == *"bash"* ]]; then
    echo "alias ai-git-commit='python3 $(pwd)/ai_git_commit/main.py'" >> ~/.bashrc
    source ~/.bashrc
elif [[ "$SHELL" == *"zsh"* ]]; then
    echo "alias ai-git-commit='python3 $(pwd)/ai_git_commit/main.py'" >> ~/.zshrc
    source ~/.zshrc
else
    echo "Unsupported shell. Please manually create an alias or symlink for ai-git-commit."
fi

echo "Installation complete. Make sure to set the OPENAI_API_KEY environment variable."
