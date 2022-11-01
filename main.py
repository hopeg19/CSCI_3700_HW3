from flask import Flask, render_template
import util

app = Flask(__name__)

username='raywu1990'
#username= 'garretthope'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

@app.route('/api/update_basket_a')
def update_basket_a():
    
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "INSERT into basket_a (a, fruit_a) values (5, 'Cherry')")
    if record == -1:
        # you can replace this part with a 404 page
        print('404 page was not found')
    else:
        # only use the first five rows
        log = 'Success'
    # disconnect from database
    util.disconnect_from_db(connection,cursor)
    # using render_template function, Flask will search
    # the file named index.html under templates folder
    return render_template('update_basket_a.html', log_html = log)

@app.route('/api/unique')
def display_unique():
	cursor, connection = util.connect_to_db(username,password,host,port,database)
	record = util.run_and_fetch_sql(cursor, "Select a, fruit_a, b, fruit_b From basket_a FULL JOIN basket_b ON fruit_a = fruit_b Where a IS NULL OR b IS NULL")
	if record == -1:
		print('404 page was not found')
	else:
		col_names = [desc[0] for desc in cursor.description]
		log = record[:10]
	util.disconnect_from_db(connection, cursor)
	return render_template('unique.html', log_html = log, table_title = col_names)

if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

