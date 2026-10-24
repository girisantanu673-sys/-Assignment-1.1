**Assignment 7.1 — Responsive Navigation Bar**.

The project is structured into two clean files:

1. **`style.css`** (External stylesheet implementing Flexbox, `justify-content`, `align-items`, and navigation link styling)
2. **`index.html`** (Sample webpage featuring the horizontal navigation bar with a logo, links, and action button)

---

### File 1: `style.css` (External Stylesheet)

```css
/* ==========================================================================
   Assignment 7.1 — Responsive Navigation Bar Stylesheet
      Author: Shalini Gangwar
         ========================================================================== */

         :root {
             --primary: #2563eb;
                 --primary-hover: #1d4ed8;
                     --bg-color: #f8fafc;
                         --surface: #ffffff;
                             --text-main: #334155;
                                 --border-color: #e2e8f0;
                                 }

                                 * {
                                     box-sizing: border-box;
                                         margin: 0;
                                             padding: 0;
                                             }

                                             body {
                                                 font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                                                     background-color: var(--bg-color);
                                                         color: var(--text-main);
                                                             line-height: 1.6;
                                                             }

                                                             /* 1. Header Container */
                                                             header {
                                                                 background-color: var(--surface);
                                                                     border-bottom: 1px solid var(--border-color);
                                                                         position: sticky;
                                                                             top: 0;
                                                                                 z-index: 1000;
                                                                                     box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
                                                                                     }

                                                                                     /* 2. Flexbox Container Layout */
                                                                                     .nav-container {
                                                                                         display: flex;                  /* Step 2: Apply display: flex */
                                                                                             justify-content: space-between; /* Step 3: Space items (Logo on left, Links on right) */
                                                                                                 align-items: center;            /* Step 4: Vertically center all items */
                                                                                                     max-width: 1000px;
                                                                                                         margin: 0 auto;
                                                                                                             padding: 15px 20px;
                                                                                                             }

                                                                                                             /* Logo Styling */
                                                                                                             .logo {
                                                                                                                 font-size: 1.3rem;
                                                                                                                     font-weight: 700;
                                                                                                                         color: var(--primary);
                                                                                                                             text-decoration: none;
                                                                                                                             }

                                                                                                                             /* 5. Navigation Links List */
                                                                                                                             .nav-links {
                                                                                                                                 display: flex;                  /* Nested flex container for links */
                                                                                                                                     list-style: none;
                                                                                                                                         gap: 24px;                      /* Spacing between link items */
                                                                                                                                             align-items: center;
                                                                                                                                             }

                                                                                                                                             .nav-links a {
                                                                                                                                                 text-decoration: none;
                                                                                                                                                     color: var(--text-main);
                                                                                                                                                         font-weight: 600;
                                                                                                                                                             font-size: 0.95rem;
                                                                                                                                                                 transition: color 0.2s ease;
                                                                                                                                                                 }

                                                                                                                                                                 .nav-links a:hover {
                                                                                                                                                                     color: var(--primary);
                                                                                                                                                                     }

                                                                                                                                                                     /* 5. Action Button Styling */
                                                                                                                                                                     .nav-btn {
                                                                                                                                                                         background-color: var(--primary);
                                                                                                                                                                             color: #ffffff;
                                                                                                                                                                                 padding: 8px 16px;
                                                                                                                                                                                     border-radius: 6px;
                                                                                                                                                                                         text-decoration: none;
                                                                                                                                                                                             font-weight: 600;
                                                                                                                                                                                                 transition: background-color 0.2s ease;
                                                                                                                                                                                                 }

                                                                                                                                                                                                 .nav-btn:hover {
                                                                                                                                                                                                     background-color: var(--primary-hover);
                                                                                                                                                                                                         color: #ffffff;
                                                                                                                                                                                                         }

                                                                                                                                                                                                         /* Page Content Preview */
                                                                                                                                                                                                         .main-content {
                                                                                                                                                                                                             max-width: 1000px;
                                                                                                                                                                                                                 margin: 40px auto;
                                                                                                                                                                                                                     padding: 0 20px;
                                                                                                                                                                                                                     }

                                                                                                                                                                                                                     .card {
                                                                                                                                                                                                                         background: var(--surface);
                                                                                                                                                                                                                             padding: 35px;
                                                                                                                                                                                                                                 border-radius: 12px;
                                                                                                                                                                                                                                     border: 1px solid var(--border-color);
                                                                                                                                                                                                                                         box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.04);
                                                                                                                                                                                                                                         }

                                                                                                                                                                                                                                         .card h2 {
                                                                                                                                                                                                                                             color: #0f172a;
                                                                                                                                                                                                                                                 font-size: 1.5rem;
                                                                                                                                                                                                                                                     margin-bottom: 12px;
                                                                                                                                                                                                                                                     }

                                                                                                                                                                                                                                                     .card p {
                                                                                                                                                                                                                                                         color: #64748b;
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
                                                                                                                                                                                                                                                                     <title>Responsive Navigation Bar - Shalini Gangwar</title>
                                                                                                                                                                                                                                                                         <meta name="description" content="Assignment 7.1 horizontal navigation bar built using Flexbox, justify-content, and align-items.">
                                                                                                                                                                                                                                                                             <link rel="icon" type="image/png" href="favicon.png">
                                                                                                                                                                                                                                                                                 <link rel="stylesheet" href="style.css">
                                                                                                                                                                                                                                                                                 </head>
                                                                                                                                                                                                                                                                                 <body>

                                                                                                                                                                                                                                                                                     <!-- 1. Header Containing Logo and Navigation Links -->
                                                                                                                                                                                                                                                                                         <header>
                                                                                                                                                                                                                                                                                                 <div class="nav-container">
                                                                                                                                                                                                                                                                                                             <!-- Brand Logo -->
                                                                                                                                                                                                                                                                                                                         <a href="#" class="logo">Shalini Gangwar</a>

                                                                                                                                                                                                                                                                                                                                     <!-- Navigation Links & Action Button -->
                                                                                                                                                                                                                                                                                                                                                 <ul class="nav-links">
                                                                                                                                                                                                                                                                                                                                                                 <li><a href="#">Home</a></li>
                                                                                                                                                                                                                                                                                                                                                                                 <li><a href="#">About</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                 <li><a href="#">Projects</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                 <li><a href="#">Contact</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                 <li><a href="#" class="nav-btn">Get Started</a></li>
                                                                                                                                                                                                                                                                                                                                                                                                                                             </ul>
                                                                                                                                                                                                                                                                                                                                                                                                                                                     </div>
                                                                                                                                                                                                                                                                                                                                                                                                                                                         </header>

                                                                                                                                                                                                                                                                                                                                                                                                                                                             <!-- Sample Webpage Content to Test Layout (Step 6) -->
                                                                                                                                                                                                                                                                                                                                                                                                                                                                 <main class="main-content">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                         <section class="card">
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     <h2>Assignment 7.1 — Flexbox Navigation Bar</h2>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 <p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 Resize your browser window (Step 6) to test how the Flexbox layout responds. The container utilizes <code>display: flex</code>, <code>justify-content: space-between</code>, and <code>align-items: center</code> to maintain clean vertical and horizontal alignment across screen sizes.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             </p>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     </section>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         </main>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         </body>
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         </html>

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ```

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ---

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         ### Step-by-Step Submission Summary

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         1. **Save Files:** Save `style.css` and `index.html` inside your assignment folder.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         2. **Review Flexbox Properties Implemented:**
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         * **`display: flex`:** Turns `.nav-container` and `.nav-links` into flexible box containers.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         * **`justify-content: space-between`:** Pins the brand logo to the left and pushes the navigation links group to the right.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         * **`align-items: center`:** Centers the logo, text links, and button vertically inside the header.


                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         3. **Browser Testing (Step 6):** Open `index.html` in Google Chrome and resize the window to verify that the navigation bar remains clean and aligned.