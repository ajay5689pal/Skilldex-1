// Initialize Blockly workspace
const workspace = Blockly.inject('blocklyArea', {
    toolbox: document.getElementById('toolbox'),
    scrollbars: true,
    trashcan: true,
    theme: Blockly.Themes.Classic
  });
  
  // Function to generate Python code from blocks
  function generatePythonCode() {
    const code = Blockly.Python.workspaceToCode(workspace);
    document.getElementById('pythonCode').innerText = code;
  }
  
  // Function to execute the Python code
  function runPythonCode() {
    const code = Blockly.Python.workspaceToCode(workspace);
    
    if (code.trim()) {
      // Example: Use Pyodide for running Python in the browser
      pyodide.runPython(code)
        .then(result => {
          document.getElementById('output').innerText = result;
        })
        .catch(err => {
          document.getElementById('output').innerText = `Error: ${err}`;
        });
    } else {
      alert("Please build some code first!");
    }
  }
  
  // Event listeners for buttons
  document.getElementById('generateBtn').addEventListener('click', generatePythonCode);
  document.getElementById('runBtn').addEventListener('click', runPythonCode);
  
  // Example: Setup Pyodide for Python execution in browser
  async function loadPyodide() {
    window.pyodide = await loadPyodide();
    console.log("Pyodide loaded");
  }
  
  // Load Pyodide (for running Python in the browser)
  loadPyodide();
  