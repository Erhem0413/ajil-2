def create_workout():
  """
  Prompts the user for information and creates a sample workout.
  """
  exercises = []
  while True:
    exercise_name = input("Enter exercise name (or 'q' to quit): ")
    if exercise_name.lower() == 'q':
      break
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of repetitions: "))
    exercises.append(Exercise(exercise_name, sets, reps))
  return exercises
