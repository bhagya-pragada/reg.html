from flask import Flask, request, render_template
app=Flask(__name__)
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'post':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        return
        render_template('sucess.html')
        return
        render_template('Register.html')
        if__name__='__main__':
        app.run(host='0.0.0.0')