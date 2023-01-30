# rasa-bot

# Install Pyenv
```
brew install pyenv
```


# Install poetry
```
brew install poetry
```

# List Pyenv supported Python Versions
```
pyenv install --list
```

# Install Python Version
pyenv install  3.8.11

# See all python installations that you have installed.
pyenv versions

# Set the default/global from one of the python versions.
```
pyenv global 3.8.11
```

# In the current directory, set the python version. This creates the file .python-version.
```
pyenv local 3.8.11
```

# To see which python is currently being used.
```
pyenv version
```

# Install Poetry
```
pip3 install poetry
```

# For tab completion in your shell, see the documentation
```
poetry help completions
```

# Configure poetry to create virtual environments inside the project's root directory
```
poetry config virtualenvs.in-project true
```
# Install Packages 
```
poetry install -E full
```
# Issue Fix : Cannot switch Python version with pyenv
```
eval "$(pyenv init -)"
eval "$(pyenv init --path)"
```
update your ~/.bash_profile, ~/.zprofile, ~/.bashrc, ~/.zshrc or the like if necessary.

# NLTK & Spacy Download
```
import nltk
nltk.downloader.download('vader_lexicon')
python -m spacy download en_core_web_md
```

# Issue Fix : Cannot install Tokenizer Package [Apple Silicon Mac M1 Pro]

Python Version : 3.8.11
```
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```
