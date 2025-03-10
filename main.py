import pandas as pd
import streamlit as st

st.title("Spending Tracker")
col1,col2 = st.columns([5,5])

def get_data():
  csv = pd.read_csv("data.csv")
  return csv

if 'csv' not in st.session_state:
  st.session_state.csv = get_data();
csv = st.session_state.csv

col1.write("### Spending by Month")
col1.bar_chart(csv.set_index("month")["nominal"])
col2.write("### Spending by Category")
col2.bar_chart(csv.set_index("category")["nominal"])
edited_df = st.data_editor(csv)
save_btn = st.button("Save Changes")

if save_btn:
  edited_df.to_csv("data.csv", index=False)
  st.rerun()



spend_id = st.text_input("Spend Id")
month = st.selectbox("Month", ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', "December"])
category = st.selectbox("Category", ['Food & Drinks', 'Bills', "Education", "Family Needs", "Gift & Charity", "Groceries", "Health & Personal Care", "Hobby & Entertainment", "Loans", "Saving & Investment", "Shopping", "Sports", "Transportation", "Traveling", "Others"])
description = st.text_input("Description")
nominal = st.number_input('Nominal (IDR)', step=100)
submit = st.button('Add')

if submit:
  new_data = pd.DataFrame([[spend_id, month, category, description, nominal]], columns=["id", "month", "category", "description", "nominal"])
  csv = pd.concat([csv, new_data], ignore_index=True)
  csv.to_csv("data.csv", index=False)
  st.rerun()
