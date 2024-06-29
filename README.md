# Attendance Reminder Email System

This project automatically sends attendance reminder emails to students based on their attendance records fetched from a Google Sheet. The system uses Python for data fetching, processing, and email sending, and the APScheduler library to schedule tasks.

## Project Structure

- `main.py`: Main script to fetch data from Google Sheets, process it, and send emails.
- `send_email.py`: Contains the function to send emails using the SMTP protocol.
- `.env.txt`: Contains environment variables such as email credentials.
- `requirements.txt`: Lists the required Python packages.

## Features

1. **Data Fetching**: Fetches attendance data from a Google Sheet.
2. **Data Processing**: Processes the data to identify students with less than 75% attendance.
3. **Email Sending**: Sends reminder emails to the identified students.
4. **Scheduling**: Uses APScheduler to schedule the email sending task.

## Setup

### Prerequisites

- Python 3.6+
- Google Sheets API access
- SMTP server access (e.g., Gmail)

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/attendance-reminder.git
    cd attendance-reminder
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set up environment variables**:
    - Create a `.env.txt` file in the project root directory.
    - Add the following environment variables:
        ```
        SENDER_EMAIL=your-email@gmail.com
        EMAIL_PASSWORD=your-email-password
        ```

4. **Update Google Sheets URL**:
    - Replace `SHEET_ID` and `SHEET_NAME` in `main.py` with your Google Sheet ID and sheet name.

### Running the Project

1. **Run the main script**:
    ```bash
    python main.py
    ```

This will start the scheduler, which will execute the `job_function` at the specified time to send emails.

## Files Description

- **main.py**: 
    - Contains the primary logic to fetch data from Google Sheets, process the data, and send emails. 
    - Uses APScheduler to schedule the `job_function`.

- **send_email.py**:
    - Contains the `send_email` function to send emails using the SMTP protocol.
    - Loads environment variables from `.env.txt` for email credentials.

- **.env.txt**:
    - Stores sensitive information like email credentials.
    - Should be kept secure and not committed to version control.

- **requirements.txt**:
    - Lists the Python libraries required for the project:
        ```
        pandas
        requests
        apscheduler
        python-dotenv
        ```

## Example Terminal Output

When the `main.py` script runs, you should see output similar to the following in your terminal:


## Cloud Service Usage

This project uses **PythonAnywhere** for cloud-based scheduling and execution. Here’s how to set it up:

1. **Sign up and log in** to PythonAnywhere.
2. **Create a new scheduled task**:
    - Navigate to the "Tasks" tab.
    - Add a new task to run `main.py` at your desired schedule.
    - Make sure to upload all necessary files (`main.py`, `send_email.py`, `.env.txt`, `requirements.txt`) to your PythonAnywhere account.

### Using PythonAnywhere for Scheduling

1. **Sign up and log in** to PythonAnywhere.
2. **Create a new scheduled task**:
    - Navigate to the "Tasks" tab.
    - Add a new task to run `main.py` at your desired schedule.

## Customization

- **Email Content**: Modify the email content in `send_email.py` as per your requirements.
- **Schedule**: Update the scheduler settings in `main.py` to change the timing of the email sending task.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
## Example Terminal Output

When the `main.py` script runs, you should see output similar to the following in your terminal:

![Terminal Output](path/to/terminal_output_image.png)
