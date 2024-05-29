# Flask i18n Project

This project implements internationalization (i18n) in a Flask application using Flask-Babel.

## Project Structure

The project is organized into several Python files and directories:

- **Python Files:**
  - `0-app.py`: Basic Flask app setup.
  - `1-app.py`: Flask app with Babel setup.
  - `2-app.py`: Flask app with Babel setup and locale selection.
  - `3-app.py`: Flask app with Babel setup, locale selection, and template parameterization.
  - `4-app.py`: Flask app with Babel setup, locale selection, and locale parameter from URL.
  - `5-app.py`: Flask app with Babel setup, locale selection, and mock login.
  - `6-app.py`: Flask app with Babel setup, locale selection, and user preferred locale.
  - `7-app.py`: Flask app with Babel setup, locale and timezone selection, and mock login.

- **Directories:**
  - `templates/`: Contains HTML templates for the Flask app.
  - `translations/`: Contains translations for different locales.
    - `en/LC_MESSAGES/messages.po`: English translations.
    - `fr/LC_MESSAGES/messages.po`: French translations.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- Flask
- Flask-Babel
- pytz

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/alx-backend.git
   ```

2. Install dependencies:

   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the Flask app:

   ```bash
   python3 0-app.py
   ```

4. Access the app in your web browser at `http://127.0.0.1:5000`.

## License

This project is licensed under the [MIT License](LICENSE).
```
