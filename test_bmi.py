from bmi import calculate_bmi
import pytest


#Test cases using Weak N X 1 Boundary Testing

# Testing Values UnderWeight
test_info_kn = calculate_bmi(57,180)
test_info_ob_under = calculate_bmi(411,89.0)
test_info_cvb_under = calculate_bmi(411,89.5)

@pytest.mark.parametrize("input,expected",[(test_info_kn['Category'],"Overweight"),(test_info_ob_under['Category'],"Underweight"),(test_info_cvb_under['Category'],"Normal")])
def test_underweight_bmi(input,expected):
    #Known passing case 
    assert  input == expected


# Testing Values Normal
test_info_kn = calculate_bmi(57,180)
test_info_ob_under = calculate_bmi(59,164.5)
test_info_cvb_under = calculate_bmi(59,165.0)

#Test cases using Weak N X 1 Boundary Testing

@pytest.mark.parametrize("input,expected",[(test_info_kn['Category'],"Overweight"),(test_info_ob_under['Category'],"Normal"),(test_info_cvb_under['Category'],"Overweight")])
def test_normal_weight_bmi(input,expected):
    #Known passing case 
    assert  input == expected


# Testing Values Overweight
test_info_kn = calculate_bmi(57,180)
test_info_ob_under = calculate_bmi(59,198.0)
test_info_cvb_under = calculate_bmi(59,198.5)

#Test cases using Weak N X 1 Boundary Testing

@pytest.mark.parametrize("input,expected",[(test_info_kn['Category'],"Overweight"),(test_info_ob_under['Category'],"Overweight"),(test_info_cvb_under['Category'],"Obese")])
def test_overweight_bmi(input,expected):
    #Known passing case 
    assert  input == expected