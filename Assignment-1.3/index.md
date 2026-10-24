**Assignment 1.3 — Terminal & Developer Workflow**.

---

### Part 1: Record of Terminal Commands

You can copy and run these commands step-by-step in your terminal (Command Prompt/PowerShell on Windows, or Terminal on Mac/Linux) to create the required folder structure and practice the workflow.

#### 1. Create and Navigate to the Main Folder

```bash
mkdir web-development-practice
cd web-development-practice

```

#### 2. Create Week Folders

* **For Windows (PowerShell / Command Prompt):**
```bash
mkdir week-1, week-2, week-3

```


* **For Mac / Linux / Git Bash:**
```bash
mkdir week-1 week-2 week-3

```



#### 3. Create an `index.html` File Inside Each Folder

* **For Windows (PowerShell):**
```bash
New-Item week-1/index.html, week-2/index.html, week-3/index.html -ItemType File

```


* **For Windows (Command Prompt):**
```cmd
type nul > week-1\index.html & type nul > week-2\index.html & type nul > week-3\index.html

```


* **For Mac / Linux / Git Bash:**
```bash
touch week-1/index.html week-2/index.html week-3/index.html

```



#### 4. Practice Navigating, Renaming, and Deleting (Bonus / Practice Commands)

* **Navigate into a folder:** `cd week-1`
* **Go back to the parent folder:** `cd ..`
* **Rename a folder:**
* *Windows:* `ren week-3 week-three`
* *Mac/Linux:* `mv week-3 week-three`


* **Delete a test file/folder:**
* *Windows:* `del filename` or `rmdir foldername`
* *Mac/Linux:* `rm filename` or `rm -rf foldername`



#### 5. Open the Project in VS Code Directly from the Terminal

Make sure you are in the root directory (`web-development-practice`), then run:

```bash
code .

```

---

### Part 2: What to Include in Your Submission

1. **Record of Terminal Commands:** Copy the command blocks used above and paste them into your submission document.
2. **Screenshot of the Final Folder Structure:** Take a screenshot of your VS Code Explorer sidebar showing the `web-development-practice` folder expanded with `week-1`, `week-2`, and `week-3`, each containing their respective `index.html` files.