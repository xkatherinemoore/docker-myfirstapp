from flask import Flask, render_template
import random

app = Flask(__name__)

# list of cat images
images = [
	"https://hips.hearstapps.com/hmg-prod/images/cute-photos-of-cats-curled-up-sleeping-1593184773.jpg?resize=480:*",
	"https://hips.hearstapps.com/hmg-prod/images/cute-photos-of-cats-excited-1593184777.jpg?resize=480:*",
	"https://hips.hearstapps.com/hmg-prod/images/cute-photos-of-cats-in-box-1593184776.jpg?resize=480:*",
	"https://hips.hearstapps.com/hmg-prod/images/cute-photos-of-cats-in-grass-1593184777.jpg?resize=480:*"
 ]

@app.route('/')
def index():
 url = random.choice(images)
 return render_template('index.html', url=url)

if __name__ == "__main__":
 app.run(host="0.0.0.0")
