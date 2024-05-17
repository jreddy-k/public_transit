Prerequisites:

Python 3.11: Download and install Python 3.11 from the official website (https://www.python.org/downloads/windows/ or https://www.python.org/downloads/macos/ for macOS). Verify the installation by opening a terminal and running python3.11 --version.
Virtual Environment (Recommended):

Highly recommended: Using a virtual environment isolates your project's dependencies from system-wide installations, preventing conflicts.
Create a virtual environment using python3.11 -m venv myenv (replace myenv with your desired name).
Activate the virtual environment:
Windows: myenv\Scripts\activate.bat
macOS/Linux: source myenv/bin/activate
Optional (without virtual environment): If you're not using a virtual environment, ensure you don't have conflicting Python versions or dependencies installed system-wide.
Installation:

Clone or download the repository: Clone this repository using Git or download the ZIP file.

Install dependencies: Navigate to the project directory and install required packages using pip:

Bash
pip install -r requirements.txt
Use code with caution.
content_copy
This will install all the libraries listed in requirements.txt.

Running the Development Server:

Start the development server: With the virtual environment activated (if using one), run the following command to start the Django development server:

Bash
python manage.py runserver
Use code with caution.
content_copy
By default, the server will listen on port 8000. You can access your Django application at http://localhost:8000/ in your web browser.
