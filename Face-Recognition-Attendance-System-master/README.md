# Face-Recognition-Attendance-System
    INSTALLATION :
        1. Install latest version of python and add it to PATH.
        2. Install mysql and create new schema by the name of "face_recognizer"
        3. Download the project in zip form and extract it
        4. Selecting "face_recognizer" schema, import the sql file(face_recognizer_student.sql) which is present inside the "database folder" and in target schema                  mention  "face recognizer schema"
        5. Open cmd and install the libraries by following commands
                pip install Pillow
                pip install opencv-python
                pip install mysql-connector-python
                pip install opencv-contrib-python
         
        6. Open the extracted project in vs code
        7. In the extracted project folder, make a new floder with name "data"
        8. Go to "student.py" and go to line 370. Select username and password and with the help of change all occurences in vs code, change the username and password  
           by replacing it with your mysql workbench user and password.
        9. Repeat above process (process no-8) in "face_recognition.py" file on line on 71
        10. Now go to "main.py" file and run the project
                
                
                
        
