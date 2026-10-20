 **Assignment 1.4 — Git Essentials I**.

---

### Part 1: Record of Terminal Commands

Open your terminal inside your project folder (`web-development-practice` or any project folder of your choice) and run the following commands sequentially:

#### 1. Verify Git Installation

```bash
git --version

```

*(Expected output: e.g., `git version 2.x.x`)*

#### 2. Configure Your Git Username and Email (Global Configuration)

Run these commands once to set up your identity for commits:

```bash
git config --global user.name "Shalini Gangwar"
git config --global user.email "your-email@example.com"

```

#### 3. Initialize the Git Repository

```bash
git init

```

#### 4. Create and Modify Files (Making 3 Meaningful Commits)

* **Commit 1: Create the initial HTML structure**
* Create an `index.html` file (you can use your text editor or terminal). Add basic HTML boilerplate code to it.
* Run the following commands:
```bash
git status
git add index.html
git commit -m "feat: add initial index.html structure"

```




* **Commit 2: Add CSS styling or page content**
* Open `index.html` and add a heading, paragraph, or link a stylesheet.
* Run the following commands:
```bash
git status
git add index.html
git commit -m "style: add heading and basic content to index page"

```




* **Commit 3: Add a footer or additional sections**
* Make another small change or addition to `index.html` (e.g., add a footer or navigation bar).
* Run the following commands:
```bash
git status
git add index.html
git commit -m "docs/feat: add footer section to complete page layout"

```





#### 5. Verify Your Commit History

To view your history of three commits, run:

```bash
git log --oneline

```

*(This will neatly display your 3 recent commits with their unique hashes and commit messages).*

---

### Part 2: What to Include in Your Submission

1. **Terminal Command Record:** Copy the command blocks used above as proof of your workflow.
2. **Required Screenshots:**
* **Screenshot 1:** Your terminal showing the output of `git log --oneline` (displaying your history of three meaningful commits).
* **Screenshot 2:** Your repository folder (e.g., in VS Code or File Explorer) showing the project structure and files.