from flask import Flask, redirect
import random

app = Flask(__name__)

# List of your image URLs
images = [
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/IMG1.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvSU1HMS5wbmciLCJpYXQiOjE3MzkzNjI3NDMsImV4cCI6MTczOTk2NzU0M30.Cqzko86dhL635p-usXc5q7JdqeMx0F66-XZGkjA2bog",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img2.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nMi5wbmciLCJpYXQiOjE3MzkzNjI3ODksImV4cCI6MTczOTk2NzU4OX0.i8gSxZpt2f5f2xjUU9ogaVkE980UZd0tOypWfF2Ng6I",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img3.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nMy5wbmciLCJpYXQiOjE3MzkzNjI3OTgsImV4cCI6MTczOTk2NzU5OH0.trj5hnqeIErQBzNSPsgMMP6T-SXWx1fGBo1M2U1RkWA",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img4.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nNC5wbmciLCJpYXQiOjE3MzkzNjI4MTAsImV4cCI6MTczOTk2NzYxMH0.IgnqkZbCtr560OwpPe3B5Q6QTwS9tp5CTewA-49II4Y",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img5.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nNS5wbmciLCJpYXQiOjE3MzkzNjI4MjQsImV4cCI6MTczOTk2NzYyNH0.gteGGhCa2PAUfgi7pIWOmVQdYDxrQiz5QaBMnYGSjcQ",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img6.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nNi5wbmciLCJpYXQiOjE3MzkzNjI4MzUsImV4cCI6MTczOTk2NzYzNX0.k8mOF0GCUeRV4DUHl7Jd45ymswG2fqPi_cCFWio4g4s",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img7.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nNy5wbmciLCJpYXQiOjE3MzkzNjI4NDMsImV4cCI6MTczOTk2NzY0M30.MlR6C13z9pEQ5OshrEnPx60ypKt9eNDDyJiT-eXHjuY",
    "https://iyvhuslpradevwbdimbd.supabase.co/storage/v1/object/sign/Nature%20massages/img8.png?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1cmwiOiJOYXR1cmUgbWFzc2FnZXMvaW1nOC5wbmciLCJpYXQiOjE3MzkzNjI4NTksImV4cCI6MTczOTk2NzY1OX0.3jvTi4xWf0vMxGA8G86LZbdKe1h2tK8EYv8Y4_PkK_k"
]

@app.route('/random-image', methods=['GET'])
def random_image():
    # Pick a random image from the list
    selected_image = random.choice(images)
    # Redirect to the selected image
    return redirect(selected_image)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
