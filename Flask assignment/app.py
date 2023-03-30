# step1  - To import FLASK
from flask import Flask,redirect,request,render_template 
import re

# step2  - Create the object with a parameter __name__
app = Flask(__name__) 

# step3 - Create an END POINT using routes and bind them with a functionality
@app.route('/')
def home_page():
    return render_template("index.html")
@app.route('/',methods=['POST'])
def matchreg():

    if request.method == 'POST':
        test_string = request.form.get('test_string', '')
        regex_string = request.form.get('regex_string', '')

        matches = re.findall(regex_string, test_string)

        # Render the results page with the matches
        return render_template('result.html', matches=matches)

if __name__ =="__main__":
    app.run(debug=True)


