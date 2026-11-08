# 🎭 Rangmanch Review API

A simple **FastAPI-based Review API** built as a learning project to practice backend development, CRUD operations, SQLite database integration, SQLModel, request validation, and REST API design.

The project allows users to create, view, update, and delete reviews for plays or performances.

## 🚀 Features

- Create a new review
- Get all reviews
- Pagination using `skip` and `limit`
- Get a review by ID
- Get reviews by play name
- Update an existing review using PATCH
- Delete a review
- Request validation using SQLModel/Pydantic
- Rating validation from **1 to 5**
- SQLite database
- SQLModel for database models and operations
- Automatic `create_at` timestamp using UTC
- Interactive API documentation with Swagger UI
- Run the application using Uvicorn

## 🛠️ Tech Stack

- **Python**
- **FastAPI**
- **SQLModel**
- **SQLite**
- **Pydantic**
- **Uvicorn**

## 📁 Project Structure

```text
rangmanch_review/
│
├── reviews/
│   └── routes.py
│
├── venv/
├── __pycache__/
├── .gitignore
├── database.py
├── main.py
├── models.py
├── requirements.txt
├── README.md
└── rangmanch.db
```

> `rangmanch.db` is the local SQLite database file and should not be committed to Git.

## 🗄️ Database

This project uses **SQLite** as the database.

SQLite is a lightweight relational database that stores the database in a local file instead of requiring a separate database server.

The project uses **SQLModel** to define database models and interact with SQLite.

The main review model contains the following fields:

| Field           | Type       | Description                          |
| --------------- | ---------- | ------------------------------------ |
| `id`            | `int`      | Primary key, automatically generated |
| `play_name`     | `str`      | Name of the play/performance         |
| `reviewer_name` | `str`      | Name of the reviewer                 |
| `rating`        | `int`      | Review rating from 1 to 5            |
| `comment`       | `str`      | Review comment                       |
| `create_at`     | `datetime` | Review creation time in UTC          |

Example SQLModel definition:

```python
class Review(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    play_name: str = Field(index=True)
    reviewer_name: str
    rating: int = Field(ge=1, le=5)
    comment: str
    create_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
```

## 🔌 API Endpoints

### 1. Root Endpoint

```http
GET /
```

Returns a basic response from the API.

---

### 2. Create Review

```http
POST /api/v1/review/
```

Creates a new review.

Example request:

```json
{
  "play_name": "Rangmanch",
  "reviewer_name": "Adarsh",
  "rating": 5,
  "comment": "Excellent performance!"
}
```

The `id` and `create_at` values are generated automatically.

---

### 3. Get Reviews

```http
GET /api/v1/review/
```

Returns the list of reviews.

Pagination can be applied using `skip` and `limit`:

```http
GET /api/v1/review/?skip=0&limit=10
```

Example:

```text
skip=0
limit=10
```

means:

> Start from the first record and return up to 10 reviews.

---

### 4. Get Review by ID

```http
GET /api/v1/review/{id}
```

Example:

```http
GET /api/v1/review/1
```

Returns the review with the specified ID.

---

### 5. Get Review by Play Name

```http
GET /api/v1/review/{play_name}
```

Example:

```http
GET /api/v1/review/Rangmanch
```

Returns review information based on the play name.

---

### 6. Update Review

```http
PATCH /api/v1/review/{id}
```

Updates an existing review.

Example:

```http
PATCH /api/v1/review/1
```

Example request:

```json
{
  "rating": 4,
  "comment": "Good performance and presentation."
}
```

---

### 7. Delete Review

```http
DELETE /api/v1/review/{id}
```

Example:

```http
DELETE /api/v1/review/1
```

Deletes the review with the specified ID.

---

## ✅ Validation

The project uses **SQLModel/Pydantic validation** for request data.

The `rating` field only accepts values between **1 and 5**:

```python
rating: int = Field(ge=1, le=5)
```

Therefore:

```text
1 → Valid
3 → Valid
5 → Valid
0 → Invalid
6 → Invalid
```

The API returns an HTTP validation error when invalid data is submitted.

## ⏰ Created At

Each review automatically receives a creation timestamp.

The project uses a timezone-aware UTC datetime:

```python
datetime.now(timezone.utc)
```

This ensures that the stored timestamp contains timezone information.

## ▶️ Running the Project

### 1. Clone the repository

```bash
git clone https://github.com/dube-codes/rangmanch_review.git
```

### 2. Go to the project directory

```bash
cd rangmanch_review
```

### 3. Create a virtual environment

Windows:

```powershell
python -m venv venv
```

### 4. Activate the virtual environment

```powershell
.\venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

### 6. Run the FastAPI application

```powershell
uvicorn main:app --reload
```

The application will run at:

```text
http://127.0.0.1:8000
```

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

Swagger UI can be used to test the CRUD APIs directly from the browser.

## 🔄 CRUD Operations

The project implements the complete CRUD flow:

```text
Create → POST
Read   → GET
Update → PATCH
Delete → DELETE
```

Example flow:

```text
POST /api/v1/review/
        ↓
   Create Review
        ↓
     SQLite
        ↓
GET /api/v1/review/
        ↓
   Read Reviews
        ↓
PATCH /api/v1/review/{id}
        ↓
   Update Review
        ↓
DELETE /api/v1/review/{id}
        ↓
   Delete Review
```

## 🎯 What I Learned

Through this project, I practiced:

- Building REST APIs using FastAPI
- Implementing CRUD operations
- Working with SQLite
- Using SQLModel for database models
- Connecting FastAPI with a database
- Using Pydantic/SQLModel validation
- Implementing pagination with `skip` and `limit`
- Working with PATCH requests for partial updates
- Handling database records using IDs and indexed fields
- Working with timezone-aware datetime values
- Running FastAPI applications using Uvicorn
- Testing APIs using Swagger UI
- Managing the project with Git and GitHub

## 🔮 Future Improvements

Possible improvements for future versions:

- Add authentication and authorization
- Add user accounts
- Add proper user-review relationships
- Add automated tests
- Add database migrations
- Add search and filtering
- Add PostgreSQL support
- Add deployment configuration
- Improve error handling and API response structure

## 📌 Project Status

This is a **learning project** created to practice FastAPI, SQLModel, SQLite, and REST API development.

The current version focuses on review CRUD operations and uses SQLite for local data storage.
