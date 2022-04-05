from flask import Blueprint,render_template,request,redirect,url_for,session
from app.main.forms import BMIForm
from bmi import calculate_bmi

main = Blueprint('main',__name__,template_folder='templates')

@main.route("/",methods=['GET','POST'])
def home():
    form  = BMIForm()
    if request.method == 'POST':
        height = form.height.data
        weight = form.weight.data

        user_info = calculate_bmi(height,weight)
        session['user_info'] = user_info
        return redirect(url_for("main.results"))


    return render_template('home.html',form=form)

@main.route("/results",methods=['GET'])
def results():
    user_info  = session.get('user_info')
    return render_template('results.html',user_info=user_info)
