import torch
from flask import request
from flask import Flask, render_template
from detoxify import Detoxify

app = Flask(__name__)

model = Detoxify('original')

@app.route('/')
def homepage():
    return render_template('website.html')

@app.route('/', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        text = request.form['inputedText']
        predictions =  model.predict(text)
        tox = round(predictions['toxicity'], 2)
        sev = round(predictions['severe_toxicity'], 2)
        obs = round(predictions['obscene'], 2)
        thr = round(predictions['threat'], 2)
        ins = round(predictions['insult'], 2)
        ida = round(predictions['identity_attack'], 2)

        return render_template('resultsPage.html',  submittedText=text, toxRes=tox, sevRes=sev, obsRes=obs, thrRes=thr, insRes=ins, idaRes=ida)#, toxicityRes=tox, sevRes=sev, obs=obsRes, thr=thrRes, ins=insRes, ida=idaRes  ) # render_template('index.html', predictions=pred)

if __name__ == '__main__':
    app.run(port=5000, debug=True, host="0.0.0.0")
