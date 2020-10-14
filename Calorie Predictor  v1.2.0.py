import time

#------------------------------------------------------------------------------#
#                                    Settings.                                 #
#------------------------------------------------------------------------------#
debugMode = False

calDeficit = -1100 # Daily calorie deficit.

hourlyBurn = 86 # Cals per idle hour.

runMilesPerMin = 0.1073333333 # Miles ran per minute. e.g 0.12 * 60 = 7.2 Miles.
runCalsPerMin = 11.0

walkMilesPerMin = 0.0585057471 #Miles walked per minute. e.g 0.06 * 45 = 2.7 Miles.
walkCalsPerMin = 7.2

circuitCals = 130 # Cals for standard circuit session.

messTripCals = 80 # Cals for a round trip to the mess.


#------------------------------------------------------------------------------#
#                              Initialise Variables.                           #
#------------------------------------------------------------------------------#
calsEaten = 0
currentBurn = 0
messTrips = 0.0
walk = "n"
walkDuration = 0
run = "n"
runDuration = 0
circuits = "n"


#------------------------------------------------------------------------------#
#                                   Definitions.                                    #
#------------------------------------------------------------------------------#
def run():
    global calsEaten, currentBurn, messTrips,  walkDuration, runDuration,  circuits

#-------------------------------------- Time ----------------------------------#
    hour = time.localtime().tm_hour
    mins = float(time.localtime().tm_min) / 60

    decTime = hour + mins

    print "\nDecimal Time:         %.2f" %decTime


#--------------------------------- Cals & Mess Trips --------------------------#
    calsEatenQuestion   = raw_input("Calories eaten today? %s " %str(calsEaten))
    if calsEatenQuestion.isdigit():
        calsEaten = int(calsEatenQuestion)

    currentBurnQuestion = raw_input("Current Burn?         %s " % str(currentBurn))
    if currentBurnQuestion.isdigit():
        currentBurn = int(currentBurnQuestion)

    messTripsQuestion   = raw_input("Remaining Mess Trips? %s " %str(messTrips))
    if messTripsQuestion != str(messTrips) and messTripsQuestion != "":
        messTrips = float(messTripsQuestion)


#-------------------------------------- Walking -------------------------------#
    walkQuestion = raw_input("Walking %s mins Later? " %int(round(walkDuration)))
    if walkQuestion.lower() == "n":
        walkDuration = float(raw_input("Walking for how many minutes? "))

    walkDistance = walkDuration * walkMilesPerMin
    walkCals = walkDuration * walkCalsPerMin

    if walkDuration != 0:
        print "Est Walking Distance: %.2f" %walkDistance
        print "Walking Cals:        ", int(walkCals)


#-------------------------------------- Running -------------------------------#
    runQuestion = raw_input("Running %s mins later? " %int(round(runDuration)))
    if runQuestion.lower() == "n":
        runDuration = float(raw_input("For how many minutes? "))

    if runDuration != 0:
        runDistance = runDuration * runMilesPerMin
        runCals = (runDuration * runCalsPerMin) + 40 + 120
        print "Est Running Distance: %.2f" %runDistance
        print "Running Cals:        ", int(runCals)
    else:
        runCals = 0


#-------------------------------------- Circuits ------------------------------#
    circuitsQuestion = raw_input("Circuits later?       %s " %circuits)

    if circuitsQuestion.lower() == "y" or circuitsQuestion.lower() == "n":
        circuits = circuitsQuestion.lower()

    if circuits == "y":
        cirCals = circuitCals
        print "Circuit Calories:    ", cirCals
    else:
        cirCals = 0


#---------------------------------- Final Calculation. ------------------------#
    print "Calorie Deficit:     ", calDeficit

    totalCals = currentBurn + ((24 - decTime) * hourlyBurn) + (messTrips * messTripCals) + walkCals + runCals + cirCals + calDeficit

    if debugMode:
        print "\nDEBUG: Total Cals = %s cals burnt + ((24 - %s current time) * %s hourly burn) + (%s mess trips * %s mess cals) + %s walk cals + %s run cals + %s circuit cals + %s cal deficit = %s cals" %(currentBurn, decTime, hourlyBurn, messTrips, messTripCals, walkCals, runCals, cirCals, calDeficit, totalCals)

    print "\n---------------------------------------"
    print "Total calories to eat today: %s Cals." %int(round(totalCals))
    print "\nYou have %s calories remaining today." %int(round(totalCals - calsEaten))
    print "---------------------------------------"

#---------------------------------- Over goal advice. -------------------------#
    if (totalCals - calsEaten) < 0:
        print "\n%.2f minutes of walking required." %(abs(totalCals - calsEaten)*(1/walkCalsPerMin))
        print "%.2f minutes of running required." %(abs(totalCals - calsEaten)*(1/runCalsPerMin))

#------------------------------------------------------------------------------#


#------------------------------------------------------------------------------#
#                                  Main Program.                               #
#------------------------------------------------------------------------------#
choice = ""

while choice.lower() != "n":
    run()
    choice = raw_input("\nRun App Again? (y/n): ")
