from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Load trained model
pipe = pickle.load(open('pipe.pkl', 'rb'))

teams = [
    'Sunrisers Hyderabad',    
    'Mumbai Indians', 
    'Royal Challengers Bangalore',  
    'Kolkata Knight Riders',
    'Kings XI Punjab', 
    'Chennai Super Kings',  
    'Rajasthan Royals',
    'Delhi Capitals'
]

cities = [
    'Mumbai','Kolkata','Delhi','Chennai','Hyderabad',
    'Jaipur','Bangalore','Chandigarh','Ahmedabad'
]

@app.route('/')
def home():
    return render_template('index.html', teams=teams, cities=cities)


@app.route('/predict', methods=['POST'])
def predict():

    batting_team = request.form['batting_team']
    bowling_team = request.form['bowling_team']
    city = request.form['city']
    runs_left = int(request.form['runs_left'])
    balls_left = int(request.form['balls_left'])
    wickets = int(request.form['wickets'])
    total_runs = int(request.form['total_runs'])
    crr = float(request.form['crr'])
    rrr = float(request.form['rrr'])

    input_df = pd.DataFrame({
        'batting_team':[batting_team],
        'bowling_team':[bowling_team],
        'city':[city],
        'runs_left':[runs_left],
        'balls_left':[balls_left],
        'wickets':[wickets],
        'total_runs_x':[total_runs],
        'crr':[crr],
        'rrr':[rrr]
    })

    result = pipe.predict_proba(input_df)
    win_prob = round(result[0][1]*100)
    loss_prob = round(result[0][0]*100)

    return render_template(
        'index.html',
        teams=teams,
        cities=cities,
        win=win_prob,
        loss=loss_prob,
        batting_team=batting_team
    )


if __name__ == '__main__':
    app.run(debug=True)