
def BMR(Weight):
    """Takes away and returns BMR"""
    BMR = Weight * 20
    return BMR


def TEF(BMR):
    """takes away and returns TEF"""
    TEF = BMR * .1
    return TEF


def Exercise_Energy_Expenditure(Beginner_Workout, _Advanced_Workout):
    """Based off Exercise Level, gives energy expenditure"""
    if Beginner_Workout == "sedentary":
        Exercise_Energy_Expenditure = 250
    elif _Advanced_Workout == "active":
        Exercise_Energy_Expenditure = 500
    return Exercise_Energy_Expenditure


def Non_Exercise_Activity_Thermogenesis(Activity_Level):
    """Based off lifestyle, gives non-exercise activity thermogenosis"""
    if Activity_Level == "Sedentary":
        Non_Exercise_Activity_Thermogenesis = 250
    elif Activity_Level == "Active":
        Non_Exercise_Activity_Thermogenesis = 500
    return Non_Exercise_Activity_Thermogenesis


def Total_Daily_Energy_Expenditure(BMR, _TEF, _Exercise_Energy_Expenditure, _Non_Exercise_Activity_Thermogenesis):
    """sum of BMR, TEF, Exercise Energy Expenditure, and Non-Exercise Activity Thermogenesis"""
    return BMR + TEF + Exercise_Energy_Expenditure + Non_Exercise_Activity_Thermogenesis
