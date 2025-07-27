import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

st.title("🛒 Sales Forecasting Dashboard")
st.write("Enter the product and outlet details below to estimate the sales:")

# User input
item_weight = st.number_input("📦 Item Weight", 0.0, 25.0, step=0.1)
fat_content = st.selectbox("🍔 Fat Content", [0, 1], format_func=lambda x: "Low Fat" if x == 0 else "Regular")
item_visibility = st.slider("👁️ Item Visibility", 0.0, 0.3, step=0.01)
item_type = st.number_input("🧃 Item Type Code", 0, 50)
item_mrp = st.number_input("💰 Item MRP", 0.0, 500.0)
establishment_year = st.number_input("🏢 Outlet Establishment Year", 1985, 2025)
outlet_size = st.selectbox("🏬 Outlet Size", [0, 1, 2], format_func=lambda x: ["High", "Medium", "Small"][x])
location_type = st.selectbox("📍 Location Type", [0, 1, 2], format_func=lambda x: f"Tier {x+1}")
outlet_type = st.selectbox("🏪 Outlet Type", [0, 1, 2, 3])
item_category = st.selectbox("📂 Item Category", [0, 1, 2], format_func=lambda x: ["Food", "Non-Consumable", "Drinks"][x])

# Convert to dataframe
user_input = pd.DataFrame([[item_weight, fat_content, item_visibility, item_type, item_mrp,
                            establishment_year, outlet_size, location_type, outlet_type, item_category]],
                          columns=['Item_Weight', 'Item_Fat_Content', 'Item_Visibility', 'Item_Type',
                                   'Item_MRP', 'Outlet_Establishment_Year', 'Outlet_Size',
                                   'Outlet_Location_Type', 'Outlet_Type', 'Item_Category'])

if st.button("🔮 Predict Sales"):
    prediction = model.predict(user_input)
    st.success(f"Estimated Sales: ₹ {round(prediction[0], 2)}")
