'''test'''
from datetime import date, timedelta
#from time import sleep
from flask import Flask, render_template, request

app = Flask(__name__)

all_goals = []
today_date = date.today()
todays_goals = []
completed_count = 0

def stage1():
    '''flower stage 1'''
    return " _______ \n" + "|_______|\n" + r" \     /" + "\n" + r"  \___/  "


def stage2():
    '''flower stage 2'''
    return r"   \ /   " + "\n" + " ___|___"  + "\n" + "|_______|"  + "\n" + r" \     /"  + "\n" + r"  \___/  "

def stage3():
    '''flower stage 3'''
    return r"   \|/   " + "\n" + " ___|___" + "\n" + "|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

def stage4():
    '''flower stage 4'''
    return r"  (\|/)" + "\n" + r"   \|/   " + "\n" + " ___|___" + "\n" + "|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

def stage5():
    '''flower stage 5'''
    return "    |" + "\n" + r"  (\|/)" + "\n" + r"   \|/   " + "\n" + " ___|___" + "\n" + "|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

def stage6():
    '''flower stage 6'''
    return "    |" + "\n" + "    |" + "\n" + r"  (\|/)" + "\n" + r"   \|/   " + "\n" + r" ___|___" + "\n" + r"|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

def stage7():
    '''flower stage 7'''
    return "    @" + "\n" + r"   (_)" + "\n" + r"    |" + "\n" + r"    |" + "\n" + r"  (\|/)" + "\n" + r"   \|/   " + "\n" + r" ___|___" + "\n" + r"|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "


def stage8():
    '''flower stage 8'''
    return r" (_)@(_)" + "\n" + r"   (_)" + "\n" + r"    |" + "\n" + r"    |" + "\n" + r"  (\|/)" + "\n" + r"   \|/   " + "\n" + r" ___|___" + "\n" + r"|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

def stage9():
    '''flower stage 9'''
    return r"  _(_)_" + "\n" + r" (_)@(_)" + "\n" + r"   (_)" + "\n" + r"    |" + "\n" + r"    |" + "\n" + r"  (\|/)" + "\n" + r"   \|/   " + "\n" + r" ___|___" + "\n" + r"|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

def stage10():
    '''flower stage 10'''
    return r"    _" + "\n" + r"  _(_)_" + "\n" + r" (_)@(_)" + "\n" + r"   (_)" + "\n" + r"    |" + "\n" + r"    |" + "\n" + r"  (\|/)" + "\n" + r"   \|/   " + "\n" + r" ___|___" + "\n" + r"|_______|" + "\n" + r" \     /" + "\n" + r"  \___/  "

current_plant = stage1()

def filter_goals():
    '''filter for todays goals'''
    for goal in all_goals:
        if goal[1] == str(today_date):
            todays_goals.append(goal)

def complete_goal():
    '''complete goal'''
    goal_list = ""
    i = 1
    for goal in todays_goals:
        goal_list += "\n{}) {}".format(i, goal[0])
        i += 1
    return goal_list


@app.route("/")
def home():
    '''setup goals'''
    return render_template("starting.html")

@app.route("/goalsetup",methods=["GET","POST"])
def goal_setup():
    "add new goals to all goals"
    new_goal_name = request.form["new_goalName"]
    new_goal_due = request.form["new_goalDue"]
    new_goal = [new_goal_name, new_goal_due]
    all_goals.append(new_goal)
    todays_goals = []
    filter_goals()

    return render_template("home.html", plantline1 = current_plant)

@app.route("/actions",methods=["GET","POST"])
def new_action():
    '''Get user action choice'''
    global today_date
    action_choice = request.form["action_pick"]
    if action_choice == "dayIncrease":
        today_date += timedelta(days=1)
        filter_goals()
        return render_template("home.html", plantline1 = current_plant)
    #
    elif action_choice == "addGoal":
        return render_template("starting.html")
    #
    elif action_choice == "completeGoal":
        goal_list = complete_goal()
        return render_template("result.html", goalOptions = goal_list)

@app.route("/goal_completion",methods=["GET","POST"])
def goal_completion():
    '''remove goal from list'''
    global completed_count
    completed_goal = request.form["completedGoal"]
    if completed_goal == "":
        return render_template("home.html", plantline1 = current_plant)
    else:
        completed_goal = int(completed_goal)
    todays_goals.pop(completed_goal - 1)
    completed_count += 1
    if not todays_goals or completed_count == 5:
        if current_plant == stage1():
            new_plant = stage2()
        elif current_plant == stage2():
            new_plant = stage3()
        elif current_plant == stage3():
            new_plant = stage4()
        elif current_plant == stage4():
            new_plant = stage5()
        elif current_plant == stage5():
            new_plant = stage6()
        elif current_plant == stage6():
            new_plant = stage7()
        elif current_plant == stage7():
            new_plant = stage8()
        elif current_plant == stage8():
            new_plant = stage9()
        elif current_plant == stage9():
            new_plant = stage10()
        #
        return render_template("plant_change.html", flower2 = current_plant, flower1 = new_plant)
    else:
        return render_template("home.html", plantline1 = current_plant)

@app.route("/return_to_actions",methods=["GET","POST"])
def return_to_actions():
    '''return to home.html'''
    global current_plant
    if current_plant == stage1():
        current_plant = stage2()
    elif current_plant == stage2():
        current_plant = stage3()
    elif current_plant == stage3():
        current_plant = stage4()
    elif current_plant == stage4():
        current_plant = stage5()
    elif current_plant == stage5():
        current_plant = stage6()
    elif current_plant == stage6():
        current_plant = stage7()
    elif current_plant == stage7():
        current_plant = stage8()
    elif current_plant == stage8():
        current_plant = stage9()
    elif current_plant == stage9():
        current_plant = stage10()
    return render_template("home.html", plantline1 = current_plant)

if __name__ == "__main__":
    app.run(debug=True)
