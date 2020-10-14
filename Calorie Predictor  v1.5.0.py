version = "1.5.0"

#------------------------------------------------------------------------------#
#                                    Settings.                                 #
#------------------------------------------------------------------------------#
# Personal Stats.
weight = 68.9
height = 178
age = 33

# Calories
calWeightDeficit = -500 # Daily weight change calorie deficit.
calCheatDeficit  = -117 # Daily cheat day calorie deficit.

# Activities
walkMilesPerMin = 0.0585057471 # Miles walked per minute.
walkMets = 3.5 # Mets.

runMilesPerMin = 0.1073333333 # Miles ran per minute.
runMets = 10.5 # METS.
runCoolTime = 5 # Cool down time.

xtMilesPerMin = 0.095 # Miles cross trained per minute. e.g 0.06 * 45 = 2.7 Miles.
xtMets = 5 # METS.
xtCoolTime = 5 # Cool down time.

circuitCals = 130 # Cals for standard circuit session.

messShortTripTime = 10.9 # Minutes for a round trip.
messLongTripTime = 30 # Minutes for a round trip.
gymTripTime = 30 # Minutes for a round trip.


#------------------------------------------------------------------------------#
#                                   Calculations.                              #
#------------------------------------------------------------------------------#
METSconversion = 3.5 * weight / 200 # Used to convert an activities METS value into calories per minute.

walkCalsPerMin = walkMets * METSconversion

runCalsPerMin = runMets * METSconversion
runCoolDown = runCalsPerMin * runCoolTime

xtCalsPerMin = xtMets * METSconversion
xtCoolDown = xtCalsPerMin * xtCoolTime

messTripShortCals = messShortTripTime * walkCalsPerMin
messTripLongCals = messLongTripTime * walkCalsPerMin
gymTripCals = gymTripTime * walkCalsPerMin



#------------------------------------------------------------------------------#
#                              Initialise Variables.                           #
#------------------------------------------------------------------------------#
# These variables are globalised for save persistance.
calsEaten = 0
sHealthBurn = 0
messShortTrips = 0.0
messLongTrips = 0.0
gymTrips = 0.0
walkDuration = 0
runDuration = 0
runOnTreadmill = "n"
xtDuration = 0
circuits = "n"


#------------------------------------------------------------------------------#
#                                   Definitions.                               #
#------------------------------------------------------------------------------#
def dailyCalories():
    global calsEaten, sHealthBurn

    # Main running Que.
    print "\n#--- Daily Calory Calculator v%s ---#\n" %version

    print "---------- Calories. ---------\n"
    calsEaten = getCalsEaten()
    sHealthBurn = getSHealthBurn()

    totalBurn = 0.0
    totalBurn += getBmr()
    totalBurn += calWeightDeficit
    totalBurn += getCalCheatDeficit()
    totalBurn += sHealthBurn
    print "----------- Trips. -----------\n"
    totalBurn += getShortMessTrips()
    totalBurn += getMessLongTrips()
    totalBurn += getGymTrips()
    print "--------- Activities. --------\n"
    totalBurn += getWalkCals()
    totalBurn += getRunCals()
    totalBurn += getXtCals()
    totalBurn += getCurcuitCals()

    showResults(totalBurn)

#----------------------------------------- BMR --------------------------------#
def getBmr():
    bmr = 10 * weight + 6.25 * height - 5 * age + 5
    print "Current BMR:                  %s" %int(bmr)
    return bmr

#---------------------------------- Calories Consumed -------------------------#
def getCalsEaten():
    global calsEaten
    calsEatenQuestion   = raw_input("Calories eaten today?         %s " %str(calsEaten))
    if calsEatenQuestion.isdigit():
        calsEaten = int(calsEatenQuestion)
    return calsEaten

#------------------------------ Calories Already Burnt ------------------------#
def getSHealthBurn():
    global sHealthBurn
    sHealthBurnQuestion = raw_input("Current S-Health cals  burnt? %s " % str(sHealthBurn))
    if sHealthBurnQuestion.isdigit():
        sHealthBurn = int(sHealthBurnQuestion)
    return sHealthBurn

#------------------------------ Calories Already Burnt ------------------------#
def getCalCheatDeficit():
    global calCheatDeficit
    cheatCalsQuestion = raw_input("Cheat calories to deduct?     %s " % str(calCheatDeficit))
    if cheatCalsQuestion.isdigit():
        calCheatDeficit = -(int(cheatCalsQuestion))
    print
    return calCheatDeficit

#--------------------------------- Short Mess Trips ---------------------------#
def getShortMessTrips():
    global messShortTrips
    messTripsQuestion   = raw_input("Remaining short mess trips?   %s " %str(messShortTrips))
    if messTripsQuestion != str(messShortTrips) and messTripsQuestion != "":
        messShortTrips = float(messTripsQuestion)
    result = (messShortTrips * messTripShortCals )
    print "Short mess trip calories      %s\n" %int(result)
    return result

