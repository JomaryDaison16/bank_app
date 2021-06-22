from api import app, CORS, cross_origin
import os
from models import *
from flask import request, json, jsonify, render_template
import random
from numpy.random import randint
# app = Flask(__name__)


@app.route('/')
def login():
	entries = New_Acc.query.order_by(New_Acc.cust_fname).all()
	return render_template('dashboard.html', entries = entries)


@cross_origin('*')
@app.route('/Create-Account', methods=['POST'])
def New_acc():
	data = request.get_json()
	passwrd = gen_pass() 
	acc = gen_acc_num()
	# console.log("hallo")
	# numpy.ndarray convertion into str
	acc_str = ''.join(str(i) for i in acc)

	account_num = New_Acc.query.filter_by(cust_acc_num = acc_str).first()

	if account_num:
		acc = gen_acc_num()
		New_acc()
		# console.log("added")

	else:
	
		#Status value is 1 for active accounts
		stat = 1

		new_user = New_Acc(cust_fname = data['fname'], 
							cust_mname = data['mname'],
							cust_lname = data['lname'],
							cust_balance = data['balance'],
							cust_status = stat,
							cust_acc_pass = passwrd,
							cust_acc_num = acc_str)
		# console.log("na")
		
		db.session.add(new_user)
		db.session.commit()

		return jsonify({'message': 1}) #return 1 if success else return 0

@app.route('/deposite', methods=['GET', 'POST'])
def deposite():
	data = request.get_json()

	id_cust = New_Acc.query.filter_by(cust_acc_num=data['acc_num']).first()
	
	if id_cust:
		id_cust.cust_balance += data['balance']

		db.session.add(id_cust)
		db.session.commit()

		return jsonify({'message':id_cust.cust_balance})

	else:
		return jsonify({'message': 0}) #return 1 if success else return 0


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
	data = request.get_json()

	id_cust = New_Acc.query.filter_by(cust_acc_num=data['acc_num']).first()
	
	if id_cust:
		if data['balance'] > id_cust.cust_balance:
			return jsonify({'message': 0}) #return 1 if success else return 0
			# return "Sorry! Insufficient funds"

		else:
			id_cust.cust_balance -= data['balance']

			db.session.add(id_cust)
			db.session.commit()
			return jsonify({'message':id_cust.cust_balance})
	else:
		return jsonify({'message': 0}) #return 1 if success else return 0
		

@app.route('/transfer-fund', methods=['GET', 'POST'])
def transfer():
	data = request.get_json()
	# id_cust1 transfers the fund
	# id_cust2 recieves the fund
	id_cust1 = New_Acc.query.filter_by(cust_acc_num=data['acc_num1']).first()
	id_cust2 = New_Acc.query.filter_by(cust_acc_num=data['acc_num2']).first()


	if id_cust1 and id_cust2:
		if id_cust1.cust_balance >= data['fund']:
			id_cust1.cust_balance -= data['fund']
			id_cust2.cust_balance += data['fund']

			db.session.add(id_cust1)
			db.session.add(id_cust2)
			db.session.commit()
			
			return jsonify({'message': id_cust1.cust_balance}) #return 1 if success else return 0

		else:
			# Insufficient Funds
			return jsonify({'message': 0}) #return 1 if success else return 0
	else:
		print(id_cust1)
		print(id_cust2)
		#One of the account number is invalid
		return jsonify({'message': 0})

@app.route('/close-bank-account', methods=['POST'])
def deactivate():
	data = request.get_json()

	id_cust = New_Acc.query.filter_by(cust_acc_num=data['acc_num']).first()
	if id_cust:
		if id_cust.cust_status == 1:
			id_cust.cust_status = 0
			
			db.session.add(id_cust)
			db.session.commit()
			
			return jsonify({'message': 1})

		else:
			# Account is not active
			return jsonify({'message': 0})
	else:
		# account number is not found
		return jsonify({'message': 0})

@app.route('/Re-open-bank-account', methods=['POST'])
def activate():
	data = request.get_json()

	id_cust = New_Acc.query.filter_by(cust_acc_num=data['acc_num']).first()
	if id_cust:
		if id_cust.cust_status == 0:
			id_cust.cust_status = 1
			
			db.session.add(id_cust)
			db.session.commit()

			return jsonify({'message': 1})

		else:
			# Account is active 
			return jsonify({'message': 0})
	else:
		# account number is not found
		return jsonify({'message': 0})



	




def gen_pass():
	pass_ = []
	digit = random.randint(100000,999999)
	x = str(digit)
	return(x)

def gen_acc_num():
	acc = randint(0,10,13)
	 	
	return acc