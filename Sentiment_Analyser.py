from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask('__name__')

@app.route("/", methods=["GET", "POST"])
def index():
    Sentiment = ''
    Polarity = ''
    Subjectivity = ''

    if request.method == "POST":
        text = request.form['text']
        blob = TextBlob(text)
        Polarity = blob.sentiment.polarity
        Subjectivity = blob.sentiment.subjectivity
        Polarity = round(Polarity, 2)
        Subjectivity = round(Subjectivity, 2)

        if Polarity > 0:
            Sentiment = "Positive"
        elif Polarity < 0:
            Sentiment = "Negative"
        else:
            Sentiment = "Neutral"

    return render_template('index.html', sentiment=Sentiment, polarity=Polarity, subjectivity=Subjectivity)

if __name__ == '__main__':
    app.run(debug=True, port=8000)