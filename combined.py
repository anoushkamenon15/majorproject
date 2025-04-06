import streamlit as st
import pickle
import warnings

warnings.filterwarnings("ignore")  # Suppress general warnings
# Set page configuration
st.set_page_config(
    page_title="PCOS We Care",
    page_icon="🩺",
    layout="wide"
)

# --- Custom CSS for Navbar ---
st.markdown("""
    <style>
        .navbar-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            background-color: #DC3C68;
            padding: 15px 50px;
            border-radius: 10px;
        }
        .navbar-title {
            font-size: 26px;
            font-weight: bold;
            color: white;
            font-family: Arial, sans-serif;
        }
        .navbar-links {
            display: flex;
            gap: 20px;
        }
        .navbar-links a {
            font-size: 18px;
            font-weight: bold;
            color: white;
            text-decoration: none;
            padding: 10px 15px;
            border-radius: 5px;
            transition: background 0.3s ease;
        }
        .navbar-links a:hover {
            background-color: #F3AFAF;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# --- Navbar Layout ---
st.markdown("""
    <div class="navbar-container">
        <div class="navbar-title">PCOS WE CARE</div>
        <div class="navbar-links">
            <a href="?nav=home">Home</a>
            <a href="?nav=about">About</a>
            <a href="?nav=risk">Risk Assessment</a>
            <a href="?nav=ack">Acknowledgment</a>
        </div>
    </div>
""", unsafe_allow_html=True)


def navigate_to(page):
    st.query_params.update(nav=page)


# --- URL-based Navigation ---
# query_params = st.experimental_get_query_params()
# selected_page = query_params.get("nav", ["home"])[0]
query_params = st.query_params
selected_page = query_params.get("nav", "home")  # Default to "home"

# Set query parameters (if needed)
st.query_params.update(nav=selected_page)

# --- Home Page ---
# if selected_page == "home":
#     st.markdown("<h1 style='color:#DC3C68;text-align:center;'>PCOS WE CARE</h1>", unsafe_allow_html=True)
#     # st.markdown('<div class="center-image">', unsafe_allow_html=True)
#     # st.image("C:/Users/Hritika/test/pcos1.jpg", caption="Comparison of Healthy and Polycystic Ovary")
#     # st.markdown('</div>', unsafe_allow_html=True)
#     with st.columns(3)[1]:
#         st.image("C:/Users/Hritika/test/pcos1.jpg")
#     st.markdown("""
#         <div style='text-align: center;'>
#             <p style='font-size: 20px; font-family: Georgia;'>
#                 If you have struggled with irregular periods, mood swings, irritability, etc.,
#                 these symptoms might look normal but could be signs of PCOS.
#             </p>
#         </div>
#     """, unsafe_allow_html=True)
#
#
#     # Add custom CSS for styling the button
#     st.markdown("""
#         <style>
#             .beautiful-button {
#                 display: inline-block;
#                 background-color: #ff66b2; /* Pink background */
#                 color: white;
#                 font-size: 18px;
#                 padding: 15px 40px;
#                 text-align: center;
#                 text-decoration: none; /* Remove the underline */
#                 border-radius: 50px;
#                 transition: background-color 0.3s ease, transform 0.2s ease;
#             }
#
#             .beautiful-button:hover {
#                 background-color: #ff3385; /* Darker pink on hover */
#                 transform: scale(1.1); /* Slightly increase size on hover */
#             }
#
#             .beautiful-button:active {
#                 background-color: #ff1a73; /* Even darker pink on click */
#             }
#
#             /* Center the button within the page */
#             .center-button {
#                 display: flex;
#                 justify-content: center;
#                 align-items: center;
#                 height: 100vh; /* Full viewport height */
#             }
#         </style>
#         """, unsafe_allow_html=True)
#
#     # Center the button on the page
#     st.markdown('<div class="center-button"><a href="?nav=risk" class="beautiful-button">Begin Your Test</a></div>',
#                 unsafe_allow_html=True)
if selected_page == "home":
    st.markdown("<h1 style='color:#DC3C68;text-align:center;'>PCOS WE CARE</h1>", unsafe_allow_html=True)

    with st.columns(3)[1]:
        st.image("pcos1.jpg")

    st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size: 20px; font-family: Georgia;'>
                If you have struggled with irregular periods, mood swings, irritability, etc., 
                these symptoms might look normal but could be signs of PCOS.
            </p>
        </div>
    """, unsafe_allow_html=True)

    # Add custom CSS for styling the button
    st.markdown("""
        <style>
            .beautiful-button {
                display: inline-block;
                background-color: #ff66b2; /* Pink background */
                color: white;
                font-size: 18px;
                padding: 15px 40px;
                text-align: center;
                text-decoration: none; /* Remove the underline */
                border-radius: 50px;
                transition: background-color 0.3s ease, transform 0.2s ease;
                margin-top: 20px; /* Adjust space between the text/image and button */
            }

            .beautiful-button:hover {
                background-color: #ff3385; /* Darker pink on hover */
                transform: scale(1.1); /* Slightly increase size on hover */
            }

            .beautiful-button:active {
                background-color: #ff1a73; /* Even darker pink on click */
            }

            /* Center the button within the page */
            .center-button {
                display: flex;
                justify-content: center;
                align-items: center;
            }
        </style>
        """, unsafe_allow_html=True)

    # Center the button on the page
    st.markdown('<div class="center-button"><a href="?nav=risk" class="beautiful-button">Begin Your Test</a></div>',
                unsafe_allow_html=True)
# --- About Us Page ---
elif selected_page == "about":

    st.markdown("<h1 style='color:#F3AFAF;text-align:center;'>About</h1>", unsafe_allow_html=True)
    with st.columns(3)[1]:
        st.image("pcos2.jpg", caption="Lifecycle of Ovum in Healthy and Polycystic Ovary")
    st.markdown("""
            <div style='text-align: left;'>
                <p style='font-size: 20px; font-family: Georgia;'>
                    PCOS is a hormonal disorder that affects reproductive-aged women. It can cause irregular periods, 
                    excessive androgen levels, and ovarian cysts. Early diagnosis and lifestyle changes can help manage 
                    symptoms and reduce long-term health risks. Polycystic Ovary Syndrome (PCOS) is a problem with hormones 
                    that happens during the reproductive years . If you have PCOS, you may not have periods very often. 
                    Or you may have periods that last many days. You may also have too much of a hormone called androgen in your body.
                    With PCOS, many small sacs of fluid develop along the outer edge of the ovary. These are called cysts. 
                    The small fluid-filled cysts contain immature eggs. These are called follicles. The follicles fail to regularly release eggs.
                    <br><strong>Causes and Risks:</strong><br>
                    The exact cause of PCOS is unknown. Early diagnosis and treatment along with weight loss may lower the risk of 
                    long-term complications such as type 2 diabetes and heart disease. Polycystic Ovary Syndrome (PCOS) is one 
                    of the most common reproductive disorders in women and despite this, diagnostic challenges, delayed 
                    diagnosis and less than optimal treatment regimens plague the condition. PCOS is a hormonal disorder 
                    affecting 6% - 13% of women in the reproductive age group worldwide. Early detection will facilitate 
                    timely intervention, helping to manage symptoms and reduce the risk of long-term complications associated with PCOS 
                    <br><strong>Complications of PCOS:</strong><br>
                    Type 2 diabetes: More than half of people with PCOS develop type 2 diabetes by age 40. <br>
                    Heart disease: PCOS can increase the risk of heart disease. <br>
                    Endometrial cancer: PCOS can increase the risk of endometrial cancer, which is cancer of the inner lining of the uterus. <br>
                    High blood pressure: PCOS can increase the risk of high blood pressure. <br>
                    High cholesterol: PCOS can increase the risk of high cholesterol. <br>
                    Gestational diabetes: PCOS can increase the risk of gestational diabetes. <br>
                    Sleep apnea: PCOS can increase the risk of sleep apnea. <br>
                    Stroke: PCOS can increase the risk of stroke. <br>
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- Acknowledgment Page ---
if selected_page == "ack":
    st.markdown("<h1 style='color:#DC3C68;text-align:center;'>Acknowledgment</h1>", unsafe_allow_html=True)

    st.markdown("""
        <div style='text-align: center;'>
            <p style='font-size: 20px; font-family: Georgia;'>
                We would like to express our sincere gratitude to all the medical professionals, researchers, 
                and contributors who have dedicated their efforts to the study and awareness of PCOS.
                Special thanks to healthcare providers and support groups for their continuous guidance in helping 
                individuals manage PCOS effectively. <br><br>
                We extend our sincere gratitude to Dr. Pauras Mhatre,MBBS, KEM Hospital, Mumbai (Reg No. 4079/2024) for his
                invaluable guidance and support in our research. His expertise in feature selection for the early diagnosis of polycystic ovary
                syndrome (PCOS) has been instrumental in shaping our study. Additionally, his insights on enhancing the societal impact of
                this research have been greatly beneficial. We deeply appreciate his time, knowledge, and encouragement throughout this
                project.
                We also appreciate the users of PCOS We Care for trusting us and using this platform to learn more 
                about their health.
            </p>
        </div>
    """, unsafe_allow_html=True)

# --- Risk Assessment Page ---
elif selected_page == "risk":
    st.markdown("<h1 style='color:#F3AFAF;text-align:center;'>Risk Assessment</h1>", unsafe_allow_html=True)

    # Load ML Model
    pickle_in = open("Classifierupdates.pkl", 'rb')
    classifier = pickle.load(pickle_in)


    def predict_risk(weight, height, cycleri, cyclelength, weightgain, hairgrowth, skindark, hairloss, pimples,exercise,fastfood):
        prediction = classifier.predict([[ weight, height,
                                          1 if cycleri == "Yes" else 0,
                                          1 if weightgain == "Yes" else 0,
                                          cyclelength,
                                          1 if hairgrowth == "Yes" else 0,
                                          1 if skindark == "Yes" else 0,
                                          1 if hairloss == "Yes" else 0,
                                          1 if pimples == "Yes" else 0,
                                          1 if exercise == "Yes" else 0,
                                          1 if fastfood == "Yes" else 0
                                        ]])
        return "You are at risk of having PCOS" if prediction == [1] else "You are not at risk of having PCOS"


    # Form Inputs
    weight = st.number_input("Enter weight in kg", min_value=0.00, value=0.00, step=0.01)
    height = st.number_input("Enter height in cm", min_value=0.00, value=0.00, step=0.01)
    cycleri = st.selectbox("Do you have regular periods?", ["Yes", "No"])
    cyclelength = st.number_input("Enter average days you have periods", min_value=0, value=0)
    weightgain = st.selectbox("Have you gained a lot of weight suddenly?", ["Yes", "No"])
    hairgrowth = st.selectbox("Do you have increased hair growth?", ["Yes", "No"])
    skindark = st.selectbox("Has your skin darkened(hyper-pigmentation)?", ["Yes", "No"])
    hairloss = st.selectbox("Do you have excessive hair loss?", ["Yes", "No"])
    pimples = st.selectbox("Do you have pimples/acne?", ["Yes", "No"])
    exercise = st.selectbox("Do you exercise fairly regularly?", ["Yes", "No"])
    fastfood = st.selectbox("Do you eat fast food regularly?", ["Yes", "No"])

    if st.button("Predict"):
        result = predict_risk(weight, height, cycleri, cyclelength, weightgain, hairgrowth, skindark, hairloss, pimples,exercise,fastfood)
        st.success(result)
