import streamlit as st

# Initialize session state for gym_ledger
if "gym_ledger" not in st.session_state:
    st.session_state.gym_ledger = {
        1001: {"name": "Alice Johnson", "membership": "Active", "type": "Monthly"},
        1002: {"name": "Bob Smith", "membership": "Inactive", "type": "Yearly"},
        1003: {"name": "Charlie Lee", "membership": "Active", "type": "Weekly"}
    }

st.title("🏋️ Gym Membership Ledger")

# Add a new member
st.header("Add New Member")
with st.form("add_member_form"):
    new_id = st.number_input("Member ID", min_value=1000, step=1)
    new_name = st.text_input("Name")
    new_status = st.selectbox("Membership Status", ["Active", "Inactive"])
    new_type = st.selectbox("Membership Type", ["Weekly", "Monthly", "Yearly"])
    submitted = st.form_submit_button("Add Member")

    if submitted:
        if new_id in st.session_state.gym_ledger:
            st.warning(f"Member ID {new_id} already exists.")
        else:
            st.session_state.gym_ledger[new_id] = {
                "name": new_name,
                "membership": new_status,
                "type": new_type
            }
            st.success(f"Member {new_name} added successfully!")

# Update membership status
st.header("Update Membership Status")
with st.form("update_status_form"):
    update_id = st.number_input("Enter Member ID to Update", min_value=1000, step=1, key="update_id")
    new_status_update = st.selectbox("New Status", ["Active", "Inactive"], key="status_update")
    update_btn = st.form_submit_button("Update Status")

    if update_btn:
        if update_id in st.session_state.gym_ledger:
            st.session_state.gym_ledger[update_id]["membership"] = new_status_update
            st.success(f"Membership status for {st.session_state.gym_ledger[update_id]['name']} updated to {new_status_update}.")
        else:
            st.error("Member ID not found.")

# Display the ledger
st.header("📋 Current Gym Members")
for member_id, details in st.session_state.gym_ledger.items():
    st.write(f"**ID:** {member_id} | **Name:** {details['name']} | **Status:** {details['membership']} | **Type:** {details['type']}")
