# Grocy Chores Notifier

## Overview

The **Grocy Chores Notifier** is a Python application that connects to the [Grocy API](https://grocy.info/) to retrieve and notify users about chores due in the next 7 days. Notifications are sent using [Pushover](https://pushover.net/), allowing users to receive updates on their mobile devices or desktop.

This project uses:
- **Python 3.11.10**
- **Conda** (via Miniforge) for environment management
- `python-dotenv` for environment variable management
- `requests` for API requests

## Features
- Fetches chores from the Grocy API.
- Notifies users about upcoming chores for the next 7 days.
- Sends Pushover notifications for both "no chores due" and a formatted list of due chores.

---

## Requirements

- **Python**: Version 3.11.10
- **Conda**: Installed via Miniforge or Anaconda (recommended for dependency management).
- **Pushover Account**: Required to receive notifications.
- **Grocy API**: Access to a running Grocy instance with API enabled.

---

## Installation and Setup

### Clone the Repository
```bash
git clone https://github.com/your-username/grocy-chores-notifier.git
cd grocy-chores-notifier
```

### Configure Environment Variables

Create a .env file in the project directory and define the following variables:

```bash
GROCY_BASEURL=https://your-grocy-instance.com
GROCY_APIKEY=your_grocy_api_key
PUSHOVER_USERKEY=your_pushover_user_key
PUSHOVER_APPKEY=your_pushover_app_key
```

---

# Setting Up the Environment

You can set up the project environment using either Conda or pip.

## Option 1: Using Conda

1. Ensure Miniforge or Anaconda is installed.

2. Use the provided environment.yml file to create the environment:

    ```bash
    conda env create -f environment.yml
    ```

3. Activate the environment:

    ```bash
    conda activate grocy-chores-notifier
    ```

## Option 2: Using pip

1. Ensure you have Python 3.11.10 installed.

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows
    ```

3. Install dependencies using requirements.txt:

    ```bash
    pip install -r requirements.txt
    ```

---

# Running the Project

Once the environment is set up:

1. Activate the environment (if not already activated):
    - **Conda**: `conda activate grocy-chores-notifier`
    - **pip**: `source venv/bin/activate` (Linux/Mac) or `venv\Scripts\activate `(Windows)

2. Run the main script:

    ```bash
    python notify.py
    ```

---

# Project Structure

```bash
grocy-chores-notifier/
├── notify.py         # Main script
├── pushover.py       # Handles Pushover notifications
├── grocyapi.py       # Interacts with the Grocy API
├── config.py         # Loads environment variables
├── environment.yml   # Conda environment configuration
├── requirements.txt  # Python dependencies for pip users
└── README.md         # Project documentation
```

---

# Troubleshooting

## Common Issues

1. Environment Variables Not Loaded:
    - Ensure .env file exists and contains all required variables.
    - Confirm the dotenv library is installed.

2. Python Version Mismatch:
    - Check your Python version with python --version.
    - Ensure it matches 3.11.10.

## Updating Dependencies

If new dependencies are added:

1. For Conda:

    ```bash
    conda env export > environment.yml
    ```

2. For pip:

    ```bash
    pip freeze > requirements.txt
    ```

---

## License

This project is licensed under the MIT License.