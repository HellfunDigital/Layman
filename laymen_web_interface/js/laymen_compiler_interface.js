```javascript
// Importing necessary modules
import { compileLaymenCode, parseLaymenCode } from '../laymen_compiler/laymen_compiler.js';
import { DebugInfoSchema } from '../laymen_compiler/laymen_debugger.js';

// DOM Elements
const laymenCodeInput = document.getElementById('laymenCodeInput');
const compileButton = document.getElementById('compileButton');
const debugButton = document.getElementById('debugButton');

// Event Listener for Compile Button
compileButton.addEventListener('click', () => {
    const laymenCode = laymenCodeInput.value;
    const parsedCode = parseLaymenCode(laymenCode);
    const compiledCode = compileLaymenCode(parsedCode);
    if (compiledCode.error) {
        alert(`Compile Error: ${compiledCode.error}`);
    } else {
        alert('Compile Success');
    }
});

// Event Listener for Debug Button
debugButton.addEventListener('click', () => {
    const laymenCode = laymenCodeInput.value;
    const parsedCode = parseLaymenCode(laymenCode);
    const debugInfo = DebugInfoSchema(parsedCode);
    if (debugInfo.error) {
        alert(`Debug Error: ${debugInfo.error}`);
    } else {
        alert(`Debug Info: ${debugInfo.message}`);
    }
});
```