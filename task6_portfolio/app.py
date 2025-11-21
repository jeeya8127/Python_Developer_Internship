from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '03c0f4618fd23c904f4371b5621f3683353b2cc49781e152' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        print(f"New submission received:")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Message: {message}")

        flash('Thank you! Your message has been sent successfully.', 'success')
        return redirect(url_for('index'))
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)