import time

version = "1.4.4"

#------------------------------------------------------------------------------#
#                                    Settings.                                 #
#------------------------------------------------------------------------------#
calWeightDeficit = -1300 # Daily weight change calorie deficit.
calCheatDeficit  = -117 # Daily cheat day calorie deficit.

hourlyBurn = 81.5 #86 # Cals per idle hour.

walkMilesPerMin = 0.0585057471 # Miles walked per minute. e.g 0.06 * 45 = 2.7 Miles.
walkCalsPerMin = 7.2

runMilesPerMin = 0.1073333333 # Miles ran per minute. e.g 0.12 * 60 = 7.2 Miles.
runCalsPerMin = 11.0
runCoolDown = 80
runOnTreadmill = "n"

xtMilesPerMin = 0.09867 # Miles cross trained per minute. e.g 0.06 * 45 = 2.7 Miles.
xtCalsPerMin = 10.43
xtCoolDown = 50

circuitCals = 130 # Cals for standard circuit session.

messTripShortCals = 80 # Cals for a short round trip to the mess.
messTripLongCals = 220 # Cals for a long round trip to the mess.
gymTripCals = 220


#------------------------------------------------------------------------------#
#                              Initialise Variables.                           #
#------------------------------------------------------------------------------#
# These variables are globalised for save persistance.
calsEaten = 0
currentBurn = 0
messShortTrips = 0.0
messLongTrips = 0.0
gymTrips = 0.0
walkDuration = 0
runDuration = 0
xtDuration = 0
circuits = "n"


#------------------------------------------------------------------------------#
#                                   Definitions.                               #
#------------------------------------------------------------------------------#
def dailyCalories():
    global calsEaten, currentBurn

    # Main running Que.
    print "\n#--- Daily Calory Calculator v%s ---#\n" %version

    calsEaten = getCalsEaten()
    currentBurn = getCurrentBurn()

    totalBurn = 0.0
    totalBurn += calWeightDeficit
    totalBurn += getCalCheatDeficit()
    totalBurn += currentBurn
    totalBurn += getFutureBurn()
    totalBurn += getShortMessTrips()
    totalBurn += getMessLongTrips()
    totalBurn += getGymTrips()
    totalBurn += getWalkCals()
    totalBurn += getRunCals()
    totalBurn += getXtCals()
    totalBurn += getCurcuitCals()

    showResults(totalBurn)

#---------------------------------- Calories Consumed -------------------------#
def getCalsEaten():
    global calsEaten
    calsEatenQuestion   = raw_input("Calories eaten today?         %s " %str(calsEaten))
    if calsEatenQuestion.isdigit():
        calsEaten = int(calsEatenQuestion)
    return calsEaten

#------------------------------ Calories Already Burnt ------------------------#
def getCurrentBurn():
    global currentBurn
    currentBurnQuestion = raw_input("Current burn?                 %s " % str(currentBurn))
    if currentBurnQuestion.isdigit():
        currentBurn = int(currentBurnQuestion)
    return currentBurn

#------------------------------ Calories Already Burnt ------------------------#
def getCalCheatDeficit():
    global calCheatDeficit
    cheatCalsQuestion = raw_input("Cheat calories to deduct?     %s " % str(calCheatDeficit))
    if cheatCalsQuestion.isdigit():
        calCheatDeficit = -(int(cheatCalsQuestion))
    return calCheatDeficit

#-------------------------------------- Time ----------------------------------#
def getDecimalTime():
    hour = time.localtime().tm_hour
    mins = float(time.localtime().tm_min) / 60
    result = hour + mins
    print "Decimal Time:                 %.2f\n" %result
    return result

#----------------------------------- Future Burn ------------------------------#
def getFutureBurn():
    futureBurn = ((24 - getDecimalTime()) * hourlyBurn)
    return futureBurn

#--------------------------------- Short Mess Trips ---------------------------#
def getShortMessTrips():
    global messShortTrips
    messTripsQuestion   = raw_input("Remaining short mess trips?   %s " %str(messShortTrips))
    if messTripsQuestion != str(messShortTrips) and messTripsQuestion != "":
        messShortTrips = float(messTripsQuestion)
    return (messShortTrips * messTripShortCals )

#---------------------------------- Long Mess Trips ---------------------------#
def getMessLongTrips():
    global messLongTrips
    messTripsQuestion   = raw_input("Remaining long mess trips?    %s " %str(messLongTrips))
    if messTripsQuestion != str(messLongTrips) and messTripsQuestion != "":
        messLongTrips = float(messTripsQuestion)
    return (messLongTrips * messTripLongCals)

#------------------------------------- Gym Trips ------------------------------#
def getGymTrips():
    global gymTrips
    gymTripQuestion   = raw_input("Remaining gym trips?          %s " %str(gymTrips))
    print
    if gymTripQuestion != str(gymTrips) and gymTripQuestion != "":
        gymTrips = float(gymTripQuestion)
    return (gymTrips * gymTripCals)


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
    print "Weight calorie Deficit:      ", calWeightDeficit
    print "Cheat calorie Deficit:       ", calCheatDeficit
    print "\n---------------------------------------"
    print "Total calories to eat today: %s Cals." %int(round(totalCals))
    print "\nProjected day's deficit: %s cals." %int(round((totalCals - calWeightDeficit - calCheatDeficit) - calsEaten))
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
