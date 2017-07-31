"""This is a ridiculous simulation of high school."""

import sys

INITIAL_WAKEFULNESS = 3.0
SLEEP_POINTS_PER_DAY = 3.0
SLEEP_POINTS_LOST_PER_TURN = 1.0

INITIAL_MUSCLES = 1.0
MUSCLES_LOST_PER_TURN = 0.01
MUSCLES_GAINED_PER_WORKOUT = 0.3

INITIAL_INTELLIGENCE = 1.0
INTELLIGENCE_LOST_PER_TURN = 0.01
INTELLIGENCE_GAINED_PER_STUDY_SESSION = 0.3

CUTE_GIRL_MIN_MUSCLES = 3.0
CUTE_GIRL_MAX_MUSCLES = 6.0
CUTE_GIRL_MIN_INTELLIGENCE = 3.0

wakefulness = INITIAL_WAKEFULNESS
muscles = INITIAL_MUSCLES
intelligence = INITIAL_INTELLIGENCE


def interpret_choice(choice):
    global wakefulness, muscles, intelligence
    if choice == "sleep":
        print("zzzzzz")
        wakefulness += SLEEP_POINTS_PER_DAY
        wakefulness = min(wakefulness, SLEEP_POINTS_PER_DAY)  # Sleeping too much doesn't help.
        wakefulness += SLEEP_POINTS_LOST_PER_TURN  # You don't get sleepy if you're sleeping.
    elif choice == "workout":
        print("Time to get ripped!")
        muscles += MUSCLES_GAINED_PER_WORKOUT
    elif choice == "study":
        print("Time to hit the books!")
        intelligence += INTELLIGENCE_GAINED_PER_STUDY_SESSION
    elif choice == "hangout":
        print("Let's play some video games, dude!")
        print("  -- Schweet!")
    elif choice == "date":
        print("Uh, uh, uh...would you like to go out on a date with me?")
        if muscles < CUTE_GIRL_MIN_MUSCLES:
            print("  -- I think of you more as a friend :(")
        elif muscles > CUTE_GIRL_MAX_MUSCLES:
            print("  -- Gross!!! I don't date guys who use steroids!")
        elif intelligence < CUTE_GIRL_MIN_INTELLIGENCE:
            print("  -- Sorry, you're not my type.")
        else:
            print("  -- Yeah, okay, you're pretty cute! <3")
    else:
        print("Hmm, that doesn't make sense to me.")


def next_turn():
    global wakefulness, muscles, intelligence
    wakefulness -= SLEEP_POINTS_LOST_PER_TURN
    muscles -= MUSCLES_LOST_PER_TURN
    intelligence -= INTELLIGENCE_LOST_PER_TURN
    if wakefulness < 0:
        print("You fell asleep while walking and got hit by a bus!")
        print("Game Over")
        sys.exit(0)
    print("wakefulness: %s muscles: %s intelligence: %s" % (wakefulness, muscles, intelligence))


while True:
    choice = input("What do you want to do next (sleep, workout, study, hangout, date)? ")
    interpret_choice(choice)
    next_turn()
