from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Flask route for the calculator page
@app.route('/')
def index():
    return render_template('calculator.html')

# Route to handle the calculation
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        data = request.get_json()
        expression = data['expression']
        result = eval(expression) 
        return jsonify(result=result)
    except Exception as e:
        return jsonify(result="Error")

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
