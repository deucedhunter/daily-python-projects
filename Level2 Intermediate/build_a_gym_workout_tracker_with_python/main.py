"""
https://dailypythonprojects.substack.com/p/build-a-gym-workout-tracker-with
Project Description

This program helps you track your workout routines, sets, reps, and weights. It lets you add exercises, record your progress, and review past workouts. Perfect for gym users who want to log their progress.
How the project works

The program is command line based and it starts by letting the user choose any of the options.

    At first, the user may want to add an exercise type. Here the user adds a pushup and a squat exercise:

Once the user has added a few exercise types, they can log an exercise whenever they perform that exercise. Here the user has logged in the pushups exercise, declaring 3 sets of 10 reps each and 0 as extra weight.

    Finally, the user see their progress by choosing option 3. View Progress:

    As you can see in the last line, the program shows that the user has done a session and it displays the details about that session.

You can use procedural or functional programming to code this project, but we used object-oriented programming in the solution in the “Show Code” button. For simplicity, we are not saving the user data in any files, but simply inside the program temporarily.
"""

PROMPT = """Gym Tracker Options:
1. Add Exercise
2. Log Workout
3. View Progress
4. Exit
Choose an option: """
exercise_list = {}
while True:
    option = int(input(PROMPT))

    match option:
        case 1:
            new_exercise = input("Enter Exercise name: ")
            exercise_list[new_exercise] = {"sets": 0, "reps": 0, "kg": 0}
            print("Added exercise:", new_exercise)
        case 2:
            current_exercise = input("Enter exercise name: ")
            sets = input("Enter number of sets: ")
            reps = input("Enter number of reps: ")
            kg = float(input("Enter weight in kg: "))
            exercise_list[current_exercise] = {
                "sets": sets,
                "reps": reps,
                "kg": kg
            }
            print(f"Logged {sets} sets of {reps} reps at {kg} kg for {current_exercise}.")
        case 3:
            print("\nProgress for Squats:\n")

            for exercise in exercise_list:
                print(f"Progress for {exercise}:")
                sets = exercise_list[exercise]["sets"]
                reps = exercise_list[exercise]["reps"]
                kg = exercise_list[exercise]["kg"]
                print(f"Session 1: {sets} sets of {reps} reps at {kg} kg")
        case 4:
            break
