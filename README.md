# MJV Free Chat Template

MJV Free Chat Template is a Python-based application designed to provide advanced functionalities using OpenAI and Streamlit. This guide will help you set up, run, and deploy the application to Google Cloud Run.

## Prerequisites

- Python 3.8 or higher
- Docker
- Google Cloud SDK
- GitHub account (for Codespaces)

## Project Structure
├── agent.py
├── Dockerfile
├── LICENSE
├── main.py
├── requirements.txt
├── .gitignore


## Setup

1. **Clone the repository**:
   ```sh
   git clone <repository_url>
   cd <repository_directory>

## Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

## Install the dependencies:

Install the dependencies:

## Running the Application Locally
Start the Streamlit application:

```sh
streamlit run main.py

## Using GitHub Codespaces
GitHub Codespaces allows you to run and test the application in a cloud-based development environment. Here's how to set it up:

Open the repository on GitHub.

Create a Codespace:

Click on the Code button.
Select Open with Codespaces and create a new Codespace.
Set up the environment:

Once the Codespace is ready, open the terminal.
Run the following commands to install the dependencies and start the application:

```sh
pip install -r requirements.txt
streamlit run main.py


