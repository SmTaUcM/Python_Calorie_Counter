import time

version = "1.7.0"

#------------------------------------------------------------------------------#
#                                    Settings.                                 #
#------------------------------------------------------------------------------#
# Personal Stats.
weight = 67.4
height = 178
age = 33
wakeTime = 5.6
bedTime = 23.0

# Calories.
calWeightDeficit = -1300 # Daily weight change calorie deficit.
calCheatDeficit  = -117 # Daily cheat day calorie deficit.

# Activities.
sittingMETS = 1.3
lyingMETS = 1.0

walkMilesPerMin = 0.0585057471 # Miles walked per minute. e.g 0.06 * 45 = 2.7 Miles.
walkCalsPerMin = 7.2
walkMets = 4.3 # Mets.
walkFitbitOffset = 1.41 # Percentage adjustment to match FitBit walking calories.

runMilesPerMin = 0.1073333333 # Miles ran per minute. e.g 0.12 * 60 = 7.2 Miles.
runCalsPerMin = 11
runMets = 10.5 # METS.
runCoolTime = 5 # Cool down time.

xtMilesPerMin = 0.09867 # Miles cross trained per minute. e.g 0.06 * 45 = 2.7 Miles.
xtCalsPerMin = 10.43
xtMets = 5 # METS.
xtCoolTime = 5 # Cool down time.

circuitCalsPerMin = 2.88
circuitMets = 8 # METS.

messShortTripTime = 10.9 # Minutes for a round trip.
messLongTripTime = 30 # Minutes for a round trip.
gymTripTime = 30 # Minutes for a round trip.


#------------------------------------------------------------------------------#
#                                   Calculations.                              #
#------------------------------------------------------------------------------#
METSconversion = 3.5 * weight / 200 # Used to convert an activity's METS value into calories per minute.

sittingCalsPerMin = sittingMETS * METSconversion
lyingCalsPerMin = lyingMETS * METSconversion

##walkCalsPerMin = (walkMets * METSconversion) * walkFitbitOffset

##runCalsPerMin = runMets * METSconversion
runCoolDown = runCalsPerMin * runCoolTime

##xtCalsPerMin = xtMets * METSconversion
xtCoolDown = xtCalsPerMin * xtCoolTime

##circuitCalsPerMin = circuitMets * METSconversion

messTripShortCals = messShortTripTime * walkCalsPerMin
messTripLongCals = messLongTripTime * walkCalsPerMin
gymTripCals = gymTripTime * walkCalsPerMin


#------------------------------------------------------------------------------#
#                              Initialise Variables.                           #
#------------------------------------------------------------------------------#
# These variables are globalised for save persistance.
decimalTime = 0.0
calsEaten = 0
currentBurn = 0
messShortTrips = 0.0
messLongTrips = 0.0
gymTrips = 0.0
walkDuration = 0
runDuration = 0
runOnTreadmill = "n"
xtDuration = 0
circuitDuration = 0


#------------------------------------------------------------------------------#
#                                   Definitions.                               #
#------------------------------------------------------------------------------#
def dailyCalories():
    global calsEaten, currentBurn, decimalTime

    # Main running Que.
    print "\n#--- Daily Calory Calculator v%s ---#\n" %version

    calsEaten = getCalsEaten()
    currentBurn = getCurrentBurn()

    totalBurn = 0.0
    totalBurn += calWeightDeficit
    totalBurn += getCalCheatDeficit()
    totalBurn += currentBurn
    decimalTime = getDecimalTime()
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

    morningHours = wakeTime - decimalTime
    if morningHours < 0:
        morningHours = 0.0

    eveningHours = 24 - bedTime
    if decimalTime > bedTime:
        eveningHours =  24 - decimalTime

    dayHours = 24.0 - decimalTime - (morningHours + eveningHours)

    futureBurn = morningHours * 60 *lyingCalsPerMin

    futureBurn += dayHours * 60 *sittingCalsPerMin

    futureBurn += eveningHours * 60 *lyingCalsPerMin

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
            runCals += runCoolDown

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
        xtCals = (xtDuration * xtCalsPerMin) + xtCoolDown
        print "Estimated x-train distance:   %.2f" %xtDistance
        print "X-training calories:         ", int(xtCals)
    else:
        xtCals = 0
    print

    return xtCals


#-------------------------------------- Circuits ------------------------------#
def getCurcuitCals():
    global circuitDuration
    circuitsQuestion = raw_input("Circuits for %s mins later?   " %circuitDuration)

    if circuitsQuestion.lower() == "n":
        circuitDuration = float(raw_input("For how many minutes?         "))

    if circuitDuration != 0:
        cirCals = circuitDuration *circuitCalsPerMin
        print "Circuit calories:            ", int(cirCals)
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
