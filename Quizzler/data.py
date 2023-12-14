# Import the 'requests' library to handle HTTP requests.

# Parameters specifying the number and type of trivia questions.
parameters = {
    # Number of questions to retrieve.
    "amount": 50, 
    # Type of questions, in this case, multiple-choice questions with true/false answers.
    "type": "boolean",   
}

# Send a GET request to the specified API URL with the defined parameters.
response = requests.get("https://opentdb.com/api.php", params=parameters)

# Check for any HTTP errors in the response, raising an exception if an error occurs.
response.raise_for_status()

# Parse the response as JSON data and retrieve the question data from the 'results' field.
data = response.json()
# Extracted question data from the API response.
question_data = data["results"]  
