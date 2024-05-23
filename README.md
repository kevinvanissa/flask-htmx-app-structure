# Flask Application with htmx, Blueprints, and Bootstrap 5

This repository contains a personalized structure for a Flask application that incorporates htmx for enhanced frontend interactions, uses Blueprints for modular application design, and integrates Bootstrap 5 for styling.

## Deployment Instructions

To run the application locally, follow these steps:

1. **Clone the repository:**
```bash
git clone https://github.com/kevinvanissa/flask-htmx-app-structure.git
cd flask-htmx-app-structure 
```
   2. **Set up virtual environment and install dependencies:**
```bash
python -m venv env  # Create a virtual environment
source env/bin/activate  # Activate the virtual environment (on Windows use `env\Scripts\activate`)
pip install -r requirements.txt  # Install required packages
```
     
  3. **Apply database migratons to create app.db:**
```bash
flask db init  # Initialize migrations (if not already done)
flask db migrate -m "My First Migration"  # Generate a migration script
flask db upgrade  # Apply the migration to create the database
```
4. **To perform tests(basic test is included):***
```bash
pytest
```
