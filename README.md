# Hospital Management System

A command-line Python application designed to streamline hospital operations. This system handles administrative tasks, staff record management (doctors, nurses, and other workers), and patient admission/discharge processes using a MySQL backend.

## 📋 Features

### Authentication
* **User Registration:** Secure sign-up for hospital administrators.
* **User Login:** Authenticated access to the main system dashboard.

### Administration Module
Manage hospital staff with full CRUD (Create, Read, Update, Delete) functionality:
* **Doctors:** Track ID, Name, Specialization, Age, Address, Contact, Consultation Fees, and Monthly Salary.
* **Nurses:** Track ID, Name, Age, Address, Contact, and Monthly Salary.
* **Workers:** Track ID, Name, Age, Address, Contact, and Monthly Salary.

### Patient Module
Manage the lifecycle of a patient's stay:
* **Admissions:** Register new patients with details including recommended doctors.
* **Discharges:** Safely discharge patients upon confirmation of paid bills.
* **Search & View:** Retrieve all patient records or search for a specific patient by their ID.

---

## 🛠️ Prerequisites

To run this project, you need the following installed on your machine:
* **Python 3.x:** [Download here](https://www.python.org/downloads/)
* **MySQL Server:** [Download here](https://dev.mysql.com/downloads/mysql/)
* **MySQL Python Connector:** To connect the Python script to your MySQL database.

---

## 🚀 Setup and Installation

### 1. Install Dependencies
Open your command prompt or terminal and install the required Python MySQL connector:
```bash
pip install mysql-connector-python
```

### 2. Configure Database Credentials
By default, the script connects to your local MySQL database using the following credentials:
* **Host:** `localhost`
* **Username:** `root`
* **Password:** `root`

*⚠️ **Important:** If your local MySQL server uses a different password, open `CS_PROJECT_SFM.py` in a text editor and update line 2:*
```python
mydb=c.connect(host="localhost",user="root",password="YOUR_ACTUAL_PASSWORD")
```

### 3. Run the Application
Navigate to the directory where your script is located and run:
```bash
python CS_PROJECT_SFM.py
```
*Note: The script is designed to automatically create the required database (`hospital`) and all necessary tables the first time you run it.*

---

## 🗄️ Database Structure

The system automatically provisions the following tables in MySQL:
1. `user_data` - Stores administrator credentials.
2. `doctor_details` - Stores doctor profiles.
3. `nurse_details` - Stores nursing staff profiles.
4. `workers_details` - Stores auxiliary staff profiles.
5. `patient_details` - Stores patient admission data and discharge status.

---

## 💻 Usage Instructions

1. **Launch the app** and select **Option 2** to Register an admin account.
2. **Select Option 1** to Sign In with your new credentials.
3. Use the **Administration menu** to populate the hospital with Doctors, Nurses, and Workers.
4. Use the **Patient menu** to admit new patients and assign them to doctors.
