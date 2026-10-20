### Part 1: Before-and-After Code Comparison

#### ❌ Before: Buggy HTML File (`buggy.html`)

This sample code contains intentional mistakes:

* Missing closing tags (e.g., `</p>`, `</div>`).
* Incorrect tag nesting (e.g., placing a `<div>` inside a `<p>` incorrectly or overlapping tags).
* Missing required attributes (e.g., missing `alt` attribute on an image or missing `charset`).

```html
<!DOCTYPE html>
<html>
<head>
    <title>Buggy Page
    <!-- Bug 1: Missing closing title tag and missing meta charset -->
    <body>
        <div id="main">
                <h1>Debugging Assignment
                        <!-- Bug 2: Missing closing h1 tag -->
                                <p>This paragraph is never closed properly.
                                        <div>
                                                    <img src="profile.jpg"> <!-- Bug 3: Missing alt attribute -->
                                                            </div>
                                                                </div>
                                                                <!-- Bug 4: Missing closing body and html tags -->

                                                                ```

                                                                #### ✔️ After: Fixed, Validated, and Properly Indented HTML File (`index.html`)

                                                                This corrected version fixes all nesting issues, closes every tag properly, and includes all necessary attributes for HTML5 validation.

                                                                ```html
                                                                <!DOCTYPE html>
                                                                <html lang="en">
                                                                <head>
                                                                    <meta charset="UTF-8">
                                                                        <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                                                            <title>Debugging Assignment - Fixed</title>
                                                                            </head>
                                                                            <body>
                                                                                <div id="main">
                                                                                        <h1>Debugging Assignment</h1>
                                                                                                <p>This paragraph is now properly closed.</p>
                                                                                                        <div class="image-container">
                                                                                                                    <img src="profile.jpg" alt="Profile Picture of Student">
                                                                                                                            </div>
                                                                                                                                </div>
                                                                                                                                </body>
                                                                                                                                </html>

                                                                                                                                ```

                                                                                                                                ---

                                                                                                                                ### Part 2: Summary of Errors Identified & Fixed

                                                                                                                                1. **Missing Closing Tags:** Added missing `</title>`, `</h1>`, `</p>`, `</body>`, and `</html>` tags to ensure the document tree closes correctly.
                                                                                                                                2. **Incorrect/Overlapping Nesting:** Ensured elements are strictly hierarchical (e.g., child elements closed inside their parent containers rather than overlapping).
                                                                                                                                3. **Missing Attributes:** Added the `alt` attribute to the `<img>` tag (required for accessibility/validation) and included `<meta charset="UTF-8">` and `lang="en"` in the `<head>`/`<html>` tags.
                                                                                                                                4. **Indentation & Formatting:** Cleaned up the code with consistent indentation for readability.

                                                                                                                                ---

                                                                                                                                ### Part 3: Steps to Complete the DevTools & Validation Requirement

                                                                                                                                To finish the practical verification steps for your submission:

                                                                                                                                1. **Inspect with DevTools:** Open your fixed HTML file in Chrome, press `F12` (or right-click -> **Inspect**), and look at the **Elements** panel. Notice how the browser DOM successfully parses the clean markup.
                                                                                                                                2. **Validator Check:** Copy the fixed HTML code, paste it into the official **[W3C HTML Validator Service](https://validator.w3.org/)** (using the "Direct Input" tab), and click **Check** to verify that it passes with 0 errors or warnings.

                                                                                                                                ---

                                                                                                                                ### What to Submit

                                                                                                                                1. The **Before-and-After code** shown above.
                                                                                                                                2. A **screenshot of your fixed webpage** running in the browser (or your browser DevTools Elements panel showing the clean DOM tree).