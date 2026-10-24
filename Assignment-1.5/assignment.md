**Assignment 1.5 — GitHub Essentials II**.

---

### Step-by-Step Instructions & Terminal Commands

#### Step 1: Create a Repository on GitHub

1. Log into your [GitHub](https://github.com/) account.
2. Click the **`+`** icon in the top-right corner and select **New repository**.
3. Name your repository (e.g., `web-development-practice`).
4. Select **Public**.
5. **Important:** Leave "Add a README file", "Add .gitignore", and "Choose a license" **unchecked** (since you already have a local repository initialized).
6. Click **Create repository**.

#### Step 2: Connect Your Local Repository to GitHub

Open your terminal inside your project folder (`web-development-practice`) and run the commands provided on your GitHub repository page (replace `your-username` with your actual GitHub username):

```bash
git remote add origin https://github.com/your-username/web-development-practice.git
git branch -M main

```

#### Step 3: Push Your Files (First Push)

Push your existing local commits up to GitHub:

```bash
git push -u origin main

```

#### Step 4: Add a New File and Make a Second Commit

1. Create a new file in your project folder named `README.md` (or modify an existing file). You can do this in VS Code or via terminal:
* *Windows (PowerShell):* `New-Item README.md -ItemType File`
* *Mac/Linux:* `touch README.md`


2. Add a quick description inside `README.md` (e.g., `# Web Development Practice Repository`).
3. Stage, commit, and push this new change:
```bash
git add README.md
git commit -m "docs: add README file for project documentation"
git push

```



#### Step 5: Verify on GitHub

* Refresh your GitHub repository page in your browser.
* Click on the **Commits** link (near the top left, showing your total commit count) to verify that both sets of commits appear correctly in the history.

---

### What to Submit

Copy the **public URL of your GitHub repository** (it will look like `[https://github.com/your-username/web-development-practice](https://github.com/your-username/web-development-practice)`) and paste it as your final submission link!