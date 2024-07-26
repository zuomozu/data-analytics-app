from flask import Flask, render_template
import analysis

app = Flask(_name_)

@app.route('/')
def index():
    results = analysis.run_analysis()
    return render_template('index.html', results=results)

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
