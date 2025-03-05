import streamlit as st
import requests

# Title of the app
st.title("Real Estate Questionnaire")

# Introduction
st.write("Please answer the following questions to help us understand your real estate needs.")

# Question 1: Property Type
property_type = st.selectbox(
    "1. What type of property are you interested in?",
    options=["Single-family home", "Condo", "Townhouse", "Multi-family home", "Commercial property"]
)

# Question 2: Budget
budget = st.slider(
    "2. What is your budget range?",
    min_value=50000, max_value=2000000, value=(200000, 500000)
)

# Question 3: Location Preference
location = st.text_input(
    "3. What is your preferred location or neighborhood?",
    placeholder="Enter your preferred location"
)

# Question 4: Number of Bedrooms
bedrooms = st.number_input("4. How many bedrooms do you need?", min_value=1, max_value=10, value=3)

# Question 5: Number of Bathrooms
bathrooms = st.number_input("5. How many bathrooms do you need?", min_value=1, max_value=10, value=2)

# Question 6: Square Footage
square_footage = st.slider("6. What is your desired square footage?", min_value=500, max_value=10000, value=1500)

# Question 7: Move-in Timeline
timeline = st.radio(
    "7. What is your preferred move-in timeline?",
    options=["Immediately", "1-3 months", "3-6 months", "6+ months"]
)

# Question 8: Must-Have Features
features = st.multiselect(
    "8. What are your must-have features?",
    options=["Pool", "Garage", "Backyard", "Open floor plan", "Modern kitchen", "Energy-efficient"]
)

# Question 9: Financing Option
financing = st.radio("9. What is your preferred financing option?", options=["Cash", "Mortgage", "Lease"])

# Question 10: Languages Spoken
languages = st.multiselect(
    "10. What languages do you speak?",
    options=["English", "Spanish", "French", "German", "Chinese", "Hindi", "Arabic", "Other"]
)

# Question 11: Additional Comments
comments = st.text_area("11. Do you have any additional comments or specific requirements?", placeholder="Enter additional comments")

# Allow user to select analysis role
selected_roles = st.multiselect(
    "Select Analysis Types",
    options={"7": "Real Estate Insights", "9": "Market Trend Analysis"},
    default=["7"]
)

# Submit button
if st.button("Submit"):
    responses = {
        "property_type": property_type,
        "budget": budget,
        "location": location,
        "bedrooms": bedrooms,
        "bathrooms": bathrooms,
        "square_footage": square_footage,
        "timeline": timeline,
        "features": features,
        "financing": financing,
        "languages": languages,
        "comments": comments,
    }

    api_url = 'http://localhost:8001/api/v1/chatgroq'  # Update with your actual API endpoint

    # Function to handle API requests
    def get_analysis(role):
        payload = {"role": role, "msg": str(responses)}
        try:
            response = requests.post(api_url, json=payload)
            if response.status_code == 200:
                return response.json()[0].strip('[]"')
            else:
                return f"Failed to generate report (Status Code: {response.status_code})"
        except Exception as e:
            return f"An error occurred: {e}"

    # Process all selected roles
    for role in selected_roles:
        analysis_result = get_analysis(role)
        st.success(f"Analysis Report for Role {role}:")
        st.write(analysis_result)
