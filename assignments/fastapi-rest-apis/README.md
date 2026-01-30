# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern REST APIs using the FastAPI framework. You will create a fully functional API with routes, request validation, and error handling, understanding how to structure and deploy web services in Python.

## 📝 Tasks

### 🛠️ Set Up FastAPI Project and Create Basic Routes

#### Description
Set up a FastAPI project environment and create the foundational API structure with basic GET and POST routes. Install FastAPI and Uvicorn, then create an API server with health check and user management endpoints.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn via pip
- Create a main API file with a FastAPI application instance
- Implement a GET `/health` endpoint that returns a status message
- Implement a POST `/users` endpoint that accepts a user object with name and email
- Return appropriate JSON responses with status codes
- Run the server on localhost:8000 using Uvicorn

---

### 🛠️ Implement Data Models and Request Validation

#### Description
Define Pydantic models for data validation and create additional endpoints that demonstrate type checking and error handling. Create models for users and products, then implement CRUD operations with proper validation.

#### Requirements
Completed program should:

- Define a `User` Pydantic model with fields: id, name, email, and age
- Define a `Product` Pydantic model with fields: id, name, price, and description
- Implement a GET `/users/{user_id}` endpoint to retrieve a specific user
- Implement a GET `/products` endpoint that returns a list of products
- Return 404 errors for non-existent resources
- Validate that email format is correct and price is a positive number
- Include descriptive error messages in responses

---

### 🛠️ Add Query Parameters and Error Handling

#### Description
Enhance the API by implementing query parameters for filtering and pagination, and add comprehensive error handling for different scenarios.

#### Requirements
Completed program should:

- Implement a GET `/products` endpoint with optional query parameters for filtering (e.g., `min_price` and `max_price`)
- Add pagination support with `skip` and `limit` query parameters
- Implement proper HTTP status codes (200, 201, 400, 404, 500)
- Add custom error responses with meaningful messages
- Include request/response examples in endpoint documentation
- Test all endpoints using the automatic interactive API documentation at `/docs`
