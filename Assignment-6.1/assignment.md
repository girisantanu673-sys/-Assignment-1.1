**Assignment 6.1 — Box Model Inspection**.

1. **`style.css`** (Styles demonstrating `content-box` vs `border-box` behaviors, distinct padding, borders, and margins)
2. **`index.html`** (Sample webpage with 3 distinct boxes, headings, and paragraphs)

---

### File 1: `style.css` (External Stylesheet)

```css
/* ==========================================================================
   Assignment 6.1 — Box Model Inspection Stylesheet
      Author: Shalini Gangwar
         ========================================================================== */

         :root {
             --bg-color: #f8fafc;
                 --card-bg: #ffffff;
                     --text-color: #334155;
                         --border-color: #cbd5e1;
                         }

                         * {
                             margin: 0;
                                 padding: 0;
                                 }

                                 body {
                                     font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                                         background-color: var(--bg-color);
                                             color: var(--text-color);
                                                 line-height: 1.6;
                                                     padding: 40px 20px;
                                                     }

                                                     .container {
                                                         max-width: 700px;
                                                             margin: 0 auto;
                                                             }

                                                             h1 {
                                                                 text-align: center;
                                                                     color: #0f172a;
                                                                         margin-bottom: 30px;
                                                                             font-size: 1.8rem;
                                                                             }

                                                                             /* Base Card Typography */
                                                                             h2 {
                                                                                 font-size: 1.2rem;
                                                                                     margin-bottom: 8px;
                                                                                         color: #1e3a8a;
                                                                                         }

                                                                                         p {
                                                                                             font-size: 0.95rem;
                                                                                                 color: #475569;
                                                                                                 }

                                                                                                 /* --------------------------------------------------------------------------
                                                                                                    Box 1: content-box (Padding and border are ADDED to the set width)
                                                                                                       -------------------------------------------------------------------------- */
                                                                                                       .box-content {
                                                                                                           box-sizing: content-box;
                                                                                                               width: 350px;
                                                                                                                   padding: 25px;
                                                                                                                       border: 8px solid #ef4444; /* Red border */
                                                                                                                           margin: 20px auto;
                                                                                                                               background-color: var(--card-bg);
                                                                                                                                   box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                                                                                                                                   }

                                                                                                                                   /* --------------------------------------------------------------------------
                                                                                                                                      Box 2: border-box (Padding and border are INCLUDED within the set width)
                                                                                                                                         -------------------------------------------------------------------------- */
                                                                                                                                         .box-border {
                                                                                                                                             box-sizing: border-box;
                                                                                                                                                 width: 350px;
                                                                                                                                                     padding: 25px;
                                                                                                                                                         border: 8px solid #22c55e; /* Green border */
                                                                                                                                                             margin: 20px auto;
                                                                                                                                                                 background-color: var(--card-bg);
                                                                                                                                                                     box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                                                                                                                                                                     }

                                                                                                                                                                     /* --------------------------------------------------------------------------
                                                                                                                                                                        Box 3: Custom Spacing Box
                                                                                                                                                                           -------------------------------------------------------------------------- */
                                                                                                                                                                           .box-custom {
                                                                                                                                                                               box-sizing: border-box;
                                                                                                                                                                                   width: 100%;
                                                                                                                                                                                       max-width: 450px;
                                                                                                                                                                                           padding: 30px 40px;
                                                                                                                                                                                               border: 4px dashed #2563eb; /* Blue dashed border */
                                                                                                                                                                                                   margin: 30px auto;
                                                                                                                                                                                                       background-color: var(--card-bg);
                                                                                                                                                                                                           box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
                                                                                                                                                                                                           }

                                                                                                                                                                                                           ```

                                                                                                                                                                                                           ---

                                                                                                                                                                                                           ### File 2: `index.html` (HTML File)

                                                                                                                                                                                                           ```html
                                                                                                                                                                                                           <!DOCTYPE html>
                                                                                                                                                                                                           <html lang="en">
                                                                                                                                                                                                           <head>
                                                                                                                                                                                                               <meta charset="UTF-8">
                                                                                                                                                                                                                   <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                                                                                                                                                                                                       <title>Box Model Inspection - Shalini Gangwar</title>
                                                                                                                                                                                                                           <meta name="description" content="Assignment 6.1 box model inspection webpage demonstrating content-box and border-box behaviors.">
                                                                                                                                                                                                                               <link rel="icon" type="image/png" href="favicon.png">
                                                                                                                                                                                                                                   <link rel="stylesheet" href="style.css">
                                                                                                                                                                                                                                   </head>
                                                                                                                                                                                                                                   <body>

                                                                                                                                                                                                                                       <main class="container">
                                                                                                                                                                                                                                               <h1>CSS Box Model Inspection</h1>
                                                                                                                                                                                                                                                       
                                                                                                                                                                                                                                                               <!-- Box 1: Content Box -->
                                                                                                                                                                                                                                                                       <div class="box-content">
                                                                                                                                                                                                                                                                                   <h2>Box 1: box-sizing: content-box</h2>
                                                                                                                                                                                                                                                                                               <p>Width is set to 350px, but padding (25px × 2) and border (8px × 2) are added on top, making the total rendered width <strong>416px</strong>.</p>
                                                                                                                                                                                                                                                                                                       </div>

                                                                                                                                                                                                                                                                                                               <!-- Box 2: Border Box -->
                                                                                                                                                                                                                                                                                                                       <div class="box-border">
                                                                                                                                                                                                                                                                                                                                   <h2>Box 2: box-sizing: border-box</h2>
                                                                                                                                                                                                                                                                                                                                               <p>Width is set to 350px, and padding plus border are contained <em>inside</em> the 350px boundary, keeping total width exactly <strong>350px</strong>.</p>
                                                                                                                                                                                                                                                                                                                                                       </div>

                                                                                                                                                                                                                                                                                                                                                               <!-- Box 3: Custom Spacing -->
                                                                                                                                                                                                                                                                                                                                                                       <div class="box-custom">
                                                                                                                                                                                                                                                                                                                                                                                   <h2>Box 3: Custom Spacing Card</h2>
                                                                                                                                                                                                                                                                                                                                                                                               <p>Demonstrates asymmetric padding (30px vertical, 40px horizontal), a dashed border, and centering margins.</p>
                                                                                                                                                                                                                                                                                                                                                                                                       </div>

                                                                                                                                                                                                                                                                                                                                                                                                           </main>

                                                                                                                                                                                                                                                                                                                                                                                                           </body>
                                                                                                                                                                                                                                                                                                                                                                                                           </html>

                                                                                                                                                                                                                                                                                                                                                                                                           ```

                                                                                                                                                                                                                                                                                                                                                                                                           ---

                                                                                                                                                                                                                                                                                                                                                                                                           ### Instructions for DevTools Inspection & Screenshot Annotation (Steps 5 & 6)

                                                                                                                                                                                                                                                                                                                                                                                                           1. **Open Chrome DevTools:**
                                                                                                                                                                                                                                                                                                                                                                                                           * Open `index.html` in Google Chrome.
                                                                                                                                                                                                                                                                                                                                                                                                           * Right-click anywhere on **Box 1** or **Box 2** and select **Inspect** (or press `F12` / `Ctrl + Shift + I`).


                                                                                                                                                                                                                                                                                                                                                                                                           2. **Locate the Box Model Diagram:**
                                                                                                                                                                                                                                                                                                                                                                                                           * In the DevTools panel on the right, make sure the **Elements** tab is active and select the **Styles** sub-tab.
                                                                                                                                                                                                                                                                                                                                                                                                           * Scroll down to the bottom of the **Styles** pane to view the interactive **Box Model diagram** (showing Content, Padding, Border, and Margin concentric boxes).


                                                                                                                                                                                                                                                                                                                                                                                                           3. **Annotating Your Screenshot (Step 6):**
                                                                                                                                                                                                                                                                                                                                                                                                           Take a screenshot of your browser window alongside the DevTools box model diagram and label the four main layers:
                                                                                                                                                                                                                                                                                                                                                                                                           * **Content:** The innermost blue area where text and headings are rendered.
                                                                                                                                                                                                                                                                                                                                                                                                           * **Padding:** The green area surrounding the content representing internal spacing.
                                                                                                                                                                                                                                                                                                                                                                                                           * **Border:** The yellow/orange line surrounding the padding representing the element's outer edge.
                                                                                                                                                                                                                                                                                                                                                                                                           * **Margin:** The outermost orange/grey space separating the element from surrounding elements.