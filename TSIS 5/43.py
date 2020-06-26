import re
s = "PythonTutorialAndExercises"
print(re.findall('[A-Z][^A-Z]*', s))
