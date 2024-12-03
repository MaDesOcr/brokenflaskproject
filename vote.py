from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

votes = {
    "Option A": 0,
    "Option B": 0,
    "Option C": 0
}
if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index_vote.html')

@app.route('/vote', methods=['GET'])
def vote():
    if request.method == 'POST':
        option = request.form.get('option')
        votes[option] = 1
        return redirect(url_for('results'))
    return render_template('vote.html')

@app.route('/results')
def results():
    return render_template('results.html', votes=votes)















if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def index():
    return render_template('index.html')



