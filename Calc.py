import pandas as pd
import statistics as st
import sys
import numpy as np


class RaterInfo():
    Id = 0
    startTime = "StartTime"
    endTime = "EndTime"
    email = "email"      # KEY
    name = "raterName"
    def __init__(self, Id, startTime, endTime, email, name):
        self.Id = Id
        self.startTime = startTime
        self.endTime = endTime
        self.email = email
        self.name = name

class Strategic_risks():
    def __init__(self, Quality_goal_not_met, Credit, Infrastructure, Resource, Other):
        self.Quality_goal_not_met = Quality_goal_not_met
        self.Credit = Credit
        self.Infrastructure = Infrastructure
        self.Resource = Resource
        self.Other = Other

class Legal_risks():
    def __init__(self, IP, Brand, Lawsuit, Other):
        self.IP= IP
        self.Brand = Brand
        self.Lawsuit = Lawsuit
        self.Other = Other

class Operational_risks():
    def __init__(self,Inefficient_process,Ineffective_process,Ineffective_KPI,Other):
        self.Inefficient_process= Inefficient_process
        self.Ineffective_process = Ineffective_process
        self.Ineffective_KPI = Ineffective_KPI
        self.Other = Other

class Compliance_risks():
    def __init__(self,Country, Health_and_Safety, ESD, Limitations, International_standard, Other):
        self.Country= Country
        self.Health_and_Safety = Health_and_Safety
        self.ESD = ESD
        self.Limitations = Limitations
        self.International_standard= International_standard
        self.Other = Other

class Technical_risks():
    def __init__(self,Testability,Performance,Reliability,Availability,Scalability,Security,Maintainability,Other):
        self.Testability = Testability
        self.Performance = Performance
        self.Reliability = Reliability
        self.Availability = Availability
        self.Scalability = Scalability
        self.Security = Security
        self.Maintainability = Maintainability
        self.Other = Other

ProbDict = ["RARE", "POSSIBLE", "PROBABLE"]
class Likelihood ():
    NumericValueOfProbability = 0
    def __init__(self, Likelihood_p):

        if (Likelihood_p in ProbDict):
            self.Likelihood_val = Likelihood_p
            if Likelihood_p == "RARE" :
                self.NumericValueOfProbability = 1
            elif Likelihood_p == "POSSIBLE" :
                self.NumericValueOfProbability = 2
            else:
                self.NumericValueOfProbability = 3
        else:
            print("error: prob value must be 1 2 or 3")



ImpactDict = [ "LOW", "MEDIUM", "HIGH"]
class Impact():
    NumericValueOfImpact = 0
    def __init__(self, Impact_p):

        if (Impact_p in ImpactDict):
            self.Impact_val = Impact_p
            if Impact_p == "LOW":
                self.NumericValueOfImpact = 1
            elif Impact_p == "MEDIUM":
                self.NumericValueOfImpact = 2
            else:
                self.NumericValueOfImpact = 3
        else:
            print ("error: Impact value must be 1 2 or 3")

ProfileDict = ["Constant", "Logarithmic", "Linear", "Exponential"]
class Cost_profile ():
    NumericValueOfProfile = 0
    def __init__(self, Profile_p):
        if (Profile_p in ProfileDict) :
            self.Profile_val = Profile_p
            if Profile_p == "Constant":
                self.NumericValueOfProfile = 1
            elif Profile_p == "Logarithmic":
                self.NumericValueOfProfile = 2
            elif Profile_p == "Linear":
                self.NumericValueOfProfile = 3
            else:
                self.NumericValueOfProfile = 4

        else:
            print ("error: profile cost value must be 1 2 3 or 4")


# Program start here - MAIN -----------------------------

# Run K Inter-rater Agreement
def analize2(file_handler2, app2):
    import Grafica as graf
    # Add here code to calculate K inter rater agreement

    graf.buildtable2(file_handler2,app2)


