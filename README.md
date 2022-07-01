## README
## MLFinalProject <br />

This project is divided into 2 parts:<br />

## Dataset Description <br />
The selected dataset we used is https://www.kaggle.com/datasets/claudiosantoro/footballteamsdatacsv?select=Bundes2021.csv which containes football match statistics from the top football leagues in the world, such as the Premier League (England), SeriaA (Italy), Bundesliga (Germany) and more.
Eeach row in the dataset's table containes information about a match that occured.
In our project we focused on the SeriaA tables on run our algorithms on them. 

Questions we wanted to answer
* *Given 2 teams, who will win? (can be also tie)*
* *Given limited amounts of money, how can I create a new group?*

## The techniques we used: KNN, Adaboost, Decision Trees and Logistic Regression.

Obstacles we faced and how we dealt with them?
- Obstacle: How should we model the text-formatted data into to a vector of numbers, which on it we will be able to conduct array maniulation in order to run the selected algorithms. 
- Solution: From each text-formatted vec,
 
- Obstacle: On how much prior data should we relay as the base set of our analysis
- Soulution: We've decided to relay on the past 2 year of data in the SeriaA. This decission was made in order to provide both sufficient amount of data for the algorithms and also keeping the data about the teams as relevant and updated as possible.

- Obstacle: How should we address the multiclass classification (1 - Home Team Win, 2- Draw, 3 - Away Team Win) with binary classification alogrithms and methods? 
- Solution: For each multiclass question, we've created a 2 layer binary classificaiton, in the following way:
If for a giving match between a Home team and an Away team, we would like to know which teams is going to win - we've asked the following question:
  1. Is the Home team predicted to win? ---> {Yes, No}
  2. Is the Away team predicted to win? ---> {Yes, No}
Then based on the answers of both question, we can conclude the complete answer:
If Home team is predicted to win and Away team is predicted to not win - answer is Home team win.
If Home team is predicted to not win and Away team is predicted to win - answer is Away team win.
If Home team is predicted to not win and Away team is predicted to not win - answer is Draw.
- Giving the fact the the same algorithm with the same data answes both question, there is not possible way for a scenario in which both teams are predicted to win. 



* The conversion of each row which presents a game into a vector in order to be able to apply the ML techniques.
* When trying to implement and run Adaboost on our data because in class we learned that for Adaboost, each class has its opposite class, but in our case we have 3   classes: home team wins, away team wins, or a tie, so it means that none of our the classes has its opposite class.

