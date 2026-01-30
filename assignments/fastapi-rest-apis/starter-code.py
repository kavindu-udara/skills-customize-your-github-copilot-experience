"""
FastAPI REST API Starter Code
Complete this assignment by building out the API with the required endpoints and models.
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Create a FastAPI application instance
app = FastAPI(
    title="Student Management API",
    description="A REST API for managing students and courses",
    version="1.0.0"
)

# ============================================================================
# TASK 1: Define Pydantic Models for Data Validation
# ============================================================================
# TODO: Create a User model with id, name, email, and age fields
# TODO: Create a Product model with id, name, price, and description fields


# ============================================================================
# Sample data storage (in-memory database for this assignment)
# ============================================================================
users_db = {}
products_db = {}
user_id_counter = 1
product_id_counter = 1


# ============================================================================
# TASK 2: Implement Basic Routes
# ============================================================================

@app.get("/health")
def health_check():
    """Health check endpoint to verify the API is running."""
    # TODO: Return a JSON response with a status message
    pass


@app.post("/users")
def create_user(user: "User"):
    """Create a new user with name and email."""
    # TODO: Validate the user data using the User model
    # TODO: Add the user to the users_db
    # TODO: Return the created user with a 201 status code
    pass


# ============================================================================
# TASK 3: Implement CRUD Operations with Error Handling
# ============================================================================

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Retrieve a specific user by ID."""
    # TODO: Look up the user in users_db
    # TODO: Return 404 if user not found
    # TODO: Return the user data if found
    pass


@app.get("/products")
def list_products(skip: int = 0, limit: int = 10, min_price: Optional[float] = None, max_price: Optional[float] = None):
    """
    List all products with optional filtering and pagination.
    
    Query parameters:
    - skip: Number of products to skip (default: 0)
    - limit: Maximum number of products to return (default: 10)
    - min_price: Filter products with price >= min_price
    - max_price: Filter products with price <= max_price
    """
    # TODO: Filter products based on min_price and max_price
    # TODO: Apply pagination with skip and limit
    # TODO: Return filtered and paginated products
    pass


@app.post("/products")
def create_product(product: "Product"):
    """Create a new product."""
    # TODO: Validate the product data
    # TODO: Ensure price is positive
    # TODO: Add product to products_db
    # TODO: Return the created product with a 201 status code
    pass


# ============================================================================
# Run the application
# ============================================================================
# To run this API, use: uvicorn starter-code:app --reload
# Visit http://localhost:8000/docs to see the interactive API documentation
