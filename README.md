# Flask Based Web Application

This repository contains a Flask based web application.

## Installation

To install the necessary dependencies for this application, follow these steps:

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/pankaj0548/Recipe-test.git
    ```

    Replace `your_username` and `your_repository` with your GitHub username and the name of your repository, respectively.

2. **Set Up Python Virtual Environment:**

    Navigate to the project directory:

    ```bash
    cd Recipe-test
    ```

    Create a Python virtual environment:

    ```bash
    python -m venv venv
    ```

    Activate the virtual environment:

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

    On macOS and Linux:

    ```bash
    source venv/bin/activate
    ```

3. **Install Requirements:**

    Once the virtual environment is activated, install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

    This will install all the necessary packages specified in the `requirements.txt` file.

4. **App env :**

    ```bash
    UPLOAD_FOLDER = 'app/static/img/uploads'
    DATABASE_URL  = 'mysql+pymysql://root:root@localhost/recipes' #Yours Db Url
    SECRET_KEY    = 'ygae@1!ffsyud@g&*ch%$avplz/d/615r&2vi21sgf(3fh*hu.x'
    ```
## Running the Application

After installing the requirements, you can run the Flask application using the following command:

```bash
python run.py
```


## Recipe App Database Schema

This repository contains the SQL schema for a recipe application database. The schema defines two tables: User and Recipe, along with their respective fields and relationships.

**Table Descriptions**

    **User Table:**
        **id**: Unique identifier for each user (Primary Key).
        **name**: Name of the user.
        **email**: Email address of the user (unique).
        **password**: Password associated with the user's account.

    **Recipe Table**
        **id**: Unique identifier for each recipe (Primary Key).
        **image**: URL or file path for the recipe image (nullable).
        **title**: Title of the recipe.
        **description**: Brief description or summary of the recipe.
        **ingredients**: List of ingredients required for the recipe.
        **instructions**: Step-by-step instructions for preparing the recipe.
        **created_by**: ID of the user who created the recipe (Foreign Key referencing the id column of the User table).
