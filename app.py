from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Hello World!</h1>
        <p>Saya Salma Salsabila dari Universitas Brawijaya</p>
        <a href="/form">Go to Form</a>
    '''

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        return f"Thank you, {name}! We have received your email: {email}"
    
    return render_template_string('''
        <form method="post">
            Name: <input type="text" name="name"><br>
            Email: <input type="email" name="email"><br>
            <input type="submit">
        </form>
    ''')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
