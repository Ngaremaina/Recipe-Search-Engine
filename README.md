# Recipe Search Web Application
This web application is designed as a robust recipe search platform, leveraging the Django framework and seamlessly integrating the powerful Edamam API. By harnessing the capabilities of Django, it offers a solid foundation for handling user interactions and data management. Through the integration of the Edamam API, users can effortlessly explore a vast array of recipes tailored to their preferences and requirements. Whether searching for specific dishes or seeking culinary inspiration, this application provides a comprehensive and user-friendly experience for discovering delicious recipes.

## Features

- **Recipe Search**: Users can search for recipes by entering keywords or ingredients.
- **Recipe Details**: Users can view detailed information about each recipe, including ingredients, instructions, and nutritional information.

## Installation

1. Clone the repository:
   ```bash
      git clone https://github.com/Ngaremaina/Recipe-Search-Engine
      cd Recipe-Search-Engine
   ```
2. Intall the env variables
   ```bash
      python -m venv env
    ```

3. Activate the env file
   ```bash
      source env/bin/activate
   ```

4. Install dependencies:
   ```bash
      pip install -r requirements.txt
   ```

5. Start the development server:
   ```bash
      python manage.py runserver
   ```

6. Open your web browser and go to `http://localhost:8000` to view the application.

## Usage

1. Use the search bar to enter keywords or ingredients for recipes you're looking for.
2. Browse through the search results and click on a recipe to view its details.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
