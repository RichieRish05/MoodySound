import requests



# Deezer track ID for "Shape of You"
track_id = "466972402"  # Replace with your desired track ID

# Make the request
response = requests.get(f"https://api.deezer.com/track/{track_id}")
data = response.json()

# Extract the preview URL
if "preview" in data:
    print("Preview URL:", data["preview"])
else:
    print("No preview available.")
