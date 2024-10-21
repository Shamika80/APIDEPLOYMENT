# Sum API with PostgreSQL and Render Deployment

This Flask application provides a simple API for calculating sums and storing them in a PostgreSQL database. It also includes functionality to retrieve sums filtered by their results. The API is deployed on Render using GitHub Actions for continuous deployment.

## Features

*   `/sum` endpoint (POST): Calculates the sum of two numbers (`num1`, `num2`) provided in a JSON payload and stores the result in the database.
*   `/sum/result/<int:result_value>` endpoint (GET): Retrieves a list of sums from the database where the result matches the provided `result_value`.
*   Error handling for missing parameters and database interactions.
*   Unit tests to ensure functionality.
*   CI/CD pipeline using GitHub Actions to automate building, testing, and deploying to Render.

## Getting Started

### Prerequisites

*   Python 3.x
*   PostgreSQL database
*   Render account
*   GitHub account

### Installation

1.  Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2.  Create a virtual environment:
    ```bash
    python -m venv venv
    ```

3.  Activate the virtual environment:   

    ```bash
    # On Windows:
    venv\Scripts\activate

    # On macOS/Linux:
    source venv/bin/activate
    ```

4.  Install dependencies:
    ```bash
    pip install -r requirements.txt   

    ```

5.  Set up environment variables:
    *   Create a `.env` file in the root directory.
    *   Add your PostgreSQL connection string to the `DATABASE_URL` variable in the `.env` file:

        ```
        DATABASE_URL=postgresql://username:password@host:port/database_name
        ```

6.  Create the database table:
    *   Connect to your PostgreSQL database.
    *   Create a table named `sums` with the following schema:

        ```sql
        CREATE TABLE sums (
            id SERIAL PRIMARY KEY,
            num1 INTEGER NOT NULL,
            num2 INTEGER NOT NULL,
            result INTEGER NOT NULL
        );
        ```

### Running the App Locally

1.  Activate your virtual environment (if not already activated).
2.  Run the app:
    ```bash
    python app.py
    ```

### Deploying to Render

1.  Create a web service on Render and connect it to your GitHub repository.
2.  Set the build command to:

    ```bash
    pip install -r requirements.txt && gunicorn --worker-class gevent app:app
    ```

3.  Add your `DATABASE_URL` as an environment variable in the Render web service settings.
4.  Set up GitHub Actions secrets for `RENDER_SERVICE_ID` and `RENDER_API_KEY`.
5.  Push your changes to the `master` branch to trigger the deployment.

## Usage

### `/sum` Endpoint

*   **Method:** POST
*   **Request Body (JSON):**
    ```json
    {
        "num1": 5,
        "num2": 3
    }
    ```
*   **Response Body (JSON):**
    ```json
    {
        "result": 8
    }
    ```

### `/sum/result/<int:result_value>` Endpoint

*   **Method:** GET
*   **Example URL:** `/sum/result/8`
*   **Response Body (JSON):**
    ```json
    [
        { "num1": 5, "num2": 3 },
        { "num1": 1, "num2": 7 }
    ]
    ```







