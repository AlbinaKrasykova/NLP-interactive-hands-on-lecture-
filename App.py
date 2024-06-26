from flask import Flask, render_template, request
from TextSumFunction import final_summary

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    summary = ''
    if request.method == 'POST':
        text = request.form['UserText']
        summary = final_summary(text)
        print(summary)
        
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)

