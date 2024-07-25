from flask import Flask, render_template
import analysis

app = Flask(__name__)

@app.route('/')
def index():
    results = analysis.run_analysis()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
