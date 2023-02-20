import streamlit as st
import pandas as pd
import pickle
from PIL import Image

print(pd.__version__)
print(st.__version__)
print(pickle.format_version)

# Load banner image
banner = Image.open('image1.jpg')

# Display banner image
st.image(banner, use_column_width=True)


# # Load custom CSS file
# css = """
# body {
#     background-color: navy;
#     color: white;
# }
# """

# # Apply custom CSS
# st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>NUTRITION'S CALCULATOR</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'><i>MAE: 0.17 | RMSE: 0.20</i></h6>", unsafe_allow_html=True)

# Step 1 - import saved model
model = pickle.load(open("pipeline_and_model.pkl", "rb"))

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.markdown("<h6 style='text-align: center;'>Insert the Nutrition Value</h6>", unsafe_allow_html=True)
st.write(' ')

v1 = st.number_input(label='V1', min_value=0.0, max_value=10000.0, step=0.1)
v2 = st.number_input(label='V2', min_value=0.0, max_value=10000.0, step=0.1)
v3 = st.number_input(label='V3', min_value=0.0, max_value=10000.0, step=0.1)
v4 = st.number_input(label='V4', min_value=0.0, max_value=10000.0, step=0.1)
v5 = st.number_input(label='V5', min_value=0.0, max_value=10000.0, step=0.1)
v6 = st.number_input(label='V6', min_value=0.0, max_value=10000.0, step=0.1)
v7 = st.number_input(label='V7', min_value=0.0, max_value=10000.0, step=0.1)
v8 = st.number_input(label='V8', min_value=0.0, max_value=10000.0, step=0.1)

# convert into dataframe
data = pd.DataFrame({'V1': [v1],
                'V2': [v2],
                'V3': [v3],
                'V4': [v4],
                'V5': [v5],
                'V6': [v6],
                'V7': [v7],
                'V8': [v8],
                })

data_styled = data.style.set_properties(**{'text-align': 'center'})
st.write(data_styled)


if st.button('Predict'):
    # model predict
    clas = model.predict(data).tolist()[0]

    # interpretation
    st.write('Prediction Value: ', clas)

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')
st.markdown("<h6 style='text-align: center;'>Hasbi Thaufik Oktodila</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Contact:</h6>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'><a href='http://linkedin.com/in/hasbithaufik/'>LinkedIn</a> | <a href='http://github.com/hasbithaufik'>GitHub</a> | <a href='mailto:hasbithaufik@gmail.com'>Gmail</a> | +6281374160173</p>",
            unsafe_allow_html=True)

