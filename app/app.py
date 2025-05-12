# streamlit_app/app.py
import streamlit as st
import requests
import os
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Morning Market Brief",
    page_icon="📈",
    layout="wide"
)

# App title and description
st.title("📈 Morning Market Brief")
st.markdown("Get the latest market insights for your day.")

# Sidebar for configuration
with st.sidebar:
    st.header("Settings")
    api_url = st.text_input("API URL", value="http://localhost:8000/brief")
    st.info("Make sure your API server is running at the specified URL.")

# Main content area
st.subheader(f"Market Brief for {datetime.now().strftime('%B %d, %Y')}")

# Audio upload option
uploaded_file = st.file_uploader("Upload audio file (optional)", type=['wav', 'mp3'])

# Get brief button
if st.button("Get Market Brief", type="primary"):
    with st.spinner("Fetching market brief..."):
        try:
            if uploaded_file:
                # Use uploaded file
                response = requests.post(api_url, files={"audio": uploaded_file})
            else:
                # No file provided - API should use default source
                response = requests.post(api_url)
            
            if response.status_code == 200:
                brief_data = response.json()
                
                # Display the response in a nice format
                st.success("Market brief generated successfully!")
                
                with st.container():
                    st.markdown("### Today's Market Summary")
                    st.markdown(brief_data['response'])
                    
                    # You could add more structured data display here if your API returns it
                    if 'key_points' in brief_data:
                        st.markdown("### Key Points")
                        for point in brief_data['key_points']:
                            st.markdown(f"- {point}")
                    
                    if 'tickers' in brief_data:
                        st.markdown("### Top Tickers")
                        cols = st.columns(3)
                        for i, (ticker, data) in enumerate(brief_data['tickers'].items()):
                            with cols[i % 3]:
                                st.metric(
                                    label=f"{ticker}", 
                                    value=f"${data['price']}", 
                                    delta=f"{data['change']}%"
                                )
            else:
                st.error(f"Error: {response.status_code} - {response.text}")
        except Exception as e:
            st.error(f"Error connecting to the API: {str(e)}")
            st.info("Make sure your API server is running and accessible.")

# Additional information
st.markdown("---")
st.markdown("""
### About this app
This Morning Market Brief app provides you with the latest market insights to start your day.
The brief is generated based on the latest market data and news.
""")