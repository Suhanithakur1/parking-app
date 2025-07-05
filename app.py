#app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def check():
    return 'Flask is working'

if __name__ == '__main__':
    app.run()
  
''' app = Flask(__name__)
You’re creating a Flask app object.

__name__ tells Flask where to look for resources like templates.

This line sets up the "engine" of your app.

🧠 Memory tip: “Make the app with Flask(__name__).

 @app.route('/')
This is a route decorator. It connects a URL path (/) to a Python function.

'/' is the homepage of your site → http://127.0.0.1:5000/”

4️⃣ def check(): return 'Flask is working'
When someone visits the homepage (/), this function runs.

It returns plain text: "Flask is working" that appears in the browser.

🧠 Memory tip: "Route → Function → Return response."

5️⃣ if __name__ == '__main__':
This checks if the file is being run directly (not imported).

If yes, then:

6️⃣ app.run()
Starts the development server.

Flask will host your app at http://127.0.0.1:5000/

🧠 Memory tip: “Run the app if file is main.”
'''
