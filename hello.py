from flask import Flask, render_template
# create a flask instance

app = Flask(__name__)

# create a route decorator 
@app.route('/')

# def index():
#     return "<h1>Hello World!</h1>"


def index():
    first_name = "Yomiel"
    stuff = "This is bold Text"
    favorite_pizza = ["Peppoeroni", "Cheese", "Mushroom", 41]
    return render_template("index.html", 
                           first_name = first_name, 
                           stuff = stuff,
                           favorite_pizza = favorite_pizza)

# localhost:5000/user/Yomiel
@app.route('/user/<name>')
def user(name):
    return render_template("user.html", user_name = name)
if __name__ == '__main__':
    app.run(debug=True)

# Create Custom Error Pages 

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.errorhandler(500)
def page_not_found(e):
    return render_template("404.html"), 500
