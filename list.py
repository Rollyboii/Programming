from flask import Flask

app = Flask(__name__)

sample_list = ['Rolly','Alessandra','Shenron','Angelo']

@app.route('/')

def index():
    
    return ','.join(sample_list)

if __name__ == '__main__':
    app.run(debug=True)