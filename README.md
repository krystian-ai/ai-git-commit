# AI-Git-Commit

AI-Git-Commit is a program that uses the Git Diff command to read code changes in the current folder repository and leverages the OpenAI API to generate a commit message. The program will ask the user to accept or edit the commit message before executing the Git commit with the generated message. AI-Git-Commit is designed to be easily accessible, using environment variables for settings and being available from any path in the system.

## Features
- Analyzes code changes in the current repository using git diff
- Utilizes OpenAI API to generate intelligent commit messages
- Asks user to accept or edit the commit message before proceeding
- Uses environment variables for configuration
- Available from any path in the system
- Includes installer script for easy setup

## Prerequisites
- Git installed on your system
- Python 3.6 or higher
- OpenAI API Key

## Installation
1. Clone this repository to your local machine:

```bash
git clone https://github.com/krystian-ai/ai-git-commit.git
cd ai-git-commit
```

2. Run the installer script:

```bash
./install.sh
```

This will:

- Install required Python dependencies
- Set up an alias or symlink for the ai-git-commit command
- Guide you through setting up environment variables

3. Make sure to add your OpenAI API key to your environment variables:

```arduino
export OPENAI_API_KEY='your_openai_api_key'
```

We recommend adding the above line to your `.bashrc`, '.zshrc', or equivalent shell configuration file for persistence.

## Usage
To use the AI-Git-Commit program, navigate to your Git repository and run:

```sql
ai-git-commit
```

The program will analyze the code changes, generate a commit message, and ask for your confirmation. You can either accept the message or edit it. After confirming the commit message, the program will execute the Git commit with the provided message.

## Contributing
Pull requests are welcome! If you have any issues, please open an issue on the GitHub repository.

## License
This project is licensed under the MIT License. See the [LICENSE](url) file for details.

## Author
[krystian-ai](https://github.com/krystian-ai)
