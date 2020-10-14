import time

#------------------------------------------------------------------------------#
#                                    Settings.                                 #
#------------------------------------------------------------------------------#
debugMode = False

calWeightDeficit = -1000 # Daily weight change calorie deficit.
calCheatDeficit  = -100 # Daily cheat day calorie deficit.

hourlyBurn = 86 # Cals per idle hour.

walkMilesPerMin = 0.0585057471 # Miles walked per minute. e.g 0.06 * 45 = 2.7 Miles.
walkCalsPerMin = 7.2

runMilesPerMin = 0.1073333333 # Miles ran per minute. e.g 0.12 * 60 = 7.2 Miles.
runCalsPerMin = 11.0
runCoolDown = 80

xtMilesPerMin = 0.095 # Miles cross trained per minute. e.g 0.06 * 45 = 2.7 Miles.
xtCalsPerMin = 9.0
xtCoolDown = 40

circuitCals = 130 # Cals for standard circuit session.

messTripShortCals = 80 # Cals for a short round trip to the mess.
messTripLongCals = 220 # Cals for a long round trip to the mess.
gymTripCals = 220


#------------------------------------------------------------------------------#
#                              Initialise Variables.                           #
#------------------------------------------------------------------------------#
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
    global calsEaten, currentBurn, messShortTrips, messLongTrips, gymTrips, walkDuration, runDuration, xtDuration, circuits

#-------------------------------------- Time ----------------------------------#
    hour = time.localtime().tm_hour
    mins = float(time.localtime().tm_min) / 60

    decTime = hour + mins

    print "\nDecimal Time:                 %.2f" %decTime


#---------------------------------- Calories Consumed -------------------------#
    calsEatenQuestion   = raw_input("Calories eaten today?         %s " %str(calsEaten))
    if calsEatenQuestion.isdigit():
        calsEaten = int(calsEatenQuestion)

#------------------------------ Calories Already Burnt ------------------------#
    currentBurnQuestion = raw_input("Current Burn?                 %s " % str(currentBurn))
    if currentBurnQuestion.isdigit():
        currentBurn = int(currentBurnQuestion)

#--------------------------------- Short Mess Trips ---------------------------#
    messTripsQuestion   = raw_input("Remaining Short Mess Trips?   %s " %str(messShortTrips))
    if messTripsQuestion != str(messShortTrips) and messTripsQuestion != "":
        messShortTrips = float(messTripsQuestion)

#---------------------------------- Long Mess Trips ---------------------------#
    messTripsQuestion   = raw_input("Remaining Long Mess Trips?    %s " %str(messLongTrips))
    if messTripsQuestion != str(messLongTrips) and messTripsQuestion != "":
        messLongTrips = float(messTripsQuestion)

#------------------------------------- Gym Trips ------------------------------#
    gymTripQuestion   = raw_input("Remaining Gym Trips?          %s " %str(gymTrips))
    if gymTripQuestion != str(gymTrips) and gymTripQuestion != "":
        gymTrips = float(gymTripQuestion)


#-------------------------------------- Walking -------------------------------#
    walkQuestion = raw_input("Walking %s mins Later?         " %int(round(walkDuration)))
    if walkQuestion.lower() == "n":
        walkDuration = float(raw_input("Walking for how many minutes? "))

    walkDistance = walkDuration * walkMilesPerMin
    walkCals = walkDuration * walkCalsPerMin

    if walkDuration != 0:
        print "Est Walking Distance:         %.2f" %walkDistance
        print "Walking Cals:                ", int(walkCals)


#-------------------------------------- Running -------------------------------#
    runQuestion = raw_input("Running %s mins later?         " %int(round(runDuration)))
    if runQuestion.lower() == "n":
        runDuration = float(raw_input("For how many minutes?         "))

    if runDuration != 0:
        runDistance = runDuration * runMilesPerMin
        runCals = runDuration * runCalsPerMin

        runGym = raw_input("On a treadmill?               ")
        if runGym.lower() == "y":
            runCals += runCoolDown + gymTripCals

        print "Est Running Distance:         %.2f" %runDistance
        print "Running Cals:                ", int(runCals)
    else:
        runCals = 0


#----------------------------------- Cross Trainer ----------------------------#
    xtQuestion = raw_input("X-Train %s mins later?         " %int(round(xtDuration)))
    if xtQuestion.lower() == "n":
        xtDuration = float(raw_input("For how many minutes?         "))

    if xtDuration != 0:
        xtDistance = xtDuration * xtMilesPerMin
        xtCals = (xtDuration * xtCalsPerMin) + xtCoolDown + gymTripCals
        print "Est x-train Distance:         %.2f" %xtDistance
        print "X-train Cals:                ", int(xtCals)
    else:
        xtCals = 0


#-------------------------------------- Circuits ------------------------------#
    circuitsQuestion = raw_input("Circuits later?               %s " %circuits)

    if circuitsQuestion.lower() == "y" or circuitsQuestion.lower() == "n":
        circuits = circuitsQuestion.lower()

    if circuits == "y":
        cirCals = circuitCals
        print "Circuit Calories:            ", cirCals
    else:
        cirCals = 0


#---------------------------------- Final Calculation. ------------------------#
    print "Calorie Weight Deficit:      ", calWeightDeficit
    print "Calorie Cheat Deficit:       ", calCheatDeficit

    totalCals = currentBurn + ((24 - decTime) * hourlyBurn) + (messShortTrips * messTripShortCals) + (messLongTrips * messTripLongCals) + (gymTrips * gymTripCals) + walkCals + runCals + xtCals + cirCals + calWeightDeficit + calCheatDeficit

    if debugMode:
        print "\nDEBUG: Total Cals = %s cals burnt + ((24 - %s current time) * %s hourly burn) + (%s short mess trips * %s short mess cals) + (%s long mess trips * %s long mess cals) + (%s gym trips * %s gym cals) + %s walk cals + %s run cals + %s xt cals + %s circuit cals + %s cal weight deficit + %s cal cheat defecit = %s cals" %(currentBurn, decTime, hourlyBurn, messShortTrips, messTripShortCals, messLongTrips,messTripLongCals, gymTrips, gymTripCals, walkCals, runCals, xtCals, cirCals, calWeightDeficit, calCheatDeficit, totalCals)

    print "\n---------------------------------------"
    print "Total calories to eat today: %s Cals." %int(round(totalCals))
    print "\nProjected day's deficit: -%s cals." %int(round((totalCals - calWeightDeficit - calCheatDeficit) - calsEaten))
    print "\nYou have %s calories remaining today." %int(round(totalCals - calsEaten))
    print "---------------------------------------"

#---------------------------------- Over goal advice. -------------------------#
    if (totalCals - calsEaten) < 0:
        print "\n%.2f minutes of walking required." %(abs(totalCals - calsEaten)*(1/walkCalsPerMin))
        print "%.2f minutes of running required." %(abs(totalCals - calsEaten)*(1/runCalsPerMin))
        print "%.2f minutes of x-train required." %(abs(totalCals - calsEaten)*(1/xtCalsPerMin))
#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
#                                  Main Program.                               #
#------------------------------------------------------------------------------#
choice = ""

while choice.lower() != "n":
    dailyCalories()
    choice = raw_input("\nRun App Again? (y/n): ")
