import re

with open("access_log.txt") as f:
  content = f.read()

matches = re.findall("[^/]*\.js", content)
print matches
