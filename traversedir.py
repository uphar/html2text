import os
import sys
import html2text

for file in os.listdir("."):
  if file.endswith(".html"):
    os.system("./html2text.py '" + file + "'")
