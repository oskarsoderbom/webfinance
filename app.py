from flask import Flask, render_template, request

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
        arg1 = float(request.form['arg1'])
        arg2 = float(request.form['arg2'])
        arg3 = float(request.form['arg3'])
        arg4 = float(request.form['arg4'])
        arg5 = float(request.form['arg5'])

        result1 = function_1(arg1)
        result2 = function_2(arg2)
        result3 = function_3(arg3)
        result4 = function_4(arg4)
        result5 = function_5(arg5)

        return render_template('result.html', result1=result1, result2=result2, result3=result3, result4=result4, result5=result5)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
