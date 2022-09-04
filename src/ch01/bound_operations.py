import requests

# I/O-bound web request
response = requests.get("https://www.example.com")
items = response.headers.items()

# CPU-bound response processing
headers = [f"{key}: {header}" for key, header in items]

# CPU-bound string concatenation
formatted_headers = "\n".join(headers)

with open("headers.txt", "w") as file:
    # I/O-bound write to disk
    file.write(formatted_headers)
