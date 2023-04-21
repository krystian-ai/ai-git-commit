@echo off

rem Check if Python is installed and the version is 3.6 or higher
where python >nul 2>nul || (
    echo Python 3.6 or higher is required. Please install or update Python.
    exit /b 1
)

python -c "import sys; assert sys.version_info >= (3, 6)" >nul 2>nul || (
    echo Python 3.6 or higher is required. Please install or update Python.
    exit /b 1
)

rem Check if pip is installed
where pip >nul 2>nul || (
    echo pip is required. Please install pip.
    exit /b 1
)

rem Install required Python packages
pip install -r requirements.txt

rem Create an alias or symlink for the ai-git-commit command
echo @echo off > ai-git-commit.bat
echo python "%cd%\main.py" %%* >> ai-git-commit.bat
move ai-git-commit.bat %USERPROFILE%\AppData\Local\Microsoft\WindowsApps /Y >nul

echo Installation complete. Make sure to set the OPENAI_API_KEY environment variable.
