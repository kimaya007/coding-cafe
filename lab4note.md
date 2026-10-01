Q1) What did --global mean here? What would happen if you left it out? Guess, then check with man git-config or ask.
--global means the setting applies to the entire user account across all repositories on the computer.
Q2)What appeared in ls -a but not in ls? What is inside it?
The ls -a command displays hidden files and folders that are excluded from the standard ls output. 
Q3)Roughly how many files and folders is Git offering to track? Does anything in that list look like something you did not write?
Git is offering to track 9 untracked files. The 4 PDF files (CC - W0.pdf through CC - W3.pdf) are files I downloaded. They are course syllabus documents, lecture slides, or reading materials provided by the instructor and not code written by me.
Q4)Compare this git status with the one from Question 3. What disappeared?
No longer lists anything within .venv/
Q5).gitignore itself shows up as untracked. Should it be committed, or ignored too? Why?
the .gitignore file should be committed to the Git repository. It should not be ignored because it shares rules with your team. The .gitignore file is meant to be a shared project setting. It keeps the repository clean across all machines. 
Q6)README.md moved from one heading to another in the git status output. Which two? In the three-places model from the session, what just happened to it?
from untracked files to changes to be committed. from git add to git commit.
Q7)What did Git print after the commit? How many files did it say changed?
11 files changed, 2947 insertions(+)
Q8)What are the first seven characters of your commit called, and what are they for?
2ed269b. The first seven characters of a Git commit hash serve as a unique short identifier for that specific commit.





