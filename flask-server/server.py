from flask import Flask, jsonify, request
from metaphor_python import Metaphor

user_input = 'software engineer video'

metaphor = Metaphor("cb6581fd-b59a-4884-b9f2-9b9b152e5779")

results = metaphor.search(
  user_input,
  num_results=1,
)

title_response = results.results[0].title
url_response = results.results[0].url

app = Flask(__name__)

@app.route('/search', methods=['GET','POST'])
def receive_user_input():
    if request.method == 'POST':
        global user_input
        user_input = request.json.get('userInput')
        global results
        results = metaphor.search(
        user_input,
        num_results=1,
        )
        global title_response
        global url_response
        title_response = results.results[0].title
        url_response = results.results[0].url
        return jsonify({"message": "Data received and processed successfully!"})
    elif request.method == 'GET':
        data = {"title": title_response, "url": url_response}
        return jsonify(data)


if __name__== "__main__":
    app.run(debug=True)