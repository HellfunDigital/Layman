```javascript
// Importing necessary dependencies
import { TutorialContentSchema } from '../laymen_compiler/laymen_tutorial_generator.py';

// DOM Element
const tutorialContentDisplay = document.getElementById('tutorialContentDisplay');

// Function to display tutorial content
function displayTutorialContent(tutorialContent) {
    tutorialContentDisplay.innerHTML = tutorialContent;
}

// Event Listener for tutorial update
window.addEventListener('tutorialUpdate', (event) => {
    const tutorialContent = event.detail;
    if (TutorialContentSchema.validate(tutorialContent)) {
        displayTutorialContent(tutorialContent);
    } else {
        console.error('Invalid tutorial content received');
    }
});
```