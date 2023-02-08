from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

'''
Home page 
'''
@app.route('/')
def index():
	return render_template("home.html")

'''
calculator either returns the template if a POST or GET is not passed to the function. 

If a POST request, I get the data passed to the function from ajax and convert the list to an equation string 

Used built-in function eval to calculate the answer 

returns the answer to the equation or error if the equation is invalid. 
'''
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
	if request.method == "POST":
		data = request.form.getlist('data[]')
		ans = 0 

		try: 
			equation = ''.join(data)
			ans = eval(equation)
		except Exception as e: 
			return "", 403
		else: 
			return jsonify(ans)

	return render_template("calculator.html")