from flask_wtf import FlaskForm 
from wtforms.fields import FloatField,SubmitField
from wtforms.validators import InputRequired

class BMIForm(FlaskForm):
    height          = FloatField("Height ",
                            validators=[
                                InputRequired("Input is required!"),
                            ])
    weight          = FloatField("Weight ",
                            validators=[InputRequired("Input is required!"),
                            ])
    submit          = SubmitField("Calculate")

    
        

