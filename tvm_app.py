import  streamlit as st
import numpy as np
import numpy_financial as npf


# 
st.title("Time Value of Money Calculator")
principal = st.number_input("Enter principal amount", value=1000)
rate = st.number_input("Enter annual interest rate (in %)", value=5.0)    
years = st.number_input("Enter number of years", value=5)  
compounding_periods = st.number_input("Enter number of compounding periods per year", value=12)



calculation = st.selectbox("Select calculation", ["Future Value", "Present Value"])



def future_value():
    fv = npf.fv(rate/100, years, principal, compounding_periods)  
    st.write("Future value = ", fv)

def present_value():
    pv = npf.pv(rate/100, years, 0, principal) 
    st.write("Present value = ", pv)




if calculation == "Future Value":
    future_value()
else:
    present_value()