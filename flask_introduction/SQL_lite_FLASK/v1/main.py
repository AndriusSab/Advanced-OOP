# from flask import Flask
from flask import Flask, request, render_template
# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# @app.route("/another")
# def hello_world():
#     return "<p>GoodBye, World!</p>"


# if __name__ == "__main__":
#     app.run(debug=True)


# app = Flask(__name__)

# @app.route("/<name>")
# def user(name):
#     return f"Labas, {name}"

# if __name__ == "__main__":
#     app.run()

# from flask import Flask, render_template
# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/calculations")
# def calculate():
#     return render_template("calculations.html")

# @app.route("/names")
# def names():
#     names = ["Andrius", "Simona", "Fausta"]
#     return render_template("names.html", my_list=names)


# if __name__ == "__main__":
#     app.run(debug=True)


app = Flask(__name__)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        vardas = request.form['vardas']
        return render_template("greetings.html", vardas=vardas)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
