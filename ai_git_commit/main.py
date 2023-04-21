import os
import subprocess
from openai_api import generate_commit_message
from utils import get_git_diff, get_user_input, get_user_confirmation

def main():
    git_diff = get_git_diff()

    if not git_diff:
        print("No changes detected. Exiting...")
        return

    commit_message = generate_commit_message(git_diff)
    print(f"Suggested commit message: {commit_message}")

    while True:
        user_response = get_user_confirmation("Accept this commit message? (yes/no/edit): ")

        if user_response is True:
            break
        elif user_response is False:
            commit_message = get_user_input("Enter your commit message: ")
            break
        elif user_response.lower() == "edit":
            commit_message = get_user_input("Edit the commit message: ")
            break

    subprocess.run(["git", "commit", "-m", commit_message])
    print(f"Commit successful with message: {commit_message}")

if __name__ == "__main__":
    main()
