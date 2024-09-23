
# DTXPatientChat

Welcome to the DTXPatientChat GitHub repository. This guide will walk you through setting up the project locally.

## Prerequisites

Before you proceed, ensure that you have the following installed on your system:
- [Git](https://git-scm.com/downloads)
- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [OpenAI API Key](https://beta.openai.com/signup/): Sign up at OpenAI and obtain your API key. Once you have the key, find the `.env` file in the `healthbot` directory and add the following line to it:
  
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Installation

Follow these steps to get your development environment set up:

### 1. Clone the Repository

First, you need to clone this repository to your local machine:

```bash
git clone https://github.com/RonitPatil/DTXPatientChat.git
cd DTXPatientChat
```

### 2. Navigate to the healthbot directory

```bash
cd healthbot
```

### 3. Create and Activate the Conda Environment

```bash
conda create --name dtx_env
conda activate dtx_env
```

### 4. Install Dependencies from requirements.txt

```bash
pip install -r requirements.txt
```

### 5. Run the Development server

```bash
python manage.py runserver
```




