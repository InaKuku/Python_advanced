# 7 Lab
# Modules

# Write a program that encrypts given words by using the characters: &quot;-|_/\()&quot; to structure the word. Use the
# pyfiglet module. You can read more about it here - https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-
# module/
# Directions
# 1. First you need to install the module that we will be using. To install it go to Setting --&gt; Project
# &lt;your_project_name&gt; --&gt; Project Interpreter --&gt; + --&gt; search for pyfiglet --&gt; install package.
# 2. Import the module
# 3. Implement the logic. We will be using the figlet_format method

import pyfiglet

word = input()

print(pyfiglet.figlet_format(word))