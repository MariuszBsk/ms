from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def expand_and_cumulate(numbers, reverse=False):
    numbers_list = numbers.split()
    expanded_numbers = []
    
    # Expand values like "150*5" into [150, 150, 150, 150, 150]
    for num in numbers_list:
        if '*' in num:
            try:
                val, repeat = num.split('*')
                expanded_numbers.extend([int(val)] * int(repeat))
            except ValueError:
                continue
        else:
            try:
                expanded_numbers.append(int(num))
            except ValueError:
                continue
    
    # Apply cumulation
    if reverse:
        expanded_numbers.reverse()

    cumulative_sum = 0
    results = []
    for value in expanded_numbers:
        cumulative_sum += value
        results.append(f"- {cumulative_sum}")

    return results

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cumulate', methods=['GET'])
def cumulate():
    direction = request.args.get('direction', 'left')
    values = request.args.get('values', '')
    
    result = expand_and_cumulate(values, reverse=(direction == 'right'))
    
    return jsonify({"result": result})

@app.route('/generate-image', methods=['GET'])
def generate_image():
    return jsonify({"message": "Feature not implemented yet"})

if __name__ == '__main__':
    app.run(debug=True)

