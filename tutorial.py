import streamlit as st
st.set_page_config(page_title='MyStreamlit',page_icon='random')
mymenu=st.sidebar.selectbox('My Menu',('Home','Fill Form','Downloads'))
st.image('https://onleitechnologies.com/wp-content/uploads/2021/12/cropped-Untitled_design__6_-removebg-preview-1.png')
st.title('Onlei Technologies')
st.header('By Divyansh Verma')
st.text('This is a tutorial on streamlit library')
if(mymenu=='Home'):
    st.markdown('<center><h1>WELCOME</h1></center>',unsafe_allow_html=True)
    st.video('https://www.youtube.com/watch?v=WdNp2gqyqyo&pp=ygUNYWF5ZWluIGJhaWdhbg%3D%3D')
elif(mymenu=='Fill Form'):
    with st.form('My Form'):
        Name=st.text_input('Enter Name')
        DOB=st.date_input('Choose DOB')
        Marks=st.slider('Choose Marks')
        k=st.form_submit_button("Submit Form")
        if k:
            st.write('Name:',Name,'DOB:',DOB,'Marks:',Marks)

elif(mymenu=='Downloads'):
    st.header("Downloads")
    st.download_button('Download Now','Hello this is the downloaded data','Onlei.txt')

