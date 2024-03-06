class Exercise:
  """
  Represents a single exercise within a workout plan.
  """
  def __init__(self, name, sets, reps):
    self.name = name
    self.sets = sets
    self.reps = reps

  def __str__(self):
    """Returns a user-friendly string representation of the exercise."""
    return f"{self.name} - {self.sets} sets of {self.reps} repetitions"

def create_workout():
  """
  Prompts the user for information and creates a sample workout.
  """
  exercises = []
  while True:
    exercise_name = input("Enter exercise name (or 'q' to quit): ")
    if exercise_name.lower() == 'q':
      break
    # Нэр орууласны дараа цаашлах
    if not exercise_name:
      print("Please enter a name for the exercise")
      continue
    sets = int(input("Enter number of sets: "))
    reps = int(input("Enter number of repetitions: "))
    exercises.append(Exercise(exercise_name, sets, reps))
  return exercises


def main():
  """
  Drives the program by creating a workout and printing it.
  """
  workout = create_workout()
  print("Your Workout:")
  for exercise in workout:
    print(exercise)

if __name__ == "__main__":
  main()
