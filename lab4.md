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
Q9)You now have two commits. Without looking it up: what are the four steps of the loop you just did twice?
git status, git add, git commit, git log
Q10)Why does this file get a special name and a special place, rather than being called notes.md like everything else?
README is a special file that has all the contents of the project so it gets a different place and name.
Q11)What did gh auth login do that means you will not be asked for a password when you push?
When you run gh auth login, it authenticates your GitHub user account and configures Git to automatically use a Personal Access Token (OAuth token) or SSH key for all future Git operations.
Q12)Refresh the repository page on GitHub. What is showing on the front page, and why that file?
README is displaying on that page because github automatically renders the README as the main description of the repository. 
Q13)Run git log --oneline again. Did pushing change your local history in any way?
no pushing did not change local history
Q14)Your repository is private but your TAs can now read it. In your own words, what is the difference between a repository being private and a repository not existing on GitHub at all?
A private repository exists on github but only people with permission can access it. if a repository doesnt exist on github, there is no online repository to access at all. 









