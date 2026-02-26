from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    subj = request.form.get('subj')
    time = request.form.get('time')

    # query parameter
    if subj == 'subj1':
        return redirect(url_for('subj1', time=time))
    elif subj == 'subj2':
        return redirect(url_for('subj2', time=time))
    elif subj == 'subj3':
        return redirect(url_for('subj3', time=time))
    elif subj == 'subj4':
        return redirect(url_for('subj4', time=time))
    else:
        return "Invalid selection."

@app.route('/subj1')
def subj1():
    return render_template('subj1.html')

@app.route('/subj2')
def subj2():
    return render_template('subj2.html')

@app.route('/subj3')
def subj3():
    return render_template('subj3.html')

@app.route('/subj4')
def subj4():
    return render_template('subj4.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000, debug=True)
