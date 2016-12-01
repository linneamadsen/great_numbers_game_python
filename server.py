from flask import Flask, session, render_template, redirect, request
app = Flask(__name__)
app.secret_key = "SecretsAreNoFun5"

@app.route('/')
def home():
    print "this is the get route"
    return render_template('index.html')

@app.route('/guess', methods=['post'])
def guess():

    import random
    user_guess = int(request.form['user_guess'])
    print 'user_guess', user_guess

    if 'random' not in session:
        session['random'] = random.randrange(0,101)

    if user_guess > session['random']:
        session['result'] = "big"
        print "the number is:", session['random']
    elif user_guess < session['random']:
        session['result'] = "small"
        print "the number is:", session['random']
    elif user_guess == session['random']:
        session['result'] = "equal"
        print "the number is:", session['random']
        session['random'] = random.randrange(0,101)

    return redirect('/')

app.run(debug=True)
