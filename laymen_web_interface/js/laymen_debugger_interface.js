```javascript
// Importing necessary modules
import { debugLaymenCode } from '../laymen_compiler/laymen_debugger.js';

// DOM Elements
const laymenCodeInput = document.getElementById('laymenCodeInput');
const debugButton = document.getElementById('debugButton');
const debugInfoDisplay = document.getElementById('debugInfoDisplay');

// Function to display debug information
function displayDebugInfo(debugInfo) {
    debugInfoDisplay.textContent = JSON.stringify(debugInfo, null, 2);
}

// Event Listener for Debug Button
debugButton.addEventListener('click', () => {
    const laymenCode = laymenCodeInput.value;
    const debugInfo = debugLaymenCode(laymenCode);
    displayDebugInfo(debugInfo);
});
```