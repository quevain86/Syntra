import re
import requests
import yaml

# Set your environment variables directly
JOKE_URL = "https://icanhazdadjoke.com"
POST_URL = "https://httpbin.org/post"

# Amount of jokes
amount_of_jokes = 5

# Headers for HTTP requests
headers = {"Accept": "application/json"}

# Fetch jokes
def fetch_jokes():
    jokes = []
    for _ in range(amount_of_jokes):
        response = requests.get(JOKE_URL, headers=headers)
        joke_data = response.json()
        joke_intro = re.match(r'(.{20})', joke_data['joke']).group()
        jokes.append({
            'intro': joke_intro,
            'joke': joke_data['joke'],
            'id': joke_data['id']
        })
    return jokes

# Fetch jokes
jokes = fetch_jokes()

# Convert data in YAML
output_data = {'jokes': jokes}
yaml_output = yaml.dump(output_data)
print(yaml_output)

# Perform POST request
post_json = {"name": "Quevain"}
post_response = requests.post(POST_URL, json=post_json)
print(post_response.text)

# Print origin IP address from the response
origin_ip = post_response.json()['origin']
print(f"Your origin IP address: {origin_ip}")