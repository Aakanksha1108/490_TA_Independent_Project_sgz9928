# Independent Project
## Submitted By: Shreyashi Ganguly

This project aims to analyaze the campaign speeches delivered by US 2020 Presidential candidates Donald Trump and Joe Biden using Topic Modeling and Query Based Extractive Text Summarization.

The models are implemented as a Rest API service. The instructions to use the API are as follows:
- Download and install the latest versions of the following packages:
    - flask
    - swagger
    - flask_cors
    - pickle
    - networkx
    - nltk
    - sklearn
    - numpy
- Download the 50d GloVe embeddings from this link https://drive.google.com/file/d/1cxVuEeRnmPgGJdOqd5kPu1nKGlqkefzi/view?usp=sharing
Save the downloaded file in the artifacts folder
- Run api.py
- Copy paste the server url appending 'apidocs' at the end in a new tab (for example http://127.0.0.1:5000/apidocs)
- The API has the following methods implemented
    - GET to visualize the topic modeling results - Click on "Try it out" -> "Execute" and paste the Request URL on a new tab. Separate GET methods are implemented for Trump and Biden.
    - POST to provide keywords pertaining to a topic of interest and retrieve relevant summary from the respective candidate's speeches - Click on "Try it out" -> Provide the key words in the text field, separated by space -> Click "Execute". The summaries are provided in the response body
