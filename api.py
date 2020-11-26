import logging

import flask
from flasgger import Swagger
from flask import Flask, request, jsonify, Response, send_from_directory
from flask_cors import CORS
from query_based_summarization.predict import query_summary

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


# Initialize the Flask application
application = Flask(__name__)

application.config['ALLOWED_EXTENSIONS'] = set(['pdf', 'html'])
application.config['UPLOAD_FOLDER'] = "artifacts"
application.config['CONTENT_TYPES'] = {"html": "text/html", "pdf": "application/pdf"}
application.config["Access-Control-Allow-Origin"] = "*"


CORS(application)

swagger = Swagger(application)

def clienterror(error):
    resp = jsonify(error)
    resp.status_code = 400
    return resp


def notfound(error):
    resp = jsonify(error)
    resp.status_code = 404
    return resp


@application.route('/v1/topic_summary', methods=['POST'])
def sentiment_classification():
    """Summarize speeches relevant to user given key words.
        ---
        parameters:
          - name: body
            in: body
            schema:
              id: text
              required:
                - text
              properties:
                text:
                  type: string
            description: the required text for POST method
            required: true
        definitions:
          TopicBasedSummarization:
          Project:
            properties:
              status:
                type: string
              ml-result:
                type: object
        responses:
          40x:
            description: Client error
          200:
            description: Keyword based summary with top 10 sentences
            examples:
                          [
                    {
                      "status": "success",
                      "summary": {"Donald Trump": ["relevant sentence 1", "relevant sentence 2",...,"relevant sentence 10"],
                                  "Joe Biden": ["relevant sentence 1", "relevant sentence 2",...,"relevant sentence 10"]}
                    },
                    {
                      "status": "error",
                      "message": "Exception caught"
                    },
                    ]
        """
    json_request = request.get_json()
    if not json_request:
        return Response("No json provided.", status=400)
    text = json_request['text']
    if text is None:
        return Response("No text provided.", status=400)
    else:
        summary = query_summary(text)
        return flask.jsonify({"status": "success", "summary": summary})


@application.route('/v1/topic_modeling/trump', methods=['GET'])
def trump_lda():
    """Major topics from Donald Trump's campaign speeches.
        ---
        definitions:
          TopicModeling:
        responses:
          40x:
            description: Client error
          200:
            description: Paste Request URL on a new tab for Topic Modeling Visualization for Donald Trump
            examples:
    """
    return flask.send_from_directory(directory=application.config['UPLOAD_FOLDER'], filename="Trump_lda.html")

@application.route('/v1/topic_modeling/biden', methods=['GET'])
def biden_lda():
    """Major topics from Joe Biden's campaign speeches.
        ---
        definitions:
          TopicModeling:
        responses:
          40x:
            description: Client error
          200:
            description: Paste Request URL on a new tab for Topic Modeling Visualization for Joe Biden
            examples:
    """
    return flask.send_from_directory(directory=application.config['UPLOAD_FOLDER'], filename="Biden_lda.html")

if __name__ == '__main__':
    application.run(debug=True, use_reloader=True)