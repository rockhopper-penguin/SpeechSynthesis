from flask import Flask, render_template, request
import sys
import requests

adress = 'https://api.voicetext.jp/v1/tts'

def getVoice(key, text, voice, emotion, emotion_level):
	Parameters = {
		'text': text,
		'speaker': voice,
		'emotion':emotion,
		'emotion_level': emotion_level
	}
	send = requests.post(adress, params = Parameters, auth = (key,''))
	result = open("static/result/result.wav", 'wb')
	result.write(send.content)
	result.close()

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

@app.route('/', methods=['POST'])
def post():
	key = request.form['apiKey']
	text = request.form['setText']
	voice = request.form['setVoice']
	emotion = request.form['setEmotion']
	emotion_level = request.form['setEmotionLevel']
	getVoice(key, text, voice, emotion, emotion_level)
	return render_template('result.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", debug=True)