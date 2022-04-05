def main():
    #Flags for while loops

    x=0 
    y=0

    #Loops until valid height input is entered  
    while x == 0:
        #Prompts user to enter Height information
        print("Enter your height in feet and inches: ")

        #Prompts user for height
        try:
            height  = float(input())
            if height > 0 :
                x=1
                continue
            else:
                print("Please Enter a Non-Zero Integer")
        except  ValueError:
            print("Please Enter a Non-Zero Integer")

    #Loops until valid weight input is entered
    while y == 0:

        #Prompts the user to enter their weight information 
        print("Enter your weight in pounds: ")
        try: 
            weight  = float(input())
            if weight > 0 :
                y=1
                continue
            else:
                print("Please Enter a Non-Zero integer")
        except ValueError:
            print("Please Enter a Non-Zero Integer")




    #Displays entered values 
    #print(f"Height : {h_feet}ft {h_inches}in  Weight: {weight}lbs")
    
    #user_bmi = calculate_bmi(h_feet,h_inches,weight)
    #display_bmi(user_bmi)

def calculate_bmi(height,weight):

    if height % 100 == height: 
        #Finds the inches (h_inches) over the lowest "ten" value i.e. height = 53 , inches over tenth  = 3 
        h_inches = height % 10

        #Finds the number of feet(h_feet)  i.e. height = 53 , (53 - 3 ) / 10  = 5 
        h_feet  = (height - h_inches) / 10
    else: 
        
        h_inches = height % 100

        h_feet = (height - h_inches) / 100


    
    #Converts the calculated height values back to integers as math operations convert them to float vals
    h_feet = int(h_feet)
    h_inches = int(h_inches)

    #multiply the weight in pounds by the metric conversion factor
    kg_weight  = weight * 0.45 

    #Calulate the total inches in height
    total_height_inches  = (h_feet * 12 ) + h_inches

    #Multiply the height in inches by the metric conversion factor
    
    m_height = total_height_inches * 0.025

    #Square the height in meters

    m2_height = m_height * m_height

    # Divide the weight by the height^2 - format to 2 decimal places

    user_bmi  = float("{:.1f}".format(kg_weight / m2_height))

    category = ""

    #if bmi is less than 18.5 - Underweight
    if user_bmi < 18.5:
        category = "Underweight"
    #if bmi is greater that 18.5 and less than equal 24.9 - Normal
    elif user_bmi >= 18.5 and user_bmi <= 24.9:
        category = "Normal"
    #if bmi is greater than equal to 25 and less than equal to 29.9 - Overweight
    elif user_bmi >= 25 and user_bmi <= 29.9:
        
        category = "Overweight"
    elif user_bmi  >= 30:
    #if bmi is greater than 30 - Overweight
        category = "Obese"
   
    #return user info in a dictionary
    user_info  = { "BMI" : user_bmi, "Category": category}


    return user_info


def display_bmi(user_info):

    #if bmi is less than 18.5 - Underweight
    if user_info['Category'] == "Underweight":
        print(f"BMI: {user_info['BMI']}, Classification: Underweight")
    #if bmi is greater that 18.5 and less than equal 24.9 - Normal
    elif user_info['Category'] == "Normal":
        print(f"BMI: {user_info['BMI']}, Classification: Normal")
    #if bmi is greater than equal to 25 and less than equal to 29.9 - Overweight
    elif user_info['Category'] == "Overweight":
        print(f"BMI: {user_info['BMI']}, Classification: Overweight")
    else:
    #if bmi is greater than 30 - Overweight
        print(f"BMI: {user_info['BMI']}, Classification: Obese")


