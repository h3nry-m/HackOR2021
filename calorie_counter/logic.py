

def BMR(weight):
    """Takes away and returns BMR"""
    BMR = weight * 20
    return BMR


def TEF(BMR):
    """takes away and returns TEF"""
    TEF = BMR * .1
    return TEF


def Exercise_Energy_Expenditure(workout):
    """Based off Exercise Level, gives energy expenditure"""
    if workout == "low":
        Exercise_Energy_Expenditure = 250
    elif workout == "high":
        Exercise_Energy_Expenditure = 500
    return Exercise_Energy_Expenditure


def Non_Exercise_Activity_Thermogenesis(Activity_Level):
    """Based off lifestyle, gives non-exercise activity thermogenosis"""
    if Activity_Level == "sedentary":
        Non_Exercise_Activity_Thermogenesis = 250
    elif Activity_Level == "active":
        Non_Exercise_Activity_Thermogenesis = 500
    return Non_Exercise_Activity_Thermogenesis


def Total_Daily_Energy_Expenditure(BMR, TEF, Exercise_Energy_Expenditure, Non_Exercise_Activity_Thermogenesis):
    """sum of BMR, TEF, Exercise Energy Expenditure, and Non-Exercise Activity Thermogenesis"""
    total_daily_energy_expenditure = BMR + TEF + \
        Exercise_Energy_Expenditure + Non_Exercise_Activity_Thermogenesis
    return total_daily_energy_expenditure


def recommended_calories(total_daily_energy_expenditure, goal, weight):
    # placeholder variable
    need_to_lose = weight - goal
    # rate values
    half_per_week_rate = total_daily_energy_expenditure - 250
    one_per_week_rate = total_daily_energy_expenditure - 500
    one_half_per_week_rate = total_daily_energy_expenditure - 750
    two_per_week_rate = total_daily_energy_expenditure - 1000
    # array to hold the rate values
    rate = [half_per_week_rate, one_per_week_rate,
            one_half_per_week_rate, two_per_week_rate]
    # calulating the time to reach your goal
    time_to_lose_half = need_to_lose/rate[0]
    time_to_lose_one = need_to_lose/rate[1]
    time_to_lose_one_half = need_to_lose/rate[2]
    time_to_lose_two = need_to_lose/rate[3]
    # return all the "time to lose" variables to spit back out
    return rate, time_to_lose_half, time_to_lose_one, time_to_lose_one_half, time_to_lose_two
