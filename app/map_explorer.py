import pandas as pd
import streamlit as st


def create_data_frame(latitude, longitude):
    """Create a pandas DataFrame with given latitude and longitude"""
    data = pd.DataFrame({"lat": [latitude], "lon": [longitude]})
    return data


def main():
    """Main function to run the application"""

    st.title("Map Explorer")
    st.subheader("A simple tool to visualise points on a map")

    # Get latitude and longitude from user input
    col1, col2 = st.columns(2)
    lat = col1.number_input(
        label="Enter Latitude:",
        value=52.2,
        min_value=-90.0,
        max_value=90.0,
        step=1.0,
    )
    lon = col2.number_input(
        label="Enter Longitude:",
        value=5.5,
        min_value=-180.0,
        max_value=180.0,
        step=1.0,
    )

    # Create pandas dataframe with user input
    data = create_data_frame(lat, lon)

    # Display map
    st.map(data, zoom=5, use_container_width=True)


if __name__ == "__main__":
    main()
