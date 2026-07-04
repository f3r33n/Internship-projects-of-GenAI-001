 Internship Project: GenAI-001 (Gemini API Integration)

This repository contains the core implementation files for a Generative AI internship project focused on integrating Google's Gemini models. The codebase demonstrates how to programmatically connect with the Gemini API to generate structured content using the updated SDK.

---

 Features
* Uses the modern `google-genai` SDK.
* Integrates the high-efficiency `gemini-2.5-flash` model.
* Demonstrates hyperparameter adjustment (`temperature` control) for text generation.

---

 Prerequisites & Installation

### 1. Install Dependencies
You must have Python installed. Install the official Google GenAI library using `pip`:

pip install google-genai




Conversation with Gemini
i very shot tell me hwo do u activate venv on linux mint vs code

To activate a Python virtual environment (venv) inside VS Code on Linux Mint, you have two quick options: the automatic way (recommended) or the manual way via the terminal.

Method 1: The VS Code Way (Automated)
VS Code can handle the activation for you every time you open a new terminal.

Open your project folder in VS Code.

Open the Command Palette by pressing Ctrl + Shift + P.

Type and select: Python: Select Interpreter.

Choose the interpreter that points to your virtual environment (it will usually say ('venv': venv) next to it).

Open a new terminal (`Ctrl + Shift + ``), and VS Code will automatically run the activation command for you.

Method 2: The Terminal Way (Manual)
If you just want to activate it directly in the built-in terminal, run the following command from your project root folder:

Bash
source venv/bin/activate
(If your virtual environment folder is named something else, replace venv with your folder's name, e.g., source .venv/bin/activate).

You will know it worked because you'll see (venv) appear at the beginning of your terminal prompt line.

Quick Tip: If you ever need to turn it off, just type deactivate in the terminal.

what issue is this (venv) fereen@15sdu2x:~/CODES /Subject 001 MIrai$ pip install google gen-ai

Collecting google

  Downloading google-3.0.0-py2.py3-none-any.whl.metadata (627 bytes)

ERROR: Could not find a version that satisfies the requirement gen-ai (from versions: none)

ERROR: No matching distribution found for gen-ai

(venv) fereen@15sdu2x:~/CODES /Subject 001 MIrai$ 

The issue is that gen-ai is not a valid package name on PyPI (the Python Package Index), so pip is throwing an error trying to find it.

If you are looking to use Google's Gemini models in Python, the official, current SDK package you want to install is google-genai (with a hyphen, not a space or underscore).

Run this command instead to install the correct library:

Bash
pip install google-genai
Why did it fail?
When you typed pip install google gen-ai (with a space), pip interpreted it as a request to install two separate packages:

google (which exists but is an old, empty placeholder package).

gen-ai (which does not exist, causing the crash).

Once you run pip install google-genai, you can import it in your code using:

Python
from google import genai
i need to push myc ode on vs code to repo https://github.com/f3r33n/Internship-projects-of-GenAI-001.git i know like git init then git add . then git commit git push -m etc

You are very close! The exact workflow has just one or two small tweaks, especially since you need to link your local code to that specific remote GitHub URL.

Here is the exact sequence of commands to run in your VS Code terminal to get your code pushed safely:

The Push Sequence
1
Initialize Git
Only if you haven't already
Bash
git init
This creates the hidden .git folder in your project directory.

2
Stage your files
Prepares files for commit
Bash
git add .
3
Commit your changes
Creates the local snapshot
Bash
git commit -m "Initial commit"
(Note: The -m flag stands for "message". Your text goes inside the quotes).

4
Rename the default branch
Ensures compatibility with GitHub
Bash
git branch -M main
GitHub uses main as the default branch name instead of master. This command renames it locally.

5
Link to your GitHub repo
Tells Git where to send the code
Bash
git remote add origin https://github.com/f3r33n/Internship-projects-of-GenAI-001.git
6
Push to GitHub
Final step
Bash
git push -u origin main
The -u flag sets the "upstream" tracking, meaning next time you want to push from this branch, you can just type a simple git push.


⚠️ Quick Security Warning: Since this is a GenAI project, make sure you do not push your API keys or .env files to GitHub. If you have a .env file, add it to a .gitignore file before running git add ..

oh but i dont want to push whole of my venv i wanna push only apitest.py file

Smart move. You definitely want to keep that massive venv folder off GitHub.

To push only your apitest.py file, you have two options. The cleanest way is to use a .gitignore file so you never accidentally push the environment later, but you can also just add the single file manually right now.

Here is how to do both.

Option 1: The Quick Fix (Add just the one file)
Instead of using git add . (which adds everything), specify the exact file name. Run these commands in your terminal:

Bash
git init
git add apitest.py
git commit -m "Add GenAI API test script"
git branch -M main
git remote add origin https://github.com/f3r33n/Internship-projects-of-GenAI-001.git
git push -u origin main
Option 2: The Best Practice (Use a .gitignore)
If you plan to add more files later, it's highly recommended to tell Git to permanently ignore the venv folder.

Create a new file in your project root named exactly .gitignore

Open it and type your virtual environment folder name inside it (usually just venv/ or .venv/ depending on what you named it):

Plaintext
venv/
.env
(I added .env in there too, just in case you store your API keys in one later).

Now you can safely use the standard commands without worrying:

Bash
git add .
git commit -m "Initial commit ignoring venv"
git push -u origin main
(Note: If you already ran git add . in a previous step, type git rm -r --cached venv to untrack the virtual environment before committing).

what rule did i violate?

You violated GitHub's Push Protection rule against committing exposed secrets.

GitHub explicitly blocked your push because it detected a hardcoded GCP API Key on line 3 of your apitest.py file inside the commit history.

How to Fix This
Even if you changed the code in your editor to "your_api_key_here" just now, the secret is still recorded inside your Git history (in commit ae61ef1). You need to completely reset or change that commit before GitHub will let you push.

Here is the quickest way to fix it safely:

Step 1: Undo the bad commit but keep your code
Run this command to undo your last commit while keeping your file exactly as it is right now in your editor:

Bash
git reset --soft HEAD~1
Step 2: Set up environment variables (Best Practice)
Instead of putting your key in the code, use Linux environment variables.

In your terminal, temporarily set it by running:

Bash
export GEMINI_API_KEY="your_actual_api_key_here"
Update line 3 of your apitest.py to initialize the client cleanly without exposing strings:

Python
client_creation = genai.Client() 
# The SDK automatically looks for the GEMINI_API_KEY environment variable!
Step 3: Re-commit and push
Now that the key is removed from the file, add, commit, and push again:

Bash
git add apitest.py
git commit -m "Fix: remove hardcoded api key and use environment variables"
git push -u origin main
i dontw ant to create an env and i dontw antto create aheacahe of gitignore juts tell me how can i do something and push this file

If you just want to get this file pushed immediately without dealing with .gitignore files or environment variables, you can temporarily strip the API key parameter entirely so the code is completely clean, commit it, and push.

Since the google-genai library automatically searches for an environment variable named GEMINI_API_KEY by default, you can actually leave the parentheses empty in your code.

Here is exactly what to do step-by-step to bypass the blocker right now:

Step 1: Clean the Code
Change line 3 in your apitest.py file to look exactly like this:

Python
client_creation = genai.Client()
(Make sure there is no text, no "your_api_key_here", and no api_key= inside the parentheses).

Step 2: Clear the Blocked History
Because Git already recorded your API key in the previous failed attempt, you must reset your local history so GitHub stops blocking you. Run this command in your VS Code terminal:

Bash
git reset --soft HEAD~1
Step 3: Re-Add, Commit, and Push
Now, stage your clean file and push it directly to your repository:

Bash
git add apitest.py
git commit -m "Initial clean commit"
git push -u origin main
How to run it locally later without an env file
Whenever you want to run your script locally on Linux Mint, you can just pass your key directly in the terminal right before execution without saving it to any files:

Bash
GEMINI_API_KEY="your_actual_key_here" python apitest.py
whast it saying h

        pull

(venv) fereen@15sdu2x:~/CODES /Subject 001 MIrai$ git push -u main origin

error: src refspec origin does not match any

error: failed to push some refs to 'main'

(venv) fereen@15sdu2x:~/CODES /Subject 001 MIrai$ 

The error is happening because the names in your push command are swapped.

You typed git push -u main origin, but the correct order is always git push -u origin main (Remote name first, then Branch name).

Because they were flipped, Git got confused and thought you were trying to push a local branch named "origin" to a remote named "main".

The Fix
Simply run the command with the names in the right order:

Bash
git push -u origin main
What if it asks you to pull?
If the terminal outputs a message about "updates were rejected because the remote contains work that you do not have locally" (hinted by the "pull" text in your message), it means GitHub has a default file (like a README.md) that your local computer doesn't have yet.

If that happens, run this command to force your local file onto GitHub and overwrite it:

Bash
git push -u origin main --force
man whast it saying again

Looking at image_a16062.jpg, GitHub is still blocking the push because of the exact same old commit (ae61ef1654...).

Even though you changed your code in the editor, Git works like a time machine—it is trying to upload the history where that API key was still present in the first commit.

Also, look closely at the terminal output: Enumerating objects: 3997. That means Git is still trying to push 3,997 files (your entire venv folder!). The reset command didn't fully unstage or clear the old history.

Let's wipe out that broken local Git history completely and start fresh. It takes 10 seconds. Run these commands one by one:

Step 1: Nuclear Option (Reset Git completely)
Delete the local hidden Git tracking folder so it forgets the bad history and the thousands of staged venv files:

Bash
rm -rf .git
Step 2: Fresh Init & Add ONLY the one file
Re-initialize Git and explicitly add only your test script:

Bash
git init
git add apitest.py
(Verify your apitest.py line 3 looks like client_creation = genai.Client() before running the next step).

Step 3: Commit and Push
Bash
git commit -m "Initial clean commit"
git branch -M main
git remote add origin https://github.com/f3r33n/Internship-projects-of-GenAI-001.git
git push -u origin main --force
This ensures only apitest.py goes up, and GitHub will accept it immediately because the secret never existed in this brand-new history.

give me next comamnds to push it finally

Based on image_a16062.jpg, you are still working out of the same terminal state where the previous commands failed. Since we need to run the clean slate sequence to bypass those 3,997 files and the blocked secret history, run these exact commands in order:

Bash
rm -rf .git
git init
git add apitest.py
git commit -m "Initial clean commit"
git branch -M main
git remote add origin https://github.com/f3r33n/Internship-projects-of-GenAI-001.git
git push -u origin main --force
Once that finishes, check your GitHub repository link—your file will be live!

give me aread me for this it was an internship project teh code is this from google import genai



client_creation = genai.Client

the_response = client_creation.models.generate_content(

model = "gemini-2.5-flash",

config = {"temperature" :2.0},

contents = "tell me a fact about sleep in one sentence"

)

answer =the_response.text

print(answer) and its how u chat with api

Here is a clean, professional README.md tailored for your internship project repo. It matches the exact code structure you are using while showing how to actually run it.

Markdown
# Internship Project: GenAI-001 (Gemini API Integration)

This repository contains the core implementation files for a Generative AI internship project focused on integrating Google's Gemini models. The codebase demonstrates how to programmatically connect with the Gemini API to generate structured content using the updated SDK.

---

## Features
* Uses the modern `google-genai` SDK.
* Integrates the high-efficiency `gemini-2.5-flash` model.
* Demonstrates hyperparameter adjustment (`temperature` control) for text generation.

---

## Prerequisites & Installation

### 1. Install Dependencies
You must have Python installed. Install the official Google GenAI library using `pip`:

```bash
pip install google-genai
2. Set Up Your API Key
The SDK automatically looks for a GEMINI_API_KEY environment variable. Before executing the script, export your API key in your Linux Mint terminal:

Bash
export GEMINI_API_KEY="your_actual_gemini_api_key"
How to Run the Project
The primary script (apitest.py) initializes the client, configures parameters, and requests a response from the model.

Code Overview (apitest.py)
Python
from google import genai

# Initialize the client (auto-detects the environment variable)
client_creation = genai.Client()

# Generate content with custom parameters
the_response = client_creation.models.generate_content(
    model="gemini-2.5-flash",
    config={"temperature": 2.0},
    contents="tell me a fact about sleep in one sentence"
)

# Output the response
answer = the_response.text
print(answer)
Execution
Run the script inside your terminal using Python:


python apitest.py
