# InputValid-python-unsecure - Python Flask Vulnerable Build (Improper Input Validation)

This repository houses a specific application build that is part of a larger comparative study, "Evaluating the Effectiveness of Secure Coding Practices Across Python, MERN, and .NET 8." The experiment systematically assesses how secure coding techniques mitigate critical web application vulnerabilities—specifically improper input validation, insecure secrets management, and insecure error handling—across these three diverse development stacks. Through the development of paired vulnerable and secure application versions, this study aims to provide empirical evidence on the practical effectiveness of various security controls and the impact of architectural differences on developer effort and overall security posture.

## Purpose
This particular build contains the **Vulnerable Build** of the Python Flask application, specifically designed to demonstrate **Improper Input Validation**.

## Vulnerability Focus
This application build explicitly demonstrates:
* **Improper Input Validation:** The application fails to adequately check, filter, or sanitize user-supplied input, making it vulnerable to various attacks that leverage malformed or malicious data.

## Description of Vulnerability in this Build
In this version, the `/signup` endpoint processes user input without performing **any server-side input validation**. This means that:
* Required fields can be left empty.
* Strings of excessive length can be submitted.
* Invalid data formats (e.g., malformed emails, phone numbers) are accepted.
* Inputs potentially containing malicious characters (e.g., script tags for XSS, SQL injection payloads) are processed directly and acknowledged as "received".
This complete lack of validation creates direct avenues for attackers to exploit the application, potentially leading to data corruption, unauthorized access, or other system compromises.

## Setup and Running the Application

### Prerequisites
* Python 3.x
* `pip` (Python package installer)
* `Flask` and `Flask-CORS` Python packages.

### Steps
1.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    # Navigate to the specific build folder, e.g.:
    cd InputValid-dotnet-secure/python/vulnerable-input-validation # Example subfolder for this specific build
    ```
2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```
3.  **Install dependencies:**
    ```bash
    pip install Flask Flask-Cors
    ```
4.  **Run the application:**
    ```bash
    python server.py
    ```
    The application will typically start on `http://127.0.0.1:5002`.

## API Endpoints

### `POST /signup`
* **Purpose:** Handles user registration requests. In this vulnerable build, it processes input without any server-side validation.
* **Method:** `POST`
* **Content-Type:** `application/json`
* **Request Body Example (JSON):**
    ```json
    {
      "username": "",  // Will be accepted
      "email": "malicious<script>alert(1)</script>", // Will be accepted
      "phoneNumber": "abc", // Will be accepted
      "password": "1", // Will be accepted
      "confirmPassword": "1" // Will be accepted
    }
    ```
* **Expected Behavior:**
    * **Any Input (valid or invalid):** Returns `200 OK` with a message like "Sign-up data received (unvalidated)!".
        * Backend console will show logs indicating `--- RECEIVED UNSECURE SIGN-UP DATA ---` and the raw, unvalidated input.

## Static Analysis Tooling
This specific build is designed to be analyzed by Static Analysis Security Testing (SAST) tools such as Semgrep and Python's Bandit to measure their detection capabilities for the specific **input validation vulnerabilities** present in this build.
