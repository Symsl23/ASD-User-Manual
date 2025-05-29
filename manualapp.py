import streamlit as st
import pandas as pd

def main():
    # Set the page configuration to 'centered'
    st.set_page_config(
        page_title="App Guide & Manual",
        layout="centered"  # This will center the content by default
    )

    # Inject custom CSS to set the max-width for the main content area
    # This targets the '.main' div which contains your app's content
    st.markdown(
        """
        <style>
        .appview-container .main .block-container {
            max-width: 740px;
            padding-left: 3rem; # Adjust padding if needed, default is usually fine
            padding-right: 1rem; # Adjust padding if needed
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Initialize session state for navigation if not already present
    if 'active_page_category' not in st.session_state:
        st.session_state.active_page_category = None
    if 'active_sub_page' not in st.session_state:
        st.session_state.active_sub_page = None
    if 'active_installation_sub_category' not in st.session_state: # New state for sub-category within Installation
        st.session_state.active_installation_sub_category = None


    # Define main page categories (Installation Guide, User Manual, About)
    user_manual_options = {
        "For Students": "1. For Students",
        "For Admins": "2. For Admins",
    }

    about_options = {
        "App Info": "App Information",
        "Contact": "Contact & Support"
    }

    # --- Sidebar Navigation ---
    st.sidebar.title("Attendance System with Auto Report Guide & Manual")

    # Installation Guide Dropdown (Main parent dropdown)
    with st.sidebar.expander("🛠️ Installation Guide"):
        if st.button("General Requirement", key="install_General Requirement_btn"):
            st.session_state.active_page_category = "Installation Guide"
            st.session_state.active_installation_sub_category = "General Requirement"
            st.session_state.active_sub_page = None # Reset sub_page for other categories

        if st.button("Required Library", key="install_requiredlibraries_btn"):
            st.session_state.active_page_category = "Installation Guide"
            st.session_state.active_installation_sub_category = "Required Library"
            st.session_state.active_sub_page = None # Reset sub_page for other categories

    # User Manual Dropdown
    with st.sidebar.expander("📖 User Manual"):
        for key, display_name in user_manual_options.items():
            if st.button(display_name, key=f"manual_{key}"):
                st.session_state.active_page_category = "User Manual"
                st.session_state.active_sub_page = key
                st.session_state.active_installation_sub_category = None # Reset for other categories

    # About Dropdown
    with st.sidebar.expander("ℹ️ About"):
        for key, display_name in about_options.items():
            if st.button(display_name, key=f"about_{key}"):
                st.session_state.active_page_category = "About"
                st.session_state.active_sub_page = key
                st.session_state.active_installation_sub_category = None # Reset for other categories

    # --- Display Content ---
    # With layout="centered" and the CSS, you don't need st.columns([1, 3, 1]) for centering.
    # The content will automatically be centered and constrained by the max-width.
    
    if st.session_state.active_page_category == "Installation Guide":
        show_installation_guide(st.session_state.active_installation_sub_category)
    elif st.session_state.active_page_category == "User Manual":
        show_user_manual(st.session_state.active_sub_page)
    elif st.session_state.active_page_category == "About":
        show_about_page(st.session_state.active_sub_page)
    else:
        # Default view or initial message
        st.info("Welcome to the App Guide & Manual! Please select a section from the sidebar to begin.")


def show_installation_guide(installation_sub_category=None):
    st.title("🛠️ Installation Guide")
    st.markdown("---")

    if installation_sub_category == "General Requirement":
        st.header("1. Prerequisites")
        st.markdown("""
        Before you begin, ensure you have the following installed:
        * **Python:** Version 3.7 or higher but the highly recommended version is Pyhton 3.11 because the development of this project are using the 3.11. You can download it from [python.org](https://www.python.org/downloads/).
        * **pip:** Python's package installer (usually comes with Python).
        * **Git (Optional but Recommended):** For cloning the repository. Download from [git-scm.com](https://git-scm.com/downloads).
        """)
        st.markdown("---")

        st.header("2. Setting up a Virtual Environment (Recommended)")
        st.markdown("""
        It's highly recommended to use a virtual environment to manage project dependencies.

        **On Windows:**
        ```bash
        python -m venv venv
        .\\venv\\Scripts\\activate
        ```

        **On macOS/Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
        You should see `(venv)` at the beginning of your terminal prompt.
        """)
        st.markdown("---")

        st.header("3. Installing the Application")
        st.subheader("Option A: Using pip (if your app is on PyPI)")
        st.markdown("""
        If your application is published on the Python Package Index (PyPI), users can install it directly using pip:
        ```bash
        pip install your-app-name
        ```
        *(Replace `your-app-name` with the actual name of your package on PyPI.)*
        """)

        st.subheader("Option B: From Source Code (e.g., GitHub)")
        st.markdown("""
        1.  **Clone the repository (if applicable):**
            ```bash
            git clone <your-repository-url>
            cd <your-repository-directory>
            ```
            *(Replace `<your-repository-url>` and `<your-repository-directory>` with your actual repository details.)*

        2.  **Install dependencies:**
            Navigate to the project directory (where `requirements.txt` or `setup.py` is located).
            ```bash
            pip install -r requirements.txt
            ```
            *(Ensure you have a `requirements.txt` file listing all necessary packages, including `streamlit`.)*
        """)
        st.markdown("---")

        st.header("4. Running the Application")
        st.markdown("""
        Once the installation is complete:
        1.  Navigate to the main application directory in your terminal (if you cloned from source).
        2.  Run the Streamlit app using the following command:
            ```bash
            streamlit run your_app_file.py
            ```
            *(Replace `your_app_file.py` with the actual name of your main Streamlit Python file.)*

        3.  Your default web browser should automatically open to the application's URL (usually `http://localhost:8501`).
        """)
        st.markdown("---")

        st.header("5. Troubleshooting (Example)")
        st.markdown("""
        * **ModuleNotFoundError:** If you see an error like `ModuleNotFoundError: No module named 'some_package'`, it means a required package is missing.
            * **Solution:** Activate your virtual environment and install the missing package: `pip install some_package`. Then, try running the app again.
        * **Streamlit command not found:**
            * **Solution:** Ensure Streamlit is installed correctly and that its installation directory is in your system's PATH. If using a virtual environment, make sure it's activated.
        * *(Add more common issues and solutions specific to your app here.)*
        """)


    elif installation_sub_category == "Required Library":
        st.header("Required Python Library")
        st.subheader("1. Streamlit")
        st.write("`Streamlit` – Used to create the web-based dashboard and user interface")
        st.code("""pip install streamlit""")

        st.markdown("---")

        st.subheader("2. Face Recognition")
        st.write("`face_recognition` – Used to detect and recognize faces from webcam or image")
        st.code("""pip install face_recognition""") # Corrected: It was 'streamlit' again

        st.write("🔧 Requires dependencies:")
        st.code("""pip install cmake
pip install dlib""")

        st.subheader("If you're encountering issues installing the face_recognition library, particularly problems related to dlib compilation, you can try installing a precompiled dlib wheel file. This often bypasses the need for a C++ compiler and CMake.")
        st.write("Here's how to do it:")
        st.markdown("""
        1.  Go to the Unofficial Dlib Precompiled Wheels Repository:     
        Open your web browser and navigate to this link:     
        https://github.com/Cfuhfsgh/Dlib-library-Installation
        2.  Identify Your Python Version:   
        You need to know your exact Python version. Open your terminal or command prompt and run:   
            ```bash
            python --version
            ``` 
            This will output something like `Python 3.8.10` or `Python 3.9.7`. Pay close attention to the minor version (e.g., `3.8`, `3.9`, `3.10`, etc.).

        3.  Download the Correct `dlib` Wheel File:   
        On the GitHub page, you'll see a list of `.whl` files. These are precompiled Python packages. 
            - Look for a file that matches your Python version and your operating system (64-bit).   
            - For example:   
                - If you have Python 3.9 and a 64-bit Windows system, you might look for `dlib-19.xx.x-cp39-cp39m-win_amd64.whl`.
                - If you have Python 3.11 and a 64-bit Windows system, you might look for `dlib-19.xx.x-cp311-cp311m-win_amd64.whl`.   
                - Click on the `.whl` file that matches your system.   
                - On the next page, click the "Download" button (usually a down-arrow icon) to save the file to your computer. Remember where you save it (e.g., your "Downloads" folder).   

        4. Install the Downloaded `dlib` Wheel File:     
        Find your Wheel File on your directory for example "Download" and then copy the name file. Use `pip` to install the `.whl` file. Replace `dlib-19.xx.x-cpXX-cpXXm-win_amd64.whl` with the actual name of the file you downloaded in your terminal:     
            ```bash
            pip install dlib-19.xx.x-cpXX-cpXXm-win_amd64.whl   
            ``` 
        (Example: `pip install dlib-19.22.99-cp39-cp39-win_amd64.whl`)     

        5. Install `face_recognition`:   
        After `dlib` is successfully installed, you can now reinstall `face_recognition`:   
            ```bash 
            pip install face_recognition     
            ``` 
        This approach should help resolve common dlib installation errors by providing a precompiled version, avoiding the need for local compilation.
        """)

        st.markdown("---")

        st.subheader("3. Pandas")
        st.write("`pandas` – Used to handle and organize tabular data (like attendance records)")
        st.code("""pip install pandas""")

        st.markdown("---")

        st.subheader("4. Pickle")
        st.write("`pickle – (Built-in)` Used to save/load face encodings into a file")
        st.write("✅ No installation needed (built into Python)")

        st.markdown("---")

        st.subheader("5. io")
        st.write("`io – (Built-in)` Used to handle in-memory file objects (for uploads, downloads)")
        st.write("✅ No installation needed (built into Python)")

        st.markdown("---")

        st.subheader("6. DateTime")
        st.write("`datetime – (Built-in)` Used to manage date and time (e.g. attendance timestamps)")
        st.write("✅ No installation needed (built into Python)")

        st.markdown("---")

        st.subheader("7. gspread")
        st.write("`gspread` – Connects to and edits Google Sheets from your app")
        st.code("""pip install gspread""")

        st.markdown("---")

        st.subheader("8. Plotly")
        st.write("`plotly` – Used for interactive charts (attendance visualizations, statistics)")
        st.code("""pip install plotly""")

        st.markdown("---")

        st.subheader("9. Google Auth")
        st.write("`google-auth` – Handles authentication to Google services")
        st.code("""pip install google-auth""")

        st.markdown("---")

        st.subheader("10. Google Auth Oauthlib")
        st.write("`google-auth-oauthlib` – Helps with Google OAuth2 authentication flows")
        st.code("""pip install google-auth-oauthlib""")

        st.markdown("---")

        st.subheader("11. Google API Python Client")
        st.write("`google-api-python-client` – Sends data to Google Sheets and uploads files to Google Drive")
        st.code("""pip install google-api-python-client""")

        st.markdown("---")

        st.subheader("12. os")
        st.write("`os – (Built-in)` Interacts with the file system (like checking files or paths)")
        st.write("✅ No installation needed (built into Python)")

        st.markdown("---")

        st.subheader("13. Seaborn")
        st.write("`seaborn` – Creates beautiful statistical charts (optional for data trends)")
        st.code("""pip install seaborn""")

        st.markdown("---")

        st.subheader("14. MatPlotLib")
        st.write("`matplotlib` – Used for plotting graphs and heatmaps (used by Seaborn too)")
        st.code("""pip install matplotlib""")

        st.markdown("---")

        st.subheader("15. Base64")
        st.write("`base64` – (Built-in) Used to encode images for display or upload")
        st.write("✅ No installation needed (built into Python)")

        st.markdown("---")

        st.subheader("16. MatPlotLib Colors")
        st.write("`matplotlib.colors` – Provides color maps for heatmaps and visualizations")
        st.write("✅ Already part of `matplotlib`")

        st.markdown("---")


    else:
        st.info("Please select either 'General Requirement' or 'Required Library' from the 'Installation Guide' dropdown.")


def show_user_manual(sub_page=None):
    st.title("📖 User Manual")
    st.markdown("---")
    
    if sub_page == "For Students":
        st.header("🧑‍🎓 For Students")
        st.subheader("1. 🧑‍🎓 Register Face")            
        st.markdown("""
        Steps:

        i) Go to the "Register Face" tab.
        """)
        st.image("images/register face.jpg", width=700)

        st.markdown("""
        ii) Fill in:
        - Full Name
        - Student ID
        - Email
        - Phone Number
        """)
        st.image("images/fill in.jpg", width=700)

        st.markdown("""
        iii) Capture your face using the camera.
        """)
        st.image("images/capture face.jpg", width=700)

        st.markdown("""iv) Click "Register".""")



        st.markdown("""         
        ✅ If registration is successful, your face and info will be saved.
        """)
        #st.image("")

        st.markdown("""
        ⚠️ Errors:

        - Invalid email or phone number.
        - No face detected.
        - Missing fields.
        """)
        #st.image("")

        st.markdown("---")

        st.subheader("2. 📝 Submit Attendance")
        st.markdown("""
        Steps:

        i) Go to the "Submit Attendance" tab.
        """)
        st.image("images/submit attendance.jpg", width=700)

        st.markdown("""
        ii) Select your class from the dropdown.
        """)
        st.image("images/select class.jpg", width=700)

        st.markdown("""
        iii) Capture your face using the camera.
        """)
        st.image("images/capture face submit.jpg", width=700)
            
        st.markdown("""
        ✅ If your face is recognized:

        - Attendance will be recorded.
        - Image will be uploaded to Google Drive.
        - Your name, student ID, class, and timestamp will be saved in Google Sheets.
        """)
        #st.image("")
            
        st.markdown("""
        ❌ If not recognized, you’ll see an error message.
        """)
        #st.image("")

        st.markdown("---")

        st.subheader("3. 📈 View Student Performance")
        st.markdown("""
        Steps:

        i) Go to the "Student Performance" tab.
        """)
        st.image("images/student performance.jpg", width=700)
            
        st.markdown("""
        ii) Select your class.
        """)
        st.image("images/select class performance.jpg", width=700)
            
        st.markdown("""
        iii) Choose your name + student ID.
        """)
        st.image("images/select student.jpg", width=700)

        st.markdown("""
        iv) View:

        - Total days attended.   
        - Attendance rate (%).   
        - Class average comparison.   
        - Attendance over time (line chart).
        """)

        st.markdown("""
        v) Download your CSV attendance report.

        ⚠️ If attendance is < 75%, you'll see a warning.
        """)
        st.image("images/view performance.jpg", width=700)

    elif sub_page == "For Admins":
        st.header("2. 🛠️ For Admins")
        st.subheader("Login:")
        st.markdown("""
        1. Go to the "Admin Panel" tab.
        """)
        st.image("images/admin panel.jpg", width=700)

        st.markdown("""
        2. Enter the admin code: admin123.
        """)
        st.image("images/admin login.jpg", width=700)

        st.markdown("---")

        st.subheader("🔧 Admin Features")
        st.markdown("""
        ➕ Add New Class
        - Type a new class name.
        - Click "Add Class" to create a Drive folder and track attendance.
        """)
        st.image("images/add class.jpg", width=700)
        
        st.markdown("""
        ➖ Remove Class
        - Select an existing class to remove from the system.
        - WARNING: This action cannot be undone.
        """)
        st.image("images/remove class.jpg", width=700)

        st.markdown("---")

        st.subheader("📊 Attendance Dashboard")
        st.markdown("""
        a) Select a class.

        b) Pick a date range.
        """)
        st.image("images/attendance dashboard.jpg", width=700)
        
        st.markdown("""
        c) View:

        - Average attendance.
        - Low attendance students.
        - Top 3 attendees.
        - Attendance pie chart.
        """)
        st.image("images/attendance dashboard2.jpg", width=700)
        st.image("images/attendance dashboard3.jpg", width=700)

        st.markdown("---")

        st.subheader("📥 Download Attendance Data")
        st.markdown("""
        - Select a class.
        - Choose a date range.
        - Click "Download CSV" to export data.
        """)
        st.image("images/download attendance data.jpg", width=700)

        st.markdown("---")

        st.subheader("💾 Data Storage")

        data_storage = {
        "Component": [
        "Registered Faces",
        "Class Folder IDs",
        "Attendance Records",
        "Face Images"
        ],
        "Location": [
        "known_faces.pkl (local file)",
        "class_folders.pkl",
        "Google Sheets",
        "Google Drive (per class folder)"
        ]
        }
        df_storage = pd.DataFrame(data_storage)
        
        st.table(df_storage)

    else:
        st.info("Please select a specific section from the 'User Manual' dropdown to view its content.")


def show_about_page(sub_page=None):
    st.title("ℹ️ About This Application")
    st.markdown("---")

    if sub_page == "App Info":
        st.markdown("""
        **[Your App Name]**
        Version: [Your App Version, e.g., 1.0.0]
        Last Updated: [Date of Last Update, e.g., May 2024]

        **Developed by:**
        [Your Name / Your Team's Name]

        **Contact / Support:**
        If you encounter any issues or have questions, please [Provide contact method, e.g., 'email support@example.com' or 'open an issue on our GitHub repository: <link-to-github-issues>'].

        **Purpose:**
        [Reiterate the main purpose of your application in a sentence or two.]

        **Technology Stack:**
        * Python
        * Streamlit
        * [List other key libraries or technologies used, e.g., Pandas, NumPy, Scikit-learn, etc.]
        """)
    elif sub_page == "Contact":
        st.header("Contact / Support")
        st.markdown("""
        If you encounter any issues or have questions, please [Provide contact method, e.g., 'email support@example.com' or 'open an issue on our GitHub repository: <link-to-github-issues>'].
        """)
    else:
        st.info("Please select a specific section from the 'About' dropdown to view its content.")

    st.markdown("---")
    st.markdown("""
    *[Optional: Add a license section if your app is open source, e.g., 'This application is licensed under the MIT License.']*
    """)


if __name__ == "__main__":
    main()