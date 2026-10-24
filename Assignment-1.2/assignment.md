 **Assignment 1.2 — Development Environment Setup** that includes both your setup documentation and code templates.

---

## Assignment 1.2 — Development Environment Setup

### 1. Setup Summary & Steps Completed

* **Visual Studio Code:** Downloaded and installed as the primary code editor.
* **Node.js (LTS):** Installed to manage JavaScript runtime environments and `npm` packages.
* **VS Code Extensions:**
* **Live Server** (by Ritwick Dey) — Installed for local server hosting and hot-reloading.
* **Prettier - Code Formatter** — Installed for automatic code styling and formatting.


* **Workspace Structure:**
* Created a root project directory named `web-development-practice`.
* Created three essential web application files: `index.html`, `style.css`, and `script.js`.



---

### 2. Starter Files & Verification Code

#### `index.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Development Environment Setup</title>
                <link rel="stylesheet" href="style.css">
                </head>
                <body>
                    <div class="container">
                            <h1>Environment Setup Complete!</h1>
                                    <p>Visual Studio Code, Node.js, and Live Server are active.</p>
                                        </div>
                                            <script src="script.js"></script>
                                            </body>
                                            </html>

                                            ```

                                            #### `style.css`

                                            ```css
                                            body {
                                                font-family: Arial, sans-serif;
                                                    background-color: #f4f6f9;
                                                        display: flex;
                                                            justify-content: center;
                                                                align-items: center;
                                                                    height: 100vh;
                                                                        margin: 0;
                                                                        }

                                                                        .container {
                                                                            text-align: center;
                                                                                padding: 30px;
                                                                                    background: white;
                                                                                        border-radius: 8px;
                                                                                            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
                                                                                            }

                                                                                            h1 {
                                                                                                color: #2c3e50;
                                                                                                }

                                                                                                ```

                                                                                                #### `script.js`

                                                                                                ```javascript
                                                                                                console.log("Environment verification successful: JavaScript loaded.");

                                                                                                ```

                                                                                                ---

                                                                                                ### 3. Terminal Verification Commands

                                                                                                To verify Node.js and `npm` installations, open your terminal/command prompt and run:

                                                                                                ```bash
                                                                                                node -v
                                                                                                npm -v

                                                                                                ```

                                                                                                **Expected Output Example:**

                                                                                                ```text
                                                                                                v20.18.0
                                                                                                10.8.2

                                                                                                ```

                                                                                                ---

                                                                                                ### 4. Required Submission Screenshots

                                                                                                Be sure to capture and attach the following **3 screenshots** to complete your submission:

                                                                                                1. **VS Code Workspace:** Showing the `web-development-practice` folder expanded in the Explorer sidebar with `index.html`, `style.css`, and `script.js`.
                                                                                                2. **Terminal Output:** Showing the executed `node -v` and `npm -v` commands with their version numbers displayed.
                                                                                                3. **Browser Output:** Showing the web page running via Live Server (at an address like `[http://127.0.0.1:5500/index.html](http://127.0.0.1:5500/index.html)`).