from flask import Flask, request, render_template

app = Flask(__name__)

# define five example functions that take one argument each
def function_1(arg):
    return arg*1

def function_2(arg):
    return arg*2

def function_3(arg):
    return arg*3

def function_4(arg):
    return arg*4

def function_5(arg):
    return arg*5

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # retrieve up to five user inputs from the form
        user_inputs = [request.form.get(f'user_input_{i+1}', '') for i in range(5)]
        # call the five functions with the user inputs as arguments
        results = [f(user_input) for f, user_input in zip([function_1, function_2, function_3, function_4, function_5], user_inputs)]
        # pass the results to the template
        return render_template('result.html', results=results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
