import streamlit as st
from pint import UnitRegistry

#note: using pint library

ureg = UnitRegistry()

# Note: I Used the OOP approach

# class for Pint-supported conversions
class UnitConverter:
    def convert(self, value, from_unit, to_unit):
        try:
            result = (value * ureg(from_unit)).to(to_unit)
            return result.magnitude
        except Exception as e:
            return f"Conversion Error: {e}"


class TemperatureConverter:
    formulas = {
        ("Celsius", "Fahrenheit"): lambda c: (c * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda c: c + 273.15,
        ("Fahrenheit", "Celsius"): lambda f: (f - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda f: (f - 32) * 5/9 + 273.15,
        ("Kelvin", "Celsius"): lambda k: k - 273.15,
        ("Kelvin", "Fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32
    }

    def convert(self, value, from_unit, to_unit):
        if from_unit == to_unit:
            return value
        try:
            return self.formulas[(from_unit, to_unit)](value)
        except KeyError:
            return "Invalid conversion"

    def get_units(self):
        return ["Celsius", "Fahrenheit", "Kelvin"]

# General Unit Converters Using Pint
class LengthConverter(UnitConverter):
    def get_units(self):
        return ["meters", "kilometers", "miles", "feet", "inches", "centimeters", "millimeters", "yards"]

class MassConverter(UnitConverter):
    def get_units(self):
        return ["grams", "kilograms", "pounds", "ounces", "milligrams", "tons"]

class SpeedConverter(UnitConverter):
    def get_units(self):
        return ["m/s", "km/h", "mph", "knots"]

class TimeConverter(UnitConverter):
    def get_units(self):
        return ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]

class AreaConverter(UnitConverter):
    def get_units(self):
        return ["square meters", "square kilometers", "square miles", "square feet", "square inches", "hectares", "acres"]

class VolumeConverter(UnitConverter):
    def get_units(self):
        return ["liters", "milliliters", "cubic meters", "cubic inches", "gallons", "pints"]

class DataTransferConverter(UnitConverter):
    def get_units(self):
        return ["bps", "Kbps", "Mbps", "Gbps", "Tbps"]

class DigitalStorageConverter(UnitConverter):
    def get_units(self):
        return ["bytes", "kilobytes", "megabytes", "gigabytes", "terabytes"]

class EnergyConverter(UnitConverter):
    def get_units(self):
        return ["joules", "kilojoules", "calories", "kilocalories", "watt-hours", "kilowatt-hours"]

class FrequencyConverter(UnitConverter):
    def get_units(self):
        return ["hertz", "kilohertz", "megahertz", "gigahertz"]

class FuelEconomyConverter(UnitConverter):
    def get_units(self):
        return ["mpg", "km/l", "l/100km"]

class PlaneAngleConverter(UnitConverter):
    def get_units(self):
        return ["degrees", "radians", "gradians"]

class PressureConverter(UnitConverter):
    def get_units(self):
        return ["pascals", "kilopascals", "bar", "psi", "mmHg", "atm"]

# All converters 
converters = {
    "Length": LengthConverter(),
    "Mass": MassConverter(),
    "Speed": SpeedConverter(),
    "Time": TimeConverter(),
    "Area": AreaConverter(),
    "Volume": VolumeConverter(),
    "Data Transfer Rate": DataTransferConverter(),
    "Digital Storage": DigitalStorageConverter(),
    "Energy": EnergyConverter(),
    "Frequency": FrequencyConverter(),
    "Fuel Economy": FuelEconomyConverter(),
    "Plane Angle": PlaneAngleConverter(),
    "Pressure": PressureConverter(),
    "Temperature": TemperatureConverter()  
}

# Function => handle conversions
def convert_units(category, value, from_unit, to_unit):
    converter = converters.get(category)
    if converter:
        return converter.convert(value, from_unit, to_unit)
    else:
        return "Invalid Category"

# Main... 
st.title("🔢 Unit Converter")
category = st.selectbox("Select a Category", list(converters.keys()))
converter = converters[category]
units = converter.get_units()
from_unit = st.selectbox("From Unit", units)
to_unit = st.selectbox("To Unit", units)
value = st.number_input("Enter Value", min_value=0.0, step=0.1)

if st.button("Convert"):
    result = convert_units(category, value, from_unit, to_unit)
    st.markdown(
    f"""
    <div style="background-color:#1e1e1e; padding: 15px; border-radius: 10px; 
                font-size:20px; font-weight:bold; color:white; text-align:center;">
        {value:.6g} {from_unit} &nbsp; = &nbsp; {result:.6g} {to_unit}
    </div>
    """,
    unsafe_allow_html=True
)