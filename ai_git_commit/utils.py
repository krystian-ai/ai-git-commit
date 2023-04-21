import sys
import subprocess

def get_git_diff():
    """
    Get the Git diff for the current repository.

    :return: A string containing the Git diff.
    """
    if sys.platform == "win32":
        # On Windows, use shell=True for subprocess.run()
        result = subprocess.run(["git", "diff","--cached"], capture_output=True, text=True, shell=True)
    else:
        result = subprocess.run(["git", "diff","--cached"], capture_output=True, text=True)
    return result.stdout

def get_user_input(prompt):
    """
    Get user input with the given prompt.

    :param prompt: The prompt to display to the user.
    :return: The user's input as a string.
    """
    return input(prompt)

def get_user_confirmation(prompt):
    """
    Get user confirmation (yes/no) with the given prompt.

    :param prompt: The prompt to display to the user.
    :return: True if the user confirms, False otherwise.
    """
    while True:
        response = input(prompt).lower()
        if response in ["y", "yes"]:
            return True
        elif response in ["n", "no"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.")
