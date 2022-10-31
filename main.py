from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/api/update_basket_a')
@app.route('/api/unique')

def update_basket_a():
    
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "  ")
    if record == -1:
        # you can replace this part with a 404 page
        print('Something is wrong with the SQL command')
    else:
        # only use the first five rows
        log = record[:5]
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('index.html', log_html = log)

def display_unique():
	cursor, connection = util.connect_to_db(username,password,host,port,database)
	record = util.run_and_fetch_sql(cursor, "  ")
	if record == -1:
		print('Something is wrong with the SQL command')
	else:
		log = record[:5]
	util.disconnect_from_db(connection, cursor)
	return render_template('index.html', log_html = log)

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

