'''
Description: 
Author: lunyang
Github: 
Date: 2022-02-02 14:29:24
LastEditors: lunyang
LastEditTime: 2022-02-02 17:29:36
'''
import streamlit as st
from multipage import MultiPage
from pages import home, machine_learning

st.set_page_config(page_title="CQUPT", layout="wide")
# st.title('重庆邮电大学智能媒体传输小组')
st.image('images/cqupt.jpeg',width=800)

app = MultiPage()

# add applications
app.add_page('Home', home.app)
app.add_page('Cross Modality Retrieval', machine_learning.app)
# Run application
if __name__ == '__main__':
    app.run()