# Sentiment Analyzer – Flask Web App

A simple and elegant web-based Sentiment Analyzer built with Flask and TextBlob. Users can input text, and the app will return the sentiment (Positive, Negative, Neutral), polarity, and subjectivity scores.


## Features

- Analyze sentiment of any text input
- Calculates **polarity** and **subjectivity** using TextBlob
- Displays clean, color-coded results in a stylish web UI
- Built using **Flask** and styled with custom **CSS**
- Lightweight and beginner-friendly


## Requirements

- **Python 3.10 or higher**
- Install dependencies using:

```bash
pip install -r requirements.txt
```


## Setup

1. Clone this repository or download the project files.

```bash
git clone https://github.com/Feniel-Dhanak/sentiment-analyzer-w-flask.git
```

2. Run the Flask app:

```bash
python Sentiment_Analyser.py
```

3. Open your browser and visit:

```
http://127.0.0.1:8000/
```

4. Enter your text and click **Analyze** to see results!


## Output

- **Sentiment** → Positive, Negative, or Neutral
- **Polarity** → Ranges from -1 (negative) to 1 (positive)
- **Subjectivity** → Ranges from 0 (objective) to 1 (subjective)
