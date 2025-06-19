# Workout-Tracker

A Python application that tracks your workouts using natural language processing. Simply type in what exercises you did, and the app will automatically log the details including duration and calories burned to a Google Sheet.

## Features

- Natural language processing for exercise input
- Automatic calculation of calories burned
- Tracks exercise duration
- Logs workout data to Google Sheets
- Secure credential management using environment variables
- Timestamp recording for each workout entry

## Requirements

- Python 3.x
- Required Python packages:
  - `requests`
  - `python-dotenv`
- API Accounts:
  - Nutritionix API account
  - Sheety account (for Google Sheets integration)

## Setup

1. Clone this repository
2. Install required packages:
   ```bash
   pip install requests python-dotenv
   ```
3. Create a `.env` file in the project root with the following variables:
   ```
   APP_ID=your_nutritionix_app_id
   API_KEY=your_nutritionix_api_key
   SHEETY_TOKEN=your_sheety_bearer_token
   sheety_endpoint=your_sheety_api_endpoint
   ```

### API Setup

1. Sign up for a [Nutritionix API](https://www.nutritionix.com/business/api) account
   - Get your Application ID and API Key
2. Set up a [Sheety](https://sheety.co/) account
   - Create a new project connected to a Google Sheet
   - Get your Bearer token and API endpoint

## Configuration

Edit the following constants in `main.py` to match your details:
```python
GENDER = "Male"
WEIGHT_KG = 55
HEIGHT_CM = 180
AGE = 21
```

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. Enter your workout when prompted (e.g., "ran 3 miles and did 50 pushups")
3. The app will:
   - Process your input using Nutritionix API
   - Calculate calories burned
   - Log the workout details to your Google Sheet

## How It Works

1. Takes natural language input about your exercises
2. Sends the input to Nutritionix API for processing
3. Receives exercise details including:
   - Exercise name
   - Duration
   - Calories burned
4. Logs the data to a Google Sheet via Sheety API with:
   - Date
   - Time
   - Exercise name
   - Duration
   - Calories burned

## File Structure

- `main.py` - Main script containing the workout tracking logic
- `.env` - Environment variables file (you need to create this)
- `README.md` - Project documentation

## Security Note

Keep your API credentials secure:
- Never commit the `.env` file to version control
- Keep your Sheety Bearer token private
- Protect your Nutritionix API credentials