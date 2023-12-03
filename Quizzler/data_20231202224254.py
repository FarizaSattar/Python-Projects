# Import the 'requests' library to handle HTTP requests.

# Parameters specifying the number and type of trivia questions.
parameters = {
    "amount": 10,        # Number of questions to retrieve.
    "type": "boolean",   # Type of questions, in this case, multiple-choice questions with true/false answers.
}

# Send a GET request to the specified API URL with the defined parameters.
response = requests.get("https://opentdb.com/api.php", params=parameters)

# Check for any HTTP errors in the response, raising an exception if an error occurs.
response.raise_for_status()

# Parse the response as JSON data and retrieve the question data from the 'results' field.
data = response.json()
question_data = data["results"]  # Extracted question data from the API response.
