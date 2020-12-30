import os
with open(os.path.join('C://Users//axelo//OneDrive//Documents//essai_streamlit_heroku','Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run streamlit_app.py'
    
file1.write(toFile)