from flask import Flask, request

app = Flask(__name__)

@app.route('/<string:str>', methods=["GET"])
def reverse_str(str):
	return str[::-1]
	
if __name__ == '__main__':
	app.run()
