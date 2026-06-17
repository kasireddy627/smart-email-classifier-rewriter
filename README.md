# Smart Email Classifier & Rewriter

## Live Demo

### Frontend Application

https://kasireddy627.github.io/smart-email-classifier-rewriter/

### Backend API

https://smart-email-classifier-rewriter-0i9f.onrender.com

### FastAPI Interactive API Documentation

https://smart-email-classifier-rewriter-0i9f.onrender.com/docs

## Overview of the project

Smart Email Classifier & Rewriter is a Generative AI application built using FastAPI, LangChain, and Groq.

The application performs two core tasks:

1. **Email Classification**

   * Categorizes emails into:

     * Work
     * Personal
     * Finance
     * Spam

2. **Email Rewriting**

   * Rewrites email content in different tones such as:

     * Professional
     * Friendly
     * Formal
     * Polite

The project demonstrates FastAPI integration, prompt engineering, LLM integration, and a simple frontend built using HTML, CSS, and JavaScript.

---

## Features

### Email Classification

* Accepts raw email content
* Uses an LLM to classify emails
* Returns one of the following categories:

  * Work
  * Personal
  * Finance
  * Spam

### Email Rewriting

* Accepts email content and a selected tone
* Uses an LLM to rewrite the email
* Preserves the original meaning while adjusting the tone

---

## Tech Stack

### Backend

* Python
* FastAPI
* LangChain
* Groq LLM
* Pydantic

### Frontend

* HTML
* CSS
* JavaScript

---

## Project Structure

```text
SMART_EMAIL_CLASSIFIER/

│
├── backend/
│   ├── prompts/
│   │   ├── classify_prompt.txt
│   │   └── rewrite_prompt.txt
│   │
│   ├── schemas/
│   │   └── request_models.py
│   │
│   ├── services/
│   │   ├── classifier_service.py
│   │   ├── rewriter_service.py
│   │   └── llm_service.py
│   │
│   ├── utils/
│   │   └── config.py
│   │
│   ├── main.py
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/kasireddy627/smart-email-classifier-rewriter
cd SMART_EMAIL_CLASSIFIER
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux / Mac:

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the `backend` folder.

Example:

```env
GROQ_API_KEY=your_groq_api_key
```

---

## Running the Application

Navigate to the backend folder:

```bash
cd backend
```

Start FastAPI:

```bash
uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### 1. Classify Email

**Endpoint**

```http
POST /classify_email
```

**Request**

```json
{
  "email": "Please submit your weekly report by Friday."
}
```

**Response**

```json
{
  "received_email": "Please submit your weekly report by Friday.",
  "category": "Work"
}
```

---

### 2. Rewrite Email

**Endpoint**

```http
POST /rewrite_email
```

**Request**

```json
{
  "email": "Send me the report.",
  "tone": "professional"
}
```

**Response**

```json
{
  "rewritten_email": "Please forward the report to me at your earliest convenience."
}
```

---

## Frontend

The application includes a simple user interface built using:

* HTML
* CSS
* JavaScript

Features:

* Email Classification Panel
* Email Rewriting Panel
* Tone Selection Dropdown
* Real-time API Integration with FastAPI

---

## Prompt Engineering

Two dedicated prompt templates are used:

### Classification Prompt

Guides the LLM to classify emails into predefined categories while returning only the category name.

### Rewrite Prompt

Guides the LLM to rewrite emails in a specified tone while preserving the original meaning and avoiding unnecessary additions.

---

## Future Improvements

* Docker Support
* Additional Email Categories
* Authentication
* Response Logging
* Multiple LLM Provider Support

---

## Author

AI Engineer Internship Assessment Submission

Built using FastAPI, LangChain, Groq, HTML, CSS, and JavaScript.