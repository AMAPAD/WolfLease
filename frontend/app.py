'''
Copyright 2023 Ashwattha Phatak, Anish Mulay, Akshay Dongare

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import streamlit as st
import requests
import pandas as pd
from datetime import datetime
import os
from groq import Groq
import random
import json
# Define your base URL for API requests
BASE_URL = "https://wolflease.onrender.com/"

def create_user():
    st.title("Create a New User")

    with st.form("user_form"):
        username = st.text_input("Username") or None
        name = st.text_input("Name") or None
        email = st.text_input("Email") or None
        contact_number = st.text_input("Contact Number") or None
        password = st.text_input("Password", type="password") or None
        dob = st.date_input("Date of Birth")
        gender = st.selectbox("Gender", ["M", "F", "O"]) or None
        user_type = st.selectbox("User Type", ["User", "Owner"]) or None
        pref_smoking = st.selectbox("Smoking Preference", ["Y", "N"]) or None
        pref_drinking = st.selectbox("Drinking Preference", ["Y", "N"]) or None
        pref_veg = st.selectbox("Vegetarian Preference", ["Y", "N"]) or None
        hobbies = st.multiselect("Hobbies", ["Reading", "Traveling", "Cooking", "Sports", "Music", "Art", "Gaming", "Technology"]) or None
        roommate_preferences = st.text_area("What are you looking for in a roommate?") or None
        personal_info = st.text_area("What do you want others to know about you?") or None
        submitted = st.form_submit_button("Create User")

    if submitted:
        user_data = {
            "username": username,
            "name": name,
            "contact_email": email,
            "contact_number": contact_number,
            "password": password,
            "dob": str(dob) if dob else None,
            "gender": gender,
            "user_type": user_type,
            "pref_smoking": pref_smoking,
            "pref_drinking": pref_drinking,
            "pref_veg": pref_veg,
            "hobbies": ', '.join(hobbies) if hobbies else None,
            "roommate_preferences": roommate_preferences,
            "personal_info": personal_info
        }

        response = requests.post(f"{BASE_URL}users/", json=user_data)

        if response.status_code == 201:
            st.success("User created successfully! Please log in.")
            st.session_state.registering = False
        else:
            st.error(f"Error creating user: {response.text}")

# Function for user login
def login():
    st.subheader("Login")
    contact_email = st.text_input("Email")
    password = st.text_input("Password", type='password')

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login"):
            response = requests.post(f"{BASE_URL}login/", json={'contact_email': contact_email, 'password': password})
            if response.status_code == 200:
                st.session_state.logged_in = True
                st.session_state.user_id = response.json().get('user_id')
                st.session_state.sessionid = response.json().get('sessionid')
                st.success(f"Login successful!")
                st.rerun()  # Refresh to reflect login
            else:
                st.error("Invalid credentials")
    
    with col2:
        if st.button("Register"):
            st.session_state.registering = True
            st.rerun()

def flat_page():
    # Define CSS for different rating levels
    review_box_style = """
    <style>
    .review-box {
        border: 1px solid #ddd;
        padding: 5px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: black;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);  /* Add shadow */
    }
    .rating-high {
        background-color: #006400;  /* Dark green */
    }
    .rating-medium {
        background-color: #FF8C00;  /* Dark orange */
    }
    .rating-low {
        background-color: #B22222;  /* Firebrick red */
    }
    </style>
    """
    st.markdown(review_box_style, unsafe_allow_html=True)

    current_user_id = "actual_user_id"

    # Fetch flats data
    response = requests.get(f"{BASE_URL}flats/")
    if response.status_code == 200:
        flats = response.json()
        for flat in flats:
            with st.expander(f"Flat {flat['flat_identifier']}"):
                col1, col2 = st.columns(2)
                col1.write(f"**Owner:** {flat['ownername']}")
                col1.write(f"**Apartment:** {flat['associated_apt_name']}")
                col2.write(f"**Rent:** ${flat['rent_per_room']}")
                col2.write(f"**Available:** {'Yes' if flat['availability'] else 'No'}")

                # Add a filter selection widget with a unique key
                rating_filter = st.selectbox(
                    "Filter reviews by rating:",
                    options=["All", "Best", "Average", "Worst"],
                    index=0,
                    key=f"rating_filter_{flat['id']}"
                )

                # Fetch reviews for this flat
                reviews_response = requests.get(f"{BASE_URL}flats/{flat['id']}/reviews/")
                if reviews_response.status_code == 200:
                    reviews = reviews_response.json()
                    st.subheader("Reviews")
                    if reviews:
                        # Apply the filter to the reviews
                        if rating_filter == "Best":
                            reviews = [review for review in reviews if review['rating'] >= 4]
                        elif rating_filter == "Average":
                            reviews = [review for review in reviews if review['rating'] == 3]
                        elif rating_filter == "Worst":
                            reviews = [review for review in reviews if review['rating'] <= 2]

                        for review in reviews:
                            rating_class = (
                                "rating-high" if review['rating'] >= 4
                                else "rating-medium" if review['rating'] == 3
                                else "rating-low"
                            )
                            st.markdown(
                                f"""
                                <div class="review-box {rating_class}">
                                    <p><strong>Rating:</strong> {review['rating']}/5</p>
                                    <p><strong>Comment:</strong> {review['comment']}</p>
                                </div>
                                """,
                                unsafe_allow_html=True
                            )
                    else:
                        st.write("No reviews yet.")
                else:
                    st.error("Failed to fetch reviews.")

                # Review submission form
                st.subheader("Submit a Review")
                with st.form(key=f"review_form_{flat['flat_identifier']}"):
                    rating = st.slider("Rating", 1, 5, 3)
                    comment = st.text_area("Comment")
                    submit_button = st.form_submit_button("Submit Review")

                    if submit_button:
                        # Make POST request to submit the review
                        review_data = {
                            "flat": flat['id'],
                            "user": current_user_id,  # Replace with the actual user ID
                            "rating": rating,
                            "comment": comment
                        }
                        reviews_response = requests.post(
                            f"{BASE_URL}flats/{flat['id']}/reviews/",
                            json=review_data
                        )

                        if reviews_response.status_code == 201:
                            st.success("Review submitted successfully!")
                        else:
                            st.error(f"Failed to submit review: {reviews_response.json()}")
    else:
        st.error("Failed to fetch flats data")


def user_page():
    st.title("User Management")

    response = requests.get(f"{BASE_URL}users/")
    if response.status_code == 200:
        users = response.json()
        df = pd.DataFrame(users)

        # Separate users and owners
        users_df = df[df['user_type'] == 'User']
        owners_df = df[df['user_type'] == 'Owner']

        # Display summary statistics
        col1, col2 = st.columns(2)
        col1.metric("Total Users", len(users_df))
        col2.metric("Total Owners", len(owners_df))

        # Function to display user/owner details
        def display_user_details(df, user_type):
            st.subheader(f"{user_type}s")
            if len(df) > 0:
                for _, user in df.iterrows():
                    with st.expander(f"{user_type}: {user['name']}"):
                        col1, col2 = st.columns(2)
                        col1.write(f"**Email:** {user['contact_email']}")
                        col1.write(f"**DOB:** {user['dob']}")
                        col1.write(f"**Gender:** {user['gender']}")
                        col2.write(f"**Smoke:** {'Yes' if user['pref_smoking'] == 'Y' else 'No'}")
                        col2.write(f"**Drink:** {'Yes' if user['pref_drinking'] == 'Y' else 'No'}")
                        col2.write(f"**Vegetarian:** {'Yes' if user['pref_veg'] == 'Y' else 'No'}")
            else:
                st.write(f"No {user_type.lower()}s found.")

        # Display users and owners in separate tabs
        tab1, tab2 = st.tabs(["Users", "Owners"])
        
        with tab1:
            display_user_details(users_df, "User")
        
        with tab2:
            display_user_details(owners_df, "Owner")

        # Add a search functionality
        st.subheader("Search Users/Owners")
        search_term = st.text_input("Enter name or email to search")
        if search_term:
            search_results = df[df['name'].str.contains(search_term, case=False) | 
                                df['contact_email'].str.contains(search_term, case=False)]
            if not search_results.empty:
                st.dataframe(search_results[['name', 'user_type', 'contact_email']], use_container_width=True)
            else:
                st.write("No results found.")

    else:
        st.error("Failed to fetch Users")


def lease_page():
    st.title("Lease Management")

    response = requests.get(f"{BASE_URL}leases/")
    if response.status_code == 200:
        leases = response.json()
        df = pd.DataFrame(leases)

        # Convert date strings to datetime objects
        df['lease_start_date'] = pd.to_datetime(df['lease_start_date'])
        df['lease_end_date'] = pd.to_datetime(df['lease_end_date'])

        # Calculate lease duration
        df['lease_duration'] = (df['lease_end_date'] - df['lease_start_date']).dt.days

        # Display summary statistics
        st.subheader("Lease Overview")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Leases", len(df))
        col2.metric("Active Leases", len(df[df['lease_end_date'] >= datetime.now()]))
        col3.metric("Avg. Lease Duration", f"{df['lease_duration'].mean():.0f} days")

        # Function to display lease details
        def display_lease_details(lease):
            with st.expander(f"Lease: {lease['lease_identifier']}"):
                col1, col2 = st.columns(2)
                col1.write(f"**Owner:** {lease['ownername']}")
                col1.write(f"**Tenant:** {lease['tenant_name']}")
                col1.write(f"**Start Date:** {lease['lease_start_date'].strftime('%Y-%m-%d')}")
                col2.write(f"**End Date:** {lease['lease_end_date'].strftime('%Y-%m-%d')}")
                col2.write(f"**Duration:** {lease['lease_duration']} days")
                
                # Calculate if the lease is active
                is_active = lease['lease_end_date'] >= datetime.now()
                status = "Active" if is_active else "Expired"
                col2.write(f"**Status:** {status}")

        # Display leases by tenant
        st.subheader("Leases by Tenant")
        tenants = df['tenant_name'].unique()
        selected_tenant = st.selectbox("Select Tenant", ["All"] + list(tenants))
        
        if selected_tenant == "All":
            tenant_leases = df
        else:
            tenant_leases = df[df['tenant_name'] == selected_tenant]
        
        for _, lease in tenant_leases.iterrows():
            display_lease_details(lease)

        # Display leases by apartment (assuming apartment name is part of the lease_identifier)
        st.subheader("Leases by Apartment")
        df['apartment'] = df['lease_identifier'].apply(lambda x: x.split('_')[0])
        apartments = df['apartment'].unique()
        selected_apartment = st.selectbox("Select Apartment", ["All"] + list(apartments))
        
        if selected_apartment == "All":
            apartment_leases = df
        else:
            apartment_leases = df[df['apartment'] == selected_apartment]
        
        for _, lease in apartment_leases.iterrows():
            display_lease_details(lease)

        # Add a search functionality
        st.subheader("Search Leases")
        search_term = st.text_input("Enter lease ID, tenant name, or owner name to search")
        if search_term:
            search_results = df[df['lease_identifier'].str.contains(search_term, case=False) | 
                                df['tenant_name'].str.contains(search_term, case=False) |
                                df['ownername'].str.contains(search_term, case=False)]
            if not search_results.empty:
                for _, lease in search_results.iterrows():
                    display_lease_details(lease)
            else:
                st.write("No results found.")

    else:
        st.error("Failed to fetch Leases")

def interest_page():
    st.title("User Interests")

    response = requests.get(f"{BASE_URL}interests/")
    if response.status_code == 200:
        interests = response.json()
        df = pd.DataFrame(interests)

        # Separate flat information
        df[['flat_name', 'floor', 'flat_number']] = df['flat_identifier'].str.split('_', expand=True)

        # Display summary statistics
        st.subheader("Interest Overview")
        col1, col2 = st.columns(2)
        col1.metric("Total Interests", len(df))
        col2.metric("Unique Users", df['username'].nunique())

        # Filter by user
        st.subheader("Filter by User")
        users = ["All"] + sorted(df['username'].unique().tolist())
        selected_user = st.selectbox("Select User", users)

        if selected_user != "All":
            filtered_df = df[df['username'] == selected_user]
        else:
            filtered_df = df

        # Display interests
        st.subheader("Interest Details")
        for _, interest in filtered_df.iterrows():
            with st.expander(f"{interest['username']} - {interest['flat_identifier']}"):
                col1, col2 = st.columns(2)
                col1.write(f"**User:** {interest['username']}")
                col1.write(f"**Apartment:** {interest['apartment_name']}")
                col2.write(f"**Flat Name:** {interest['flat_name']}")
                col2.write(f"**Floor:** {interest['floor']}")
                col2.write(f"**Flat Number:** {interest['flat_number']}")

        # Add a search functionality
        st.subheader("Search Interests")
        search_term = st.text_input("Enter username or flat identifier to search")
        if search_term:
            search_results = df[df['username'].str.contains(search_term, case=False) | 
                                df['flat_identifier'].str.contains(search_term, case=False)]
            if not search_results.empty:
                for _, interest in search_results.iterrows():
                    with st.expander(f"{interest['username']} - {interest['flat_identifier']}"):
                        col1, col2 = st.columns(2)
                        col1.write(f"**User:** {interest['username']}")
                        col1.write(f"**Apartment:** {interest['apartment_name']}")
                        col2.write(f"**Flat Name:** {interest['flat_name']}")
                        col2.write(f"**Floor:** {interest['floor']}")
                        col2.write(f"**Flat Number:** {interest['flat_number']}")
            else:
                st.write("No results found.")

        # Display interests by apartment
        st.subheader("Interests by Apartment")
        apartments = df['apartment_name'].unique()
        for apartment in apartments:
            with st.expander(f"Apartment: {apartment}"):
                apartment_interests = df[df['apartment_name'] == apartment]
                st.dataframe(apartment_interests[['username', 'flat_identifier']], use_container_width=True)

    else:
        st.error("Failed to fetch Interests Page")

def add_flat():
    st.title("Add New Flat")

    # Fetch apartments for the dropdown
    response = requests.get(f"{BASE_URL}apartments/")
    if response.status_code == 200:
        apartments = response.json()
        apartment_names = [apt['name'] for apt in apartments]
    else:
        st.error("Failed to fetch apartments")
        return

    # Fetch owners (users of type 'Owner') for the dropdown
    response = requests.get(f"{BASE_URL}users/?user_type=Owner")
    if response.status_code == 200:
        owners = response.json()
        owner_names = [owner['username'] for owner in owners]
    else:
        st.error("Failed to fetch owners")
        return

    with st.form("add_flat_form"):
        associated_apt_name = st.selectbox("Associated Apartment", apartment_names)
        floor_number = st.number_input("Floor Number", min_value=1, step=1)
        flat_number = st.number_input("Flat Number", min_value=1, step=1)
        availability = st.checkbox("Available")
        rent_per_room = st.number_input("Rent per Room", min_value=0, step=50)
        ownername = st.selectbox("Owner", owner_names)

        submitted = st.form_submit_button("Add Flat")

    if submitted:
        flat_data = {
            "associated_apt_name": associated_apt_name,
            "floor_number": floor_number,
            "flat_number": flat_number,
            "availability": availability,
            "rent_per_room": rent_per_room,
            "ownername": ownername
        }

        response = requests.post(f"{BASE_URL}flats/", json=flat_data)

        if response.status_code == 201:
            st.success("Flat added successfully!")
        else:
            st.error(f"Error adding flat: {response.text}")



# Function to display the dashboard
def dashboard():
    if st.session_state.get('logged_in', False):
        st.subheader("Dashboard")
        all_users_response = requests.get(f"{BASE_URL}users/")
        if all_users_response.status_code == 200 and all_users_response.json():
            all_users = all_users_response.json()
            user_info = next((user for user in all_users if user['id'] == st.session_state.user_id), None)
            st.markdown(f"### Welcome to your dashboard, {user_info.get('name')}!")
            st.subheader("Profile Details")
            # Display user details in a structured format
            col1, col2, col3 = st.columns(3)
            col1.metric("Username", user_info.get('username', 'N/A'))
            col1.metric("Name", user_info.get('name', 'N/A'), delta_color="off")
            col1.metric("Email", user_info.get('contact_email', 'N/A'))
            col2.metric("Contact Number", user_info.get('contact_number', 'N/A'))
            col2.metric("Date of Birth", user_info.get('dob', 'N/A'))
            col2.metric("Gender", user_info.get('gender', 'N/A'))
            col3.metric("Smoking Preference", user_info.get('pref_smoking', 'N/A'))
            col3.metric("Drinking Preference", user_info.get('pref_drinking', 'N/A'))
            col3.metric("Vegetarian", user_info.get('pref_veg', 'N/A'))
        else:
            st.error("Failed to fetch user details.")
    else:
        st.error("You are not logged in. Please log in to view the dashboard.")
    
    if st.button("Refresh"):
        st.experimental_rerun()

    st.subheader("Your Activity")
    total_logins = random.randint(0, 25)
    total_leases_signed = random.randint(0, 5)
    st.write(f"Total Logins: {total_logins}")
    st.write(f"Total Leases Signed: {total_leases_signed}")
        
def fetch_session():
    if 'session_data' not in st.session_state:
        response = requests.get('http://127.0.0.1:8000/session_data', cookies={"sessionid": st.session_state.get('sessionid')})
        if response.status_code == 200:
            st.session_state['session_data'] = response.json()
        else:
            st.warning("Session expired. Please log in again.")
            st.session_state.logged_in = False
            st.rerun()

def add_lease():
    tenants_list = None
    owner_list = None
    flat_identifier_list = None
    flat_response = requests.get(f"{BASE_URL}flats/")
    response = requests.get(f"{BASE_URL}users/")
    flat_list = None
    if response.status_code == 200:
        users = response.json()
        tenants_list = [user['username'] for user in users if user['user_type'] == 'User']
        owner_list = [user['username'] for user in users if user['user_type'] == 'Owner']
    else:
        st.error("Failed to fetch users")
        return
    if flat_response.status_code == 200:
        flat_list = flat_response.json()
        flat_identifier_list = [flat['flat_identifier'] for flat in flat_list]

    if tenants_list and owner_list:
        with st.form("add_lease_form"):
            lease_start_date = st.date_input("Lease Start Date")
            lease_end_date = st.date_input("Lease End Date")
            flat_identifier = st.selectbox("Flat", flat_identifier_list)
            tenant_name = st.selectbox("Tenant Name", tenants_list)
            ownername = st.selectbox("Owner Name",owner_list)
            submitted = st.form_submit_button("Create Lease")
        if submitted:
            data = {
                'lease_start_date': lease_start_date.isoformat(),
                'lease_end_date': lease_end_date.isoformat(),
                'tenant_name': tenant_name,
                'ownername': ownername,
                'flat_identifier': flat_identifier,
                'lease_identifier': flat_identifier+""+tenant_name
            }
            update_response = requests.post(f"{BASE_URL}leases/", json=data)
            if update_response.status_code == 201:
                st.success("Lease added successfully!")
            else:
                st.error(f"Error adding lease: {update_response.text}")


def tenant_rights_page():
    st.title("Tenant Rights")

    # Read the HTML file
    with open('rights.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    st.components.v1.html(html_content, height=600, scrolling=True)

def sign_lease():
    response = requests.get(f"{BASE_URL}users/")
    user_list = None
    lease_identifier_list = None
    if response.status_code == 200:
        users = response.json()
        user_list = [user['username'] for user in users if user['user_type'] == 'User']
    lease_response = requests.get(f"{BASE_URL}leases")
    if response.status_code == 200:
        lease_response = lease_response.json()
        lease_identifier_list = [lease['lease_identifier'] for lease in lease_response]
    print(user_list, lease_identifier_list)
    with st.form("sign_lease"):
        dob = st.date_input("Enter DOB")
        username = st.text_input("Username")
        lease_identifier = st.selectbox("Lease", lease_identifier_list)
        submitted = st.form_submit_button("Sign Lease")

    if submitted:
        update_response = requests.post(f"{BASE_URL}sign/{lease_identifier}/{username}/{dob}")
        if update_response.status_code == 200:
            st.success("Lease added successfully!")
        else:
            st.error(f"Error adding lease: {update_response.text}")

def profile_matching_page():
    st.title("Profile Matching")
    # Ensure the user is logged in
    if 'logged_in' in st.session_state and st.session_state.logged_in:
        # Fetch all users' preferences and attributes
        response = requests.get(f"{BASE_URL}users/")
        if response.status_code == 200:
            users = response.json()
            current_user = next((user for user in users if user['id'] == st.session_state.user_id), None)
            if current_user:
                # Prepare data for the LLM
                relevant_data = {
                    user['id']: {
                        'dob': user['dob'],
                        'gender': user['gender'],
                        'user_type': user['user_type'],
                        'preferences': {
                            'smoking': user['pref_smoking'],
                            'drinking': user['pref_drinking'],
                            'vegetarian': user['pref_veg'],
                            'hobbies': user['hobbies']
                        },
                        'roommate_preferences': user['roommate_preferences'],
                        'personal_info': user['personal_info']
                    } for user in users
                }
                print("relevant_data", relevant_data)
                prompt = json.dumps(relevant_data)
                # Call the guarded Groq API to get matches
                try:
                    api_key = os.getenv("GROQ_API_KEY")
                    groq_client = Groq(api_key=api_key)
                    response = groq_client.chat.completions.create(model="llama3-70b-8192", messages=[{"role": "system", "content": "Generate user matches based on preferences and comments. For each user, return a JSON with the format: {user1: [username and reason of top 3 matches], user2: [username and reason of top 3 matches], ...}.DO NOT OUTPUT ANYTHING ELSE. ONLY STRICTLY OUTPUT JSON. DONT OUTPUT ANY /n or anything else"},
                  {"role":"user", "content":"Here are the users: " + prompt}])
                    llm_response = response.choices[0].message.content
                    matches = json.loads(llm_response)
                    print(matches)
                    # Display the matches in a table
                    if matches:
                        st.subheader("Your Top Matches")
                        if str(current_user['id']) in matches:  
                            match_data = []
                            for match in matches[str(current_user['id'])]:
                                matched_user_id, reason = match
                                matched_username = next((user['username'] for user in users if user['id'] == matched_user_id), None)
                                if matched_username:
                                    match_data.append({"Matched User": matched_username, "Reason": reason})
                            if match_data:
                                st.table(match_data)
                            else:
                                st.write("No matches found for you.")
                        else:
                            st.write("No matches found for you.")
                    else:
                        st.write("No matches found.")
                except json.JSONDecodeError as e:
                    st.error("Failed to decode JSON from LLM response. Trying again without JSON format.")
                    try:
                        response = groq_client.chat.completions.create(model="llama3-70b-8192", messages=[{"role": "system", "content": "Generate user matches based on preferences and comments. For each user, return the matches in plain text."},
                      {"role":"user", "content":"Here are the users: " + prompt}])
                        llm_response = response.choices[0].message.content
                        st.write(llm_response)
                    except Exception as e:
                        st.error(f"Failed to process matching on second attempt: {str(e)}")
                except Exception as e:
                    st.error(f"Failed to process matching: {str(e)}")
            else:
                st.error("Current user data not found.")
        else:
            st.error("Failed to fetch user data")
    else:
        st.warning("Please log in to view your matches.")


def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if 'registering' not in st.session_state:
        st.session_state.registering = False
    
    if st.session_state.logged_in:
        page = st.sidebar.selectbox("Select Page", ["User Dashboard", "Flats", "Users", "Leases", "Interests", "Add Flats", "Add Lease", "Sign Lease", "Tenant Rights", "Profile Matching"])
        if page == "Flats":
            flat_page()
        elif page == "User Dashboard":
            dashboard()
        elif page == "Users":
            user_page()
        elif page == "Leases":
            lease_page()
        elif page == "Interests":
            interest_page()
        elif page == "Add Flats":
            add_flat()
        elif page == "Add Lease":
            add_lease()
        elif page == "Sign Lease":
            sign_lease()
        elif page == "Tenant Rights":
            tenant_rights_page()
        elif page == "Profile Matching":
            profile_matching_page()
        
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.rerun()
    else:
        if st.session_state.registering:
            create_user()
            if st.button("Back to Login"):
                st.session_state.registering = False
                st.rerun()
        else:
            login()



if __name__ == "__main__":
    main()


