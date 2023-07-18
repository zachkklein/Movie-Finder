from flask import Flask, request, jsonify, render_template, redirect
import tkinter #IMPORT MODEL CODE NOT TKINTER

app = Flask(__name__)

def inputs(genre, actor, language, length, rating):
    responses = {'genre': genre, 'actor': actor, 'langauge': language, 'length': length, 'rating': rating}
    return responses

emptyList = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['GET', 'POST'])
def getRecommendations():
   #data = request.json  # Get data sent from the frontend
    # Call your Python model function with the data
    genre = request.form.get('genre')
    actor = request.form.get('actor')
    language = request.form.get('language')
    length = request.form.get('length')
    rating = request.form.get('rating')
    emptyList.append(inputs(genre, actor, language, length, rating)) #CHANGE LINE WHEN CODE DONE
    return redirect('/')
    # recommendations = modelName.getRecommendations(data) #modelName is the imported model
    # return jsonify(recommendations) 

@app.route('/print')
def printList():
    print(*emptyList, sep='\n')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


