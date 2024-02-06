# Rain Alert App

For my 35th day of programming in Python, I created an application to notify me when it's going to rain in my city. 

The idea was to utilize different APIs and experiment with sending SMS notifications through the Twilio platform.


## Features

- **Rain alerts:** Receive notifications when rain is forecasted.

## Usage

To use this app, you need to have Python installed on your system along with the required libraries. Additionally, you'll need to sign up for an account and obtain API keys from both OpenWeatherMap and Twilio.

1. Obtain API keys from [OpenWeatherMap](https://openweathermap.org/api) and [Twilio](https://www.twilio.com/docs/usage/api). 

2. Replace the placeholder strings in the code with your actual API keys:

    ```python
    api_key = "YOUR_OPENWEATHERMAP_API_KEY"
    account_sid = "YOUR_TWILIO_ACCOUNT_SID"
    auth_token = "YOUR_TWILIO_AUTH_TOKEN"
    ```

3. Ensure that you have configured the script with a trusted phone number to receive the alerts. Update the `to` parameter with your trusted phone number:

    ```python
    to='YOUR_TRUSTED_PHONE_NUMBER'
    ```

4. Run the script:

    ```bash
    python main.py
    ```

## Note

This application is configured to provide weather forecasts specifically for Brasília, Brazil. If you intend to use it for a different location, you can modify the latitude and longitude values in the `weather_params` dictionary accordingly.
