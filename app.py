from flask import Flask, render_template, request, url_for, jsonify

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("home.html")

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
	if request.method == "POST":
		data = request.form.getlist('data[]')
		equation = ''.join(data)
		ans = eval(equation)

		return jsonify(ans)

	return render_template("calculator.html")
