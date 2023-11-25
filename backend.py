import json
from flask import Flask, render_template, request, redirect, url_for
from summary import summary
from scraper import scraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keywords = request.form.get('keywords')
        articles_summary = summary(scraper(keywords))

        # Convert the list to a JSON string
        articles_summary_json = json.dumps(articles_summary)

        return redirect(url_for('result', keywords=keywords, articles_summary=articles_summary_json))
    else:
        return render_template('index.html')

@app.route('/result')
def result():
    # Retrieve the data
    keywords = request.args.get('keywords')
    articles_summary = json.loads(request.args.get('articles_summary'))

    # Render the result template
    return render_template('result.html', keywords=keywords, articles_summary=articles_summary)

if __name__ == '__main__':
    app.run(debug=True)
