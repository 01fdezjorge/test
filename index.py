from flask import Flask, render_template, url_for
from datetime import datetime

app = Flask(__name__)
app.config['LEAFMOBIL_DATABASE_URL'] = 'sqlite:///LeafMobilDatabse.db'
# db = SQLAlchemy(app)

# class TodoList(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self):
#         return '<Task %r>' % self.id

@app.route('/', methods=['POST', 'GET'])
def home():
	return render_template('index.html')

@app.route('/location')
def location():
	return render_template('location.html')

@app.route('/cars')
def cars():
	return render_template('cars.html')

@app.route('/rating')
def rating():
	return render_template('rating.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

if __name__ == "__main__":
	app.run(debug=True)