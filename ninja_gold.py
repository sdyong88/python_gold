from flask import Flask, render_template,request, redirect, session
import random

app = Flask(__name__)
app.secret_key='ninjagoldsecret'

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/process_money', methods=['POST'])
def process_money():
	default = 0
	bank = session.get('bank',default)
	activities = session.get('activities',default)

	farm_gold = request.form.get('farm_gold',default=None)
	cave_gold = request.form.get('cave_gold',default=None)
	house_gold = request.form.get('house_gold',default=None)
	casino_gold = request.form.get('casino_gold',default=None)
	
	session['farm_gold'] = farm_gold
	session['cave_gold'] = cave_gold
	session['house_gold'] = house_gold
	session['casino_gold'] = casino_gold
	session['bank'] = bank

	farm_rand = int(random.randrange(10,21))
	cave_rand = int(random.randrange(5,10))
	house_rand = int(random.randrange(2,5))
	casino_rand = int(random.randrange(-50,50))

	if(session['farm_gold']):
		session['bank'] += farm_rand
		session['activities'] = 'Earn',farm_rand,'gold from the cave!'
	if(session['cave_gold']):
		session['bank'] += cave_rand
		session['activities'] = 'Earn',cave_rand,'gold from the cave!'
	if(session['house_gold']):
		session['bank'] += house_rand
		session['activities'] = 'Earn',house_rand,'gold from the cave!'
	if(session['casino_gold']):
		session['bank'] += casino_rand
		session['activities'] = 'Took',casino_rand,'gold from the cave!'

	return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
	session.clear()
	return redirect('/')

app.run(debug=True)