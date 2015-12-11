from flask import Flask, render_template #NEW IMPORT!!
from flask import Flask, render_template, request  #NEW IMPORT -- request


app = Flask(__name__)    #This is creating a new Flask object

#decorator that links...

@app.route('/')
@app.route('/index')          						#This is the main URL
def index():
    return render_template("index.html", name = "index")		#The argument should be in templates folder

# @app.route('/bcsm')
# def bcsm():
#     return render_template("bcsm.html", name = "bcsm")
#
# @app.route('/pcsm')
# def pcsm():
#     return render_template("pcsm.html", name = "pcsm")
#
# @app.route('/blcsm')
# def plcsm():
#     return render_template("blcsm.html", name = "blcsm")
#
# @app.route('/lcsm')
# def lcsm():
#     return render_template("lcsm.html", name = "lcsm")

@app.route('/about')
def lcsm():
    return render_template("about.html", name = "about")

# @app.route( )
#     if enter ! = xxx:
#         return redirect(url_for('index'))



if __name__ == '__main__':
    app.run(debug=True)		#debug=True is optional
