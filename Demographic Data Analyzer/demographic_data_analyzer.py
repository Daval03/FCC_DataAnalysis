import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("Demographic Data Analyzer/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    all_races = df["race"].unique() #index
    race = df["race"]
    race_count = pd.Series([]).reindex(all_races)
    for i in range(0, len(all_races)):
        race_count[all_races[i]] = len(race[race == all_races[i]])

    # What is the average age of men?
    men = df[df["sex"] == "Male"]
    average_age_men = men["age"].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((len(df[df["education"] == "Bachelors"]) * 100)/len(df),1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    with_edu = df[( (df["education"]=="Bachelors") | (df["education"]=="Masters") | (df["education"]=="Doctorate") )]
    without_edu = df[ (df["education"]!="Bachelors") & (df["education"]!="Masters") & (df["education"]!="Doctorate")]
    with_edu_50k = len(with_edu[ with_edu["salary"] != ">50K"])
    without_edu_50k = len(without_edu[ without_edu["salary"] != ">50K"])

    # percentage with salary <=50K
    higher_education = with_edu_50k*100/len(with_edu)
    lower_education = without_edu_50k*100/len(without_edu)

    # percentage with salary >50K
    higher_education_rich = round(100-higher_education, 1)
    lower_education_rich =  round(100-lower_education, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df["hours-per-week"].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min = len(df[ (df["hours-per-week"] == min_work_hours)])
    min_50k = len(df[ (df["salary"] == ">50K") & (df["hours-per-week"] == min_work_hours) ])

    rich_percentage = (min_50k * 100)/min

    # What country has the highest percentage of people that earn >50K?
    countrys = df["native-country"].unique()
    countrys_count = pd.Series([]).reindex(countrys)
    for i in range(0, len(countrys)):
        population_50k = len( df[(df["native-country"] == countrys[i]) & (df["salary"] ==">50K")]  )
        population = len( df[(df["native-country"] == countrys[i])] )
        countrys_count[countrys[i]] = population_50k*100/population

    highest_earning_country = countrys_count.idxmax()
    highest_earning_country_percentage = round(countrys_count.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india50k = df[ (df["native-country"]== "India") & (df["salary"] ==">50K")]
    india50k_list = india50k["occupation"].unique() 
    india50k_count = pd.Series([]).reindex(india50k_list)

    for i in range(0, len(india50k_list)):
        india50k_count[india50k_list[i]] = len (india50k[ india50k[ "occupation" ] == india50k_list[i]])
    top_IN_occupation = india50k_count.idxmax()
    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
