import streamlit as st # type: ignore

# Unit conversion functions
def convert_length(value, from_unit, to_unit):
    length_conversions = {
        'meters': 1,
        'kilometers': 1000,
        'centimeters': 0.01,
        'millimeters': 0.001,
        'miles': 1609.34,
        'yards': 0.9144,
        'feet': 0.3048,
        'inches': 0.0254
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    weight_conversions = {
        'kilograms': 1,
        'grams': 0.001,
        'milligrams': 0.000001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value

# Streamlit UI
def main():
    # Set page title and icon
    st.set_page_config(page_title="Unit Converter🔄", page_icon="📏")

    # Header
    st.title("📏 Google-like Unit Converter")
    st.write("Convert between different units easily!")

    # Add a divider for better UI
    st.markdown("---")

    # Select the type of conversion
    conversion_type = st.selectbox(
        "**Select Conversion Type**",
        ["Length", "Weight", "Temperature"],
        help="Choose the type of unit you want to convert."
    )

    # Define units based on conversion type
    if conversion_type == "Length":
        units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
    elif conversion_type == "Weight":
        units = ['kilograms', 'grams', 'milligrams', 'pounds', 'ounces']
    elif conversion_type == "Temperature":
        units = ['celsius', 'fahrenheit', 'kelvin']

    # Input value
    value = st.number_input(
        "**Enter the value to convert**",
        value=1.0,
        min_value=0.0,
        help="Enter the numerical value you want to convert."
    )

    # Use columns for better layout
    col1, col2 = st.columns(2)

    # Select the 'from' unit
    with col1:
        from_unit = st.selectbox(
            "**From**",
            units,
            help="Select the unit you are converting from."
        )

    # Select the 'to' unit
    with col2:
        to_unit = st.selectbox(
            "**To**",
            units,
            help="Select the unit you are converting to."
        )

    # Add a button to perform the conversion
    if st.button("**Convert**", help="Click to perform the conversion."):
        # Perform the conversion
        if conversion_type == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif conversion_type == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif conversion_type == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)

        # Display the result in a success box
        st.success(f"**Converted value:** {result:.2f} {to_unit}")

    # Add a footer
    st.markdown("---")
    st.write("Made with ❤️ using Streamlit")

# Run the app
if __name__ == "__main__":
    main()
