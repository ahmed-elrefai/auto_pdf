# 📄 Auto PDF

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Auto PDF** is a high-reliability automation tool designed to eliminate repetitive office tasks. It transforms raw data from CSV files into polished, professional PDF reports using custom HTML templates.

---

## 🚀 Features
* **Bulk Generation:** Processes X rows of data into X individual PDFs in seconds.
* **HTML Templating:** Full control over design using standard HTML/CSS.
* **Dynamic Placeholders:** Easily map CSV columns to PDF fields using `{{ placeholder }}` syntax.
* **Reliable Processing:** Built with error handling to ensure data integrity during generation.

## 🛠️ How It Works

The system maps headers from your `.csv` file directly to placeholders in your `.html` template.

### 1. Prepare your CSV
Ensure your CSV contains columns matching your template variables: `name`, `email`, `subject`, and `score`.

### 2. Create your Template
Design your report using standard HTML. Here is the supported format:

```html
<h1>Student Report</h1>
<p><strong>Name:</strong> {{ name }}</p>
<p><strong>Email:</strong> {{ email }}</p>
<p><strong>Subject:</strong> {{ subject }}</p>
<p><strong>Score:</strong> {{ score }}</p>
```

## 📸 Preview

<img width="1836" height="998" alt="image" src="https://github.com/user-attachments/assets/576de270-0674-404e-91ae-3e18fb171186" />


## 🏗️ System Architecture
As a backend-focused project, Auto PDF prioritizes:

Separation of Concerns: Decoupling data parsing from PDF rendering.

Resource Efficiency: Optimized for memory usage when handling large CSV files.

## 👨‍💻 Author
**Ahmed Elrefai**, Backend Developer & CS Student at Ain Shams University [LinkedIn](https://www.linkedin.com/ahmed-elrefai) | [YouTube](https://www.youtube.com/@ibnalrefai)
