## Python test for flask to test locally
import requests as r
import pandas as pd
import json


base_url = 'http://127.0.0.1:5000/' 

json_data = {
            "Gender": "Male",
            "Married": "Yes",
            "Dependents": 2,
            "Education": "Graduate",
            "Self_Employed": "Yes",
            "ApplicantIncome": 4400,
            "CoapplicantIncome": 1500,
            "LoanAmount": 100.0,
            "Loan_Amount_Term": 360.0,
            "Credit_History": 1.0,
            "Property_Area": "Rural",
            "Total_Income": 5900
            }

# Get Response
# response = r.get(base_url)
response = r.post(base_url + "prediction", json = json_data)
print(response.text)