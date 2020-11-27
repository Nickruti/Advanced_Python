
# Import the required module for text  
# to speech conversion 
from gtts import gTTS 
from docx import Document
from io import StringIO
  
# This module is imported so that we can  
# play the converted audio 
import os 
  
# The text that you want to convert to audio 
#mytext = 'Welcome to geeksforgeeks!'

# Language in which you want to convert 
language = 'en'
  
# Passing the text and language to the engine,  
# here we have marked slow=False. Which tells  
# the module that the converted audio should  
# have a high speed 
with open('210286_Manuscript_2.docx', 'r') as f:
    source_stream = StringIO(f.read())
document = Document(source_stream)
source_stream.close()


myobj = gTTS(text=f.read(), lang=language, slow=False) 
  
# Saving the converted audio in a mp3 file named 
# welcome  
myobj.save("welcome.mp3") 
  
# Playing the converted file 
#os.system("mpg321 welcome.mp3") 