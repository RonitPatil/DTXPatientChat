
# DTXPatientChat

Welcome to the DTXPatientChat GitHub repository. This guide will walk you through setting up the project locally and give a brief description of the app.

## Prerequisites

Before you proceed, ensure that you have the following installed on your system:
- [Git](https://git-scm.com/downloads)
- [Anaconda](https://www.anaconda.com/products/individual) or [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
- [OpenAI API Key](https://beta.openai.com/signup/): Sign up at OpenAI and obtain your API key. Once you have the key, find the `.env` file in the `patientbot` directory and add the following line to it:
  
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

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Run the Development server

```bash
python manage.py runserver
```
## Project Description

**DTXPatientChat** is a Django-based healthcare chatbot system built specifically to serve a single patient. The chatbot is designed to assist the patient in managing their healthcare needs by leveraging two distinct agents:

### Appointment Intent Detection Agent
This agent monitors patient interactions to detect if the user is requesting to schedule, reschedule, or cancel an appointment. If an appointment request is identified, the system proceeds to handle the scheduling accordingly. If no appointment intent is detected, the conversation is passed to the second agent.

### Medical Agent
If the user is not asking about appointments, this agent steps in to handle general healthcare queries. It provides information related to the patient's health conditions, medications, and offers appropriate feedback. Additionally, every 7 messages, the system generates a summary of the conversation to maintain contextual awareness, ensuring that the chatbot retains key details from prior interactions.

The bot is highly specialized, answering only healthcare-related questions and avoiding any irrelevant topics. It also offers personalized criticism on dietary habits based on the patient's medical conditions, making the conversation highly relevant and tailored to the patient's health.




