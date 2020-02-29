from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def post():
	key = request.form['apiKey']
	text = request.form['setText']
	voice = request.form['setVoice']
	return render_template('index.html', getApiKey = key, getText = text, getVoice = voice)

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)