import requests

# Specify the API endpoint URL
api_url = "https://dad-jokes.p.rapidapi.com/random/joke"

# Optional: If the API requires headers or additional parameters, you can specify them
headers = {'X-RapidAPI-Key': '5212105672msh5ede6170621fe25p1572d4jsn4b919ac2c0b7'}

# Make the GET request
response = requests.get(api_url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

 # Check if the 'body' key is present and has a list of jokes
    if 'body' in data and isinstance(data['body'], list) and len(data['body']) > 0:
        # Extract and print 'setup' and 'punchline' from the first joke in the list
        joke = data['body'][0]
        print(f"Setup: {joke.get('setup', 'N/A')}") # Or I could simply ask to print(joke.get('setup', 'N/A'))
        print(f"Punchline: {joke.get('punchline', 'N/A')}") # Or I could simply ask to print(joke.get('punchline', 'N/A'))
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

# I understand, but could write the code myself up to line 15. 

   