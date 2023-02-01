from flask import Flask, request, render_template
from stories import Story, story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "oh-so-secret"
debug = DebugToolbarExtension(app)



@app.route('/')
def home_page():
    words = story.prompts
    return render_template('form.html', story=words)

@app.route('/story')
def story_page():
    text = story.generate(request.args)
    return render_template('first_story.html', text=text)