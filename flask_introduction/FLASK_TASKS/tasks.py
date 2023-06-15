# 1 užduotis
# Sukurti programą, 
# kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu (rekomenduojama naudoti šablonus).

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")




 # 2 užduotis   
# Sukurti programą, kuri įvedus norimą žodį adreso eilutėje (po / simbolio) ir
# paspaudus ENTER, atspausdintų jį penkis kartus.


@app.route('/<word>')
def print_word(word):
    my_list =[]
    for _ in range(5):
        my_list.append(word)
    s = '<br>'.join(my_list)   
    return s 
      
@app.route("/v2/<word>")
def word(word):
    words = []
    for _ in range(5):
        words.append(word)
    return render_template("word.html", my_list=words)
    

# if __name__ == '__main__':
#     app.run(debug=True)
    
    

# @app.route('/print', methods=['GET', 'POST'])
# def print_word():
#     if request.method == 'POST':
#         word = request.form.get('word', '')  
#         output = word * 5 
#         return render_template("print.html", output=output)
#     return render_template("print.html")


# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    #  3  užduotis 
    # Sukurti programą, kuri puslapyje localhost:5000/keliamieji
# parodytų visus keliamuosius metus nuo 1900 iki 2100 metų

# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/keliamieji')
# def keliamieji():
#     leap_years = []
#     for year in range(1900, 2101):
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             leap_years.append(year)
#     return render_template("keliamieji.html", leap_years=leap_years)

# if __name__ == '__main__':
#     app.run(debug=True)
    
    
    #  4  užduotis
    
# from flask import Flask, render_template, request

# app = Flask(__name__)

@app.route('/keliamieji_input', methods=['GET', 'POST'])
def leap_year():
    if request.method == 'POST':
        year = request.form.get('year', '')  
      

        try:
            year = int(year)
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                is_leap_year = True
            else:
                is_leap_year = False
        except ValueError:
            is_leap_year = False

        return render_template("keliamieji_input.html", year=year, is_leap_year=is_leap_year)
    else:
        return render_template("keliamieji_input.html")

if __name__ == '__main__':
    app.run(debug=True)