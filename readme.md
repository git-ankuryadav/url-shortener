# Flask URL Shortener

A simple URL shortener built using **Python, Flask, and SQLite**. It converts long URLs into short, shareable links and redirects users to the original destination.

## Features

- Shorten long URLs using randomly generated 6-character codes.
- Redirect short links to their original URLs.
- Store shortened URLs persistently using SQLite.
- Prevent duplicate short codes using database constraints.
- Handle invalid or nonexistent short links with a 404 response.
- Automatically create the database and table when the application starts.

## Tech Stack

- **Python 3.12+** — Core programming language
- **Flask** — Web framework
- **SQLite** — Database
- **HTML** — Basic user interface

## Project Structure

```text
url-shortener/
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `urls.db` database file is generated automatically when the application runs.

## Getting Started

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd url-shortener
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it on macOS or Linux:

```bash
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python3 app.py
```

Open the following address in your browser:

http://127.0.0.1:5000/

## How It Works

1. The user enters a long URL into the form.
2. Flask receives the URL through a POST request.
3. The application generates a random short code.
4. SQLite stores the short code and original URL.
5. Flask displays the generated short link.
6. When someone visits that link, Flask retrieves the original URL and redirects the browser.

## Database Design

The application uses a SQLite table named `urls`.

| Column         | Description                           |
| -------------- | ------------------------------------- |
| `id`           | Auto-incrementing primary key         |
| `short_code`   | Unique code used in the shortened URL |
| `original_url` | Original destination URL              |

The `UNIQUE` constraint prevents two records from having the same short code. If a collision occurs, the application generates another code.

## API Routes

| Method | Route      | Purpose                         |
| ------ | ---------- | ------------------------------- |
| GET    | `/`        | Display the URL shortening form |
| POST   | `/shorten` | Generate and save a short URL   |
| GET    | `/<code>`  | Redirect to the original URL    |

## Learning Outcomes

This project demonstrates practical use of:

- Flask routing and HTTP methods
- HTML forms and request handling
- Python functions and random code generation
- SQLite database connections and SQL queries
- Database constraints and exception handling
- HTTP redirects and 404 responses
- Python virtual environments and dependency management

## Future Improvements

- Add HTML templates and CSS for a better interface.
- Allow users to choose custom short codes.
- Track link clicks and display analytics.
- Add URL validation and safer error handling.
- Prevent unnecessary duplicate URL records.
- Add automated tests using `pytest`.
- Deploy the application online.

## Note

This project is intended for learning and experimentation. It currently uses Flask's development server and should be hardened before production deployment.

## License

This project is open source and available under the MIT License, if you choose to include one.
