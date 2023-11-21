import pandas as pd
from map_explorer import create_data_frame


def test_create_data_frame():
    """Test that create_data_frame correctly creates a DataFrame."""
    latitude, longitude = 40.7128, -74.0060
    expected_output = pd.DataFrame({"lat": [latitude], "lon": [longitude]})

    result = create_data_frame(latitude, longitude)

    pd.testing.assert_frame_equal(result, expected_output)