#---------------------------------- Long Mess Trips ---------------------------#
def getMessLongTrips():
    global messLongTrips
    messTripsQuestion   = raw_input("Remaining long mess trips?    %s " %str(messLongTrips))
    if messTripsQuestion != str(messLongTrips) and messTripsQuestion != "":
        messLongTrips = float(messTripsQuestion)
    result = (messLongTrips * messTripLongCals)
    print "Long mess trip calories       %s\n" %int(result)
    return result

#------------------------------------- Gym Trips ------------------------------#
def getGymTrips():
    global gymTrips
    gymTripQuestion   = raw_input("Remaining gym trips?          %s " %str(gymTrips))
    if gymTripQuestion != str(gymTrips) and gymTripQuestion != "":
        gymTrips = float(gymTripQuestion)
    result = (gymTrips * gymTripCals)
    print "Gym trip calories             %s\n" %int(result)
    return result

#-------------------------------------- Walking -------------------------------#
def getWalkCals():
    global walkDuration
    walkQuestion = raw_input("Walking %s mins Later?         " %int(round(walkDuration)))
    if walkQuestion.lower() == "n":
        walkDuration = float(raw_input("Walking for how many minutes? "))

    walkDistance = walkDuration * walkMilesPerMin
    walkCals = walkDuration * walkCalsPerMin

    if walkDuration != 0:
        print "Estimated walking distance:   %.2f" %walkDistance
        print "Walking calories:            ", int(walkCals)
    print

    return walkCals

#-------------------------------------- Running -------------------------------#
def getRunCals():
    global runDuration, runOnTreadmill
    runQuestion = raw_input("Running %s mins later?         " %int(round(runDuration)))
    if runQuestion.lower() == "n":
        runDuration = float(raw_input("For how many minutes?         "))

    if runDuration != 0:
        runDistance = runDuration * runMilesPerMin
        runCals = runDuration * runCalsPerMin

        runGym = raw_input("On a treadmill?               %s " %runOnTreadmill)
        if runGym.lower() == "y" or runGym.lower() == "n":
            runOnTreadmill = runGym.lower()

        if runOnTreadmill.lower() == "y":
            runCals += runCoolDown + gymTripCals

        print "Estimated running distance:   %.2f" %runDistance
        print "Running calories:            ", int(runCals)
    else:
        runCals = 0
    print
    return runCals

#----------------------------------- Cross Trainer ----------------------------#
def getXtCals():
    global xtDuration
    xtQuestion = raw_input("X-Training %s mins later?      " %int(round(xtDuration)))
    if xtQuestion.lower() == "n":
        xtDuration = float(raw_input("For how many minutes?         "))

    if xtDuration != 0:
        xtDistance = xtDuration * xtMilesPerMin
        xtCals = (xtDuration * xtCalsPerMin) + xtCoolDown + gymTripCals
        print "Estimated x-train distance:   %.2f" %xtDistance
        print "X-training calories:         ", int(xtCals)
    else:
        xtCals = 0
    print

    return xtCals

#-------------------------------------- Circuits ------------------------------#
def getCurcuitCals():
    global circuits
    circuitsQuestion = raw_input("Circuits later?               %s " %circuits)

    if circuitsQuestion.lower() == "y" or circuitsQuestion.lower() == "n":
        circuits = circuitsQuestion.lower()

    if circuits == "y":
        cirCals = circuitCals
        print "Circuit calories:            ", cirCals
    else:
        cirCals = 0
    print

    return cirCals

#---------------------------------- Final Calculation. ------------------------#
def showResults(totalCals):
    print "---------- Deficits. ---------\n"
    print "Weight calorie Deficit:      ", calWeightDeficit
    print "Cheat calorie Deficit:       ", calCheatDeficit
    print "\n---------------------------------------"
    print "Total calories to eat today: %s Cals." %int(round(totalCals))
    print "\nProjected day's deficit: -%s cals." %int(round((totalCals - calWeightDeficit - calCheatDeficit) - calsEaten))
    print "\nYou have %s calories remaining." %int(round(totalCals - calsEaten))
    print "---------------------------------------"

#---------------------------------- Over goal advice. -------------------------#
    if (totalCals - calsEaten) < 0:
        print "\n%.2f minutes of walking required." %(abs(totalCals - calsEaten)*(1/walkCalsPerMin))
        print "%.2f minutes of running required." %(abs(totalCals - calsEaten)*(1/runCalsPerMin))
        print "%.2f minutes of x-train required." %(abs(totalCals - calsEaten)*(1/xtCalsPerMin))
#------------------------------------------------------------------------------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
#                                  Main Program.                               #
#------------------------------------------------------------------------------#
choice = ""

while choice.lower() != "n":
    dailyCalories()
    choice = raw_input("\nRun App Again? (y/n): ")
