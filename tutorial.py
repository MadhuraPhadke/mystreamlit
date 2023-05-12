import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fill Form','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/Untitled_design__6_-removebg-preview-1-300x169.png')
st.title('Onlei Technologies')
st.header('By Abhinav Srivastava')
st.text('This is a tutorial on Streamlit library')
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/PinClipart.com_adult-learning-clipart_5373093.png')
if(mymenu=='Home'):
    st.markdown('<center><h1>Welcome</h1></center>',unsafe_allow_html=True)
    st.video('https://youtu.be/EjY2gUFVwZE')
elif(mymenu=='Fill Form'):
    with st.form('My Form'):
        name=st.text_input('Enter your name')
        dob=st.date_input('Select your date of birth')
        marks=st.slider('Choose your marks')
        submit=st.form_submit_button('Submit form')

        if submit:
            st.write('Name:',name,'DOB:',dob,'Marks:',marks)
            
elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','Hello! This is a downloaded data','onlei.txt')
    