# RunAnalizer
def analize(file_handler1, con, app):

    areaOfRisks = 8
    numberOfRisks = 22

    # AllSurveys 12x8
    AllSurveys = [[0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],
                  [0,1,2,3,4,5,6,7,8],]

    file_handler = pd.read_csv(file_handler1)
    numberOfRaters = len(file_handler.index)

    if numberOfRaters > 12 or numberOfRaters < 2:
        print('errore: il numero massimo di raters è 12 e il minimo è 2')
        sys.exit()


    for x  in range(1, numberOfRaters+1):
        for y in range(0, areaOfRisks+1):
            if y == 0 :
                Id = file_handler.loc[(file_handler.ID == x), "ID"].item()
                startTime = file_handler.loc[(file_handler.ID == x), "Start time"].item()
                endTime = file_handler.loc[(file_handler.ID == x), "Completion time"].item()
                email = file_handler.loc[(file_handler.ID == x), "Email"].item()
                name = file_handler.loc[(file_handler.ID == x), "Name"].item()
                AllSurveys[x][y] = RaterInfo(Id, startTime, endTime, email, name)
            if y == 1 :
                strat_risk = file_handler.loc[(file_handler.ID == x), "Strategic Risk"].item()

                try:
                    if "Approval of product/service delivery even if the quality goals are not met" in strat_risk:
                        Quality_goal_not_met = True
                    else:
                        Quality_goal_not_met = False

                    if "Decision impacting credit" in strat_risk:
                        Credit = True
                    else:
                        Credit = False

                    if "Decision impacting infrastructures availability" in strat_risk:
                        Infrastructure = True
                    else:
                        Infrastructure = False

                    if "Decision impacting resources and headcount" in strat_risk:
                        Resource = True
                    else:
                        Resource = False

                    Other = False

                except TypeError:
                    Quality_goal_not_met = False
                    Credit = False
                    Infrastructure = False
                    Resource = False
                    Other = False

                AllSurveys[x][y] = Strategic_risks(Quality_goal_not_met, Credit, Infrastructure, Resource, Other)

            if y == 2 :
                legal_risk = file_handler.loc[(file_handler.ID == x), "Operational Risk - LEGAL"].item()
                try:
                    if "Intellectual Property" in legal_risk:
                        IP = True
                    else:
                        IP = False

                    if "Brand Protection and Reputation" in legal_risk:
                        Brand = True
                    else:
                        Brand = False

                    if "Legal Lawsuit" in legal_risk:
                        Lawsuit = True
                    else:
                        Lawsuit = False

                    Other = False

                except TypeError:
                    IP = False
                    Brand = False
                    Lawsuit = False
                    Other = False

                AllSurveys[x][y] = Legal_risks(IP, Brand, Lawsuit, Other)

            if y == 3 :
                op_risk = file_handler.loc[(file_handler.ID == x), "Operational Risk"].item()
                try:
                    if "Inefficient process" in op_risk:
                        Inefficient_process = True
                    else:
                        Inefficient_process = False

                    if "Ineffective process" in op_risk:
                        Ineffective_process = True
                    else:
                        Ineffective_process = False

                    if "KPIs are not capturing relevant indicators" in op_risk:
                        Ineffective_KPI = True
                    else:
                        Ineffective_KPI = False

                    Other = False

                except TypeError:
                    Inefficient_process = False
                    Ineffective_process = False
                    Ineffective_KPI = False
                    Other = False

                AllSurveys[x][y] = Operational_risks(Inefficient_process,Ineffective_process,Ineffective_KPI,Other)

            if y == 4 :
                compl_risk = file_handler.loc[(file_handler.ID == x), "Compliance Risks"].item()
                try:
                    if "Ability to sell product/service in specific countries" in compl_risk:
                        Country = True
                    else:
                        Country = False

                    if "Health and safety compliance" in compl_risk:
                        Health_and_Safety = True
                    else:
                        Health_and_Safety = False

                    if "ESD Compliance" in compl_risk:
                        ESD = True
                    else:
                        ESD = False

                    if "Product/Service limitations" in compl_risk:
                        Limitations = True
                    else:
                        Limitations = False

                    if "Compliance with International standard" in compl_risk:
                        International_standard = True
                    else:
                        International_standard = False
                    Other = False

                except TypeError:
                    Country = False
                    Health_and_Safety = False
                    ESD = False
                    Limitations = False
                    International_standard = False
                    Other = False

                AllSurveys[x][y] = Compliance_risks(Country, Health_and_Safety, ESD, Limitations, International_standard, Other)

            if y == 5 :
                tech_risk = file_handler.loc[(file_handler.ID == x), "Technical Risks"].item()
                try:
                    if "Testability" in tech_risk:
                        Testability = True
                    else:
                        Testability = False

                    if "Performance" in tech_risk:
                        Performance = True
                    else:
                        Performance = False

                    if "Reliability" in tech_risk:
                        Reliability = True
                    else:
                        Reliability = False

                    if "Availability" in tech_risk:
                        Availability = True
                    else:
                        Availability = False

                    if "Scalability" in tech_risk:
                        Scalability = True
                    else:
                        Scalability = False

                    if "Security" in tech_risk:
                         Security = True
                    else:
                         Security = False

                    if "Maintainability" in tech_risk:
                         Maintainability = True
                    else:
                         Maintainability = False

                    Other = False

                except TypeError:
                    Testability = False
                    Performance = False
                    Reliability = False
                    Availability = False
                    Scalability = False
                    Security = False
                    Maintainability = False
                    Other = False

                AllSurveys[x][y] = Technical_risks(Testability, Performance, Reliability, Availability, Scalability, Security, Maintainability, Other)

            if y == 6 :
                Prob = file_handler.loc[(file_handler.ID == x), "Risk Assessment - Probability"]
                val = Prob.item()
                AllSurveys[x][y] = Likelihood(val)
            if y == 7 :
                Impact_val = file_handler.loc[(file_handler.ID == x), "Risk Assessment - Impact"]
                val = Impact_val.item()
                AllSurveys[x][y] = Impact(val)
            if y == 8 :
                Profile = file_handler.loc[(file_handler.ID == x), "What is the profile cost of the risk?"]
                val = Profile.item()
                AllSurveys[x][y] = Cost_profile(val)



    data_prob = []
    data_impact = []
    data_profile = []
    Quality_goal_not_met_Count = 0
    Credit_Count = 0
    Infrastructure_Count = 0
    Resource_Count = 0
    IP_Count = 0
    Brand_Count = 0
    Lawsuit_Count = 0
    Inefficient_process_Count = 0
    Ineffective_process_Count = 0
    Ineffective_KPI_Count = 0
    Country_Count = 0
    Health_and_Safety_Count = 0
    ESD_Count = 0
    Limitations_Count = 0
    International_standard_Count = 0
    Testability_Count = 0
    Performance_Count = 0
    Reliability_Count = 0
    Availability_Count = 0
    Scalability_Count = 0
    Security_Count = 0
    Maintainability_Count = 0

    for x  in range(1, numberOfRaters+1):
        for y in range(0, areaOfRisks + 1):
             if y == 1:
                if AllSurveys[x][y].Quality_goal_not_met:
                    Quality_goal_not_met_Count += 1
                if AllSurveys[x][y].Credit:
                    Credit_Count += 1
                if AllSurveys[x][y].Infrastructure:
                    Infrastructure_Count += 1
                if AllSurveys[x][y].Resource:
                    Resource_Count += 1
             if y == 2:
                 if AllSurveys[x][y].IP:
                     IP_Count += 1
                 if AllSurveys[x][y].Brand:
                     Brand_Count += 1
                 if AllSurveys[x][y].Lawsuit:
                    Lawsuit_Count += 1
             if y == 3:
                if AllSurveys[x][y].Inefficient_process:
                    Inefficient_process_Count += 1
                if AllSurveys[x][y].Ineffective_process:
                    Ineffective_process_Count += 1
                if AllSurveys[x][y].Ineffective_KPI:
                    Ineffective_KPI_Count += 1
             if y == 4:
                if AllSurveys[x][y].Country:
                    Country_Count += 1
                if AllSurveys[x][y].Health_and_Safety:
                    Health_and_Safety_Count += 1
                if AllSurveys[x][y].ESD:
                    ESD_Count += 1
                if AllSurveys[x][y].Limitations:
                    Limitations_Count += 1
                if AllSurveys[x][y].International_standard:
                    International_standard_Count += 1
             if y == 5:
                 if AllSurveys[x][y].Testability:
                     Testability_Count += 1
                 if AllSurveys[x][y].Performance:
                     Performance_Count += 1
                 if AllSurveys[x][y].Reliability:
                     Reliability_Count += 1
                 if AllSurveys[x][y].Availability:
                     Availability_Count += 1
                 if AllSurveys[x][y].Scalability:
                     Scalability_Count += 1
                 if AllSurveys[x][y].Security:
                     Security_Count += 1
                 if AllSurveys[x][y].Maintainability:
                     Maintainability_Count += 1

             if y == 6:
                data_prob.append(AllSurveys[x][y].NumericValueOfProbability)
             if y == 7:
                 data_impact.append(AllSurveys[x][y].NumericValueOfImpact)
             if y == 8:
                 data_profile.append(AllSurveys[x][y].NumericValueOfProfile)

    prob_mean = round(st.mean(data_prob), 1)
    prob_stdev = round(st.stdev(data_prob), 1)
    prob_mode = round(st.mode(data_prob), 0)
    impact_mean = round(st.mean(data_impact), 1)
    impact_stdev = round(st.stdev(data_impact), 1)
    impact_mode= round(st.mode(data_impact), 0)
    profile_mean = round(st.mean(data_profile), 1)
    profile_stdev = round(st.stdev(data_profile), 1)
    profile_mode = round(st.mode(data_profile), 0)


    #Reliability value: n. of votes closest to mean/number of raters

    prob_count = 0
    for i in data_prob:
        if i == round(prob_mean) :
            prob_count +=1

    prob_rel = round((prob_count/numberOfRaters)*100)

    imp_count = 0
    for i in data_impact:
        if i == round(impact_mean):
            imp_count += 1

    imp_rel = round((imp_count / numberOfRaters) * 100)

    prof_count = 0
    for i in data_profile:
        if i == round(profile_mean):
            prof_count += 1

    prof_rel = round((prof_count / numberOfRaters) * 100)


    array1 = np.array([[prob_mean, prob_mode, prob_stdev],
                                      [impact_mean, impact_mode, impact_stdev],
                                      [profile_mean, profile_mode, profile_stdev]])

    print(array1[0,0])

    print("Quality goal not met risk counter: ", Quality_goal_not_met_Count)
    print("Credit risk counter:", Credit_Count)
    print("Infrastructure risk counter: ", Infrastructure_Count)
    print("Resource risk counter: ", Resource_Count)
    print("prob_mean =",prob_mean)
    print("prob_stdev =",prob_stdev)
    print("prob_mode =",prob_mode)
    print("impact_mean =",impact_mean)
    print("impact_stdev =",impact_stdev)
    print("impact_mode =",impact_mode)
    print("profile_mean =",profile_mean)
    print("profile_stdev =",profile_stdev)
    print("profile_mode =",profile_mode)


    import Grafica as graf
    #### Will make an array for all values ####
    graf.buildtable(Quality_goal_not_met_Count,
    Credit_Count,
    Infrastructure_Count,
    Resource_Count,
    IP_Count,
    Brand_Count,
    Lawsuit_Count,
    Inefficient_process_Count,
    Ineffective_process_Count,
    Ineffective_KPI_Count,
    Country_Count,
    Health_and_Safety_Count,
    ESD_Count,
    Limitations_Count,
    International_standard_Count,
    Testability_Count,
    Performance_Count,
    Reliability_Count,
    Availability_Count,
    Scalability_Count,
    Security_Count,
    Maintainability_Count,
    float(con),
    numberOfRaters,
    numberOfRisks,
    array1,
    prob_rel,
    imp_rel,
    prof_rel,
    app)