from api import db


class New_Acc(db.Model):
	"""docstring for Account"""
	__tablename__ = 'new_acc'
	cust_id = db.Column(db.Integer, primary_key=True)
	cust_fname = db.Column(db.String(50), nullable=False)
	cust_mname = db.Column(db.String(50), nullable=False)
	cust_lname = db.Column(db.String(50), nullable=False)
	cust_balance = db.Column(db.Float, default=0) #initial balance is set to 0
	cust_status = db.Column(db.Integer, default=1) #1 for active and 0 for inactive
	cust_acc_pass = db.Column(db.String(6), nullable=False)
	cust_acc_num = db.Column(db.String(13), nullable=False, unique = True)




	def __init__(self, cust_fname, cust_mname, cust_lname, cust_balance, cust_status, cust_acc_pass, cust_acc_num):
		
		self.cust_fname = cust_fname
		self.cust_mname = cust_mname
		self.cust_lname = cust_lname
		self.cust_balance = cust_balance
		self.cust_status = cust_status
		self.cust_acc_pass = cust_acc_pass
		self.cust_acc_num = cust_acc_num