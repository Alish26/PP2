import re
def Sol(s):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", s)

print(Sol("Python"))
print(Sol("PythonExercises"))
print(Sol("PythonExercisesPracticeSolution"))
