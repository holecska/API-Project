# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## API References

### Getting Started
- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:5000/`, which is set as a proxy in the frontend configuration. 
- Authentication: This version of the application does not require authentication or API keys. 

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": False, 
    "error": 400,
    "message": "bad request"
}
```
The API will return four error types when requests fail:
- 400: Bad Request
- 404: Resource Not Found
- 405: Method not allowed
- 422: Not Processable

### Endpoints

#### GET /categories
- General:
	Returns of an object with caterories and a success value (True/False)
- Sample: `curl http://127.0.0.1:5000/categories`

```
{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "success": true
}
```

#### GET /questions
- General: 
	Returns a list of a category object with all categories, 
	paginated (basic setting: 10 questions per Page), not categorized questions stored in the database.
	Returns current category (in this case the value is null), number of total questions and a success value.

- Sample: `curl http://127.0.0.1:5000/questions?page=1`

```
{
  "categories": [
    "Science", 
    "Art", 
    "Geography", 
    "History", 
    "Entertainment", 
    "Sports"
  ], 
  "current_category": null, 
  "questions": [
    {
      "answer": "Tom Cruise", 
      "category": 5, 
      "difficulty": 4, 
      "id": 4, 
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }, 
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }
  ], 
  "success": true, 
  "total_questions": 21
}

```

#### GET /categories/<int:category_id>/questions?page=2

- General: 
	Returns questions by category and paginated (in this case 5 question per Page).
	Returns a success value and the total number of questions in the category.

- Sample: `curl http://127.0.0.1:5000/categories/2/questions?page2`

```
{
  "questions": [
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "success": true, 
  "total_questions": 3
}
```

#### POST /questions

- General: this API can handle two type of requests. 

1) Create a new question

   - General:
	The Frontend send a JSON file, containing values for answer, category, difficulty and question.
	Returns an answer with success value, and the created question's ID. 

   - Sample: 
   `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" 
    -d '{
	"answer":"The Palace of Versailles",
	"category": "1",
	"difficulty": "4",
	"question":"In which royal palace would you find the Hall of Mirrors"}'`

   ```
   {
    "success": true, 
    "created": 12,
   }
   ```

2) Search in questions

   - General: 
	The client send a JSON data, with 'searchTerm' attribute. 
	Returns questions which meet the search criterien. 
   
   - Sample: 
	`curl http://127.0.0.1:5000/questions -X POST 
	-H "Content-Type: application/json" -d '{"searchTerm":"Searching"}'`

   
   ```
   {
   "questions": [
       {
         "answer": "Lake Victoria", 
         "category": 3, 
         "difficulty": 2, 
         "id": 13, 
         "question": "What is the largest lake in Africa?"
       }, 
       {
         "answer": "The Palace of Versailles", 
         "category": 3, 
         "difficulty": 3, 
         "id": 14, 
         "question": "In which royal palace would you find the Hall of Mirrors?"
       }
     ], 
   "success": true, 
   "total_questions": 3, 
   "current_category": null
   }
   ```


#### DELETE /questions/delete/<int:question_id>

- General: Delete a specified question and returns the deleted question's ID, 
	success value, all (paginated, not categorized) questions and the number of questions in the database.

- Sample: `curl http://127.0.0.1:5000/questions/delete/5 -X DELETE`

 ```

 {
   "deleted": 5,
   "questions": [
       {
         "answer": "Lake Victoria", 
         "category": 3, 
         "difficulty": 2, 
         "id": 13, 
         "question": "What is the largest lake in Africa?"
       }, 
       {
         "answer": "The Palace of Versailles", 
         "category": 3, 
         "difficulty": 3, 
         "id": 14, 
         "question": "In which royal palace would you find the Hall of Mirrors?"
       }
      ... (up to 10 per Page)
     ], 
   "success": true, 
   "total_questions": 3,
   "current_category": null
 }

```

#### GET / POST QUIZZES /quizzes

- General: 
	This Endpoint needs the played category and the previous questions of the game.
	Returns a success value and a random question to the frontend. If all questions in the category have been already sent to the client, it will return an empty question attribute.

- Sample: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" 
	  -d '{"quiz_category": "0", "previous_questions": [14,15]}'

```

{
"question": {
   "answer": "One",
   "category": 2,
   "difficulty": 4,
   "id": 18,
   "question": "How many paintings did Van Gogh sell in his lifetime?"
   },
"success": true
}

```



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```