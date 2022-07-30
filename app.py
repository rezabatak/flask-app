from crypt import methods
from flask import Flask, redirect, url_for, render_template, request
from ig_miner import ig_miner
from tt_miner import tt_miner
from ast import literal_eval

app = Flask(__name__)

main_title = "ALVA Data Tools"

# @app.route >> to specify what is the url path
@app.route("/")
def home():
    return render_template('index.html', main_title = main_title)

@app.route("/result", methods = ['POST', 'GET'])
def result():
    username = request.form.get('usernameInput')
    socialchannel = request.form.get('socialchannel')
    itteration = int(request.form.get('itterationInput'))

    # TODO: bikin function ingest_db

    if socialchannel == 'instagram':
        ig_kolDataResult = ig_miner.getKOLData(influencer_username=username, itteration=itteration)
        tt_kolDataResult = ''
    if socialchannel == 'tiktok':
        ig_kolDataResult = ''
        tt_kolDataResult = tt_miner.getKOLData(influencer_username=username, itteration=itteration)
    else:
        kolDataResult = 'Need to select social media channel'
    
    return render_template('index.html', main_title = main_title, ig_kolDataResult = ig_kolDataResult, tt_kolDataResult = tt_kolDataResult)

@app.route("/docs")
def docs():
    return render_template('docs.html', main_title = main_title) 

if __name__ == "__main__":
    app.run(host="139.59.127.27", port=80, debug=True) # For production never set debug=True
