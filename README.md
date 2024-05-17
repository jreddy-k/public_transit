Python 3.11

Download and install Python 3.11 from the official website:
Windows: https://www.python.org/downloads/windows/
macOS: https://www.python.org/downloads/macos/
Verify the installation by opening a terminal and running:
Bash
python3.11 --version
Use code with caution.
content_copy
Virtual Environment (Highly Recommended)

Using a virtual environment isolates your project's dependencies from system-wide installations, preventing conflicts.

Create a virtual environment:

Bash
python3.11 -m venv myenv  # Replace "myenv" with your desired name
Use code with caution.
content_copy
Activate the virtual environment:

Windows: myenv\Scripts\activate.bat
macOS/Linux: source myenv/bin/activate
Optional (Without Virtual Environment)

If you're not using a virtual environment, ensure you don't have conflicting Python versions or dependencies installed system-wide.

Installation
Clone or Download the Repository: Clone this repository using Git or download the ZIP file.

Install Dependencies: Navigate to the project directory and install required packages using pip:

Bash
pip install -r requirements.txt
Use code with caution.
content_copy
This will install all the libraries listed in requirements.txt.

Running the Development Server
Start the Development Server: With the virtual environment activated (if using one), run the following command to start the Django development server:

Bash
python manage.py runserver
Use code with caution.
content_copy
By default, the server will listen on port 8000. You can access your Django application at http://localhost:8000/ in your web browser.
