import streamlit as st
# ML packages
from sklearn.externals import joblib
from PIL import Image
# Vectorizer
gender_vectorizer = open("model/gender_vectorizer.pkl","rb")
gender_cv = joblib.load(gender_vectorizer)

# Models
gender_nv_model = open("model/naivebayesgendermodel.pkl", "rb")
gender_clf = joblib.load(gender_nv_model)

@st.cache #to improve speed
def predict_gender(data):
    vect = gender_cv.transform(data).toarray()
    result = gender_clf.predict(vect)
    return result
    

def load_image(filename):
    img = Image.open(filename)
    return st.image(img, width=300)

def load_css(css_file):
    with open(css_file) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

def main():
    st.title("Gender Classifier ML App")

    html_temp ="""

    <div style="background-color:tomato;padding:15px;">
    
    <h2>Strsamlit ML App</h2>

    </div>
    """

    st.markdown(html_temp, unsafe_allow_html=True)

    load_css('icon.css')
    load_icon('people')
    name = st.text_input("Enter Name", "Type Here")

    if st.button("Classify"):
        st.text("Name {}".format(name.title()))
        result = predict_gender([name])
        if result[0] == 0:
            prediction = 'Female'
            c_image = "girl_1.jpg"
        
        else:
            result[0] == 1
            prediction = 'Male'
            c_image = "boy.png"

        st.success("Name '{}', was classified as {}".format(name, prediction))
        load_image(c_image)


if __name__ == '__main__':
    main()