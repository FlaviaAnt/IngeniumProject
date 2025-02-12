from flask import Flask, redirect
import random

app = Flask(__name__)

# List of your image URLs
images = [
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/MagicEraser_250212_110759.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvTWFnaWNFcmFzZXJfMjUwMjEyXzExMDc1OS53ZWJwIiwiaWF0IjoxNzM5MzUyMDY3LCJleHAiOjE3Mzk5NTY4Njd9.EmIQn-M5POlrmjjV6wfSPmYtyypll6MmtsAcJrGAC2I",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/pexels-photo-1367192.jpeg?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvcGV4ZWxzLXBob3RvLTEzNjcxOTIuanBlZyIsImlhdCI6MTczOTM1MjA4OSwiZXhwIjoxNzM5OTU2ODg5fQ.MkOqB1VlNTVH9wHFlb4ARCK75fA4GWwMNlxsOwa6YR0",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/pexels-photo-149621.jpeg?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvcGV4ZWxzLXBob3RvLTE0OTYyMS5qcGVnIiwiaWF0IjoxNzM5MzUyMTA0LCJleHAiOjE3Mzk5NTY5MDR9.gs61HGElzcNbLnx8jFHqHEgdnJBP1OwuxrmDZMKPczg",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/pexels-photo-3293148.webp?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvcGV4ZWxzLXBob3RvLTMyOTMxNDgud2VicCIsImlhdCI6MTczOTM1MjEyNCwiZXhwIjoxNzM5OTU2OTI0fQ.alXUAK8hRy9h2rZOqVvgVc0nEnzskeSocBY8rrTUXzs",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/photo-1451187580459-43490279c0fa.avif?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvcGhvdG8tMTQ1MTE4NzU4MDQ1OS00MzQ5MDI3OWMwZmEuYXZpZiIsImlhdCI6MTczOTM1MjEzMiwiZXhwIjoxNzM5OTU2OTMyfQ.mJHL9n4fiL5OuoI7CUIrHpMTNtSZzyq56p0q2GQCyIA"
]

@app.route('/random-image', methods=['GET'])
def random_image():
    # Pick a random image from the list
    selected_image = random.choice(images)
    # Redirect to the selected image
    return redirect(selected_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
