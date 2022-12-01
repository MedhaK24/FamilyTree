from flask import Flask, render_template
app=Flask(__name__,template_folder='Templates')
@app.route('/Nidhi')
def showNidhi():
    return render_template('Nidhi.html')
@app.route('/Medha')
def showMedha():
    return render_template('Medha.html')
@app.route('/Mom')
def showMom():
    return render_template('Mom.html')
@app.route('/Dad')
def showDad():
    return render_template('Dad.html')
app.run(debug=True)