import re
text = "PythonIsVeryHardLanguage"
print(re.findall('[A-Z][^A-Z]*', text))