from flask import Flask, request, render_template, redirect
from control_part2 import mainpart, df_tolist

app = Flask(__name__)

def answers(genre, actor, year):
    responses = {'genre': genre, 'actor': actor, 'year': year}
    return responses

#Empty list that will be updated with inputs
movieList = []

#Routing / to index.html
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommendations', methods=['GET', 'POST'])
def getRecommendations():
   #data = request.json  # Get data sent from the frontend
    # Call your Python model function with the data
    user_ing = request.form.get('genre')
    user_inc = request.form.get('actor')
    user_date = request.form.get('year')
    show_df = mainpart(user_ing, user_inc, user_date)
    final_one=df_tolist(show_df)
    print(final_one)
    return render_template('results.html', user_ing = request.form.get('genre'), user_inc = request.form.get('actor'), user_date = request.form.get('year'), final_one=final_one)
  
    #HTML needs to print put final_one
    #return redirect('/')

#prints the list when /print is added to url-path
@app.route('/print')
def printList():
    print(*movieList, sep='\n')
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


