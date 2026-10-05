from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory linked list storage
linked_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/works/string-converter', methods=['GET', 'POST'])
def string_converter():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/works/area/circle', methods=['GET', 'POST'])
def acircle():
    result = None
    error = None
    if request.method == 'POST':
        try:
            radius = float(request.form.get('radius', '0'))
            if radius < 0:
                error = "Radius must be positive"
            else:
                result = round(radius * radius * 3.14159, 2)
        except ValueError:
            error = "Please enter a valid number"
    return render_template('circle.html', result=result, error=error)

@app.route('/works/area/triangle', methods=['GET', 'POST'])
def atriangle():
    result = None
    error = None
    if request.method == 'POST':
        try:
            base = float(request.form.get('base', '0'))
            height = float(request.form.get('height', '0'))
            if base < 0 or height < 0:
                error = "Base and height must be positive"
            else:
                result = round((base * height) / 2, 2)
        except ValueError:
            error = "Please enter valid numbers"
    return render_template('triangle.html', result=result, error=error)

@app.route('/works/linkedlist', methods=['GET', 'POST'])
def linkedlist():
    global linked_list

    if request.method == 'POST':
        action = request.form.get('action', '')

        if action == 'add':
            value = request.form.get('value', '').strip()
            if value:
                linked_list.append(value)
        elif action == 'remove':
            index = int(request.form.get('index', '-1'))
            if 0 <= index < len(linked_list):
                linked_list.pop(index)
        elif action == 'clear':
            linked_list = []

    return render_template('linkedlist.html', items=linked_list)

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
