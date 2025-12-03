import flask
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/Submit',methods=["POST"])
def submit():
    username=request.form["username"]
    email=request.form["emailid"]
    return render_template('submitted.html',name=username,email=emailid)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
