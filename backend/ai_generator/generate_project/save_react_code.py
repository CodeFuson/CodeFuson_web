import os
import subprocess


def save_generated_react_code(generated_code, folder):
    frontend_path = os.path.join(folder, 'frontend')

    # Ensure the frontend directory exists
    os.makedirs(frontend_path, exist_ok=True)

    # Create src directory if it doesn't exist
    src_path = os.path.join(frontend_path, 'src')
    os.makedirs(src_path, exist_ok=True)

    # Save the Home.js and Home.css files
    try:
        # Save the Home.js file
        with open(os.path.join(src_path, 'Home.js'), 'w', encoding='utf-8') as js_file:
            js_file.write(generated_code['js'])

        # Save the Home.css file
        with open(os.path.join(src_path, 'Home.css'), 'w', encoding='utf-8') as css_file:
            css_file.write(generated_code['css'])

        # Save and update App.js to use Home.js
        with open(os.path.join(src_path, 'App.js'), 'w', encoding='utf-8') as app_file:
            app_file.write("""
import React from 'react';
import './App.css';
import './Home.css'; // import the generated Home.css
import Home from './Home'; // import the generated Home.js

function App() {
  return (
    <div className="App">
      <Home /> {/* Use the Home component */}
    </div>
  );
}

export default App;
            """)


        # Ensure correct permissions
        subprocess.run(f"chmod -R 755 {frontend_path}", shell=True, check=True)

    except Exception as e:
        print(f"Error saving React code: {e}")
        raise e