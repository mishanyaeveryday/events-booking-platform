# Events Booking Platform

## Project Description
This is an application for managing and displaying events. Users can browse the list of events, filter them by categories, and view detailed information for each event. The application also supports event payment via PayPal and displays a map with the event's location.

## Features
- View all events.
- View events by category.
- Detailed information about each event, including description, price, date, and location.
- Ability to pay for events via PayPal.
- Display a map with the event's location.
- Success and failure statuses for payments.

## Technologies
The project is built using the following technologies:
- **Python** and **Django**: The main backend framework.
- **PostgreSQL**: Database for storing event and category information.
- **Folium**: Used to display a map with the event's location.
- **Geocoder**: For fetching coordinates based on location names.
- **PayPal SDK**: For handling payments via PayPal.
- **Bootstrap**: For styling and responsive UI.
- **HTML/CSS** and **JavaScript**: For displaying the user interface.

## Installation and Running the Project

1. Clone the repository:
   ```bash
   git clone https:https://github.com/mishanyaeveryday/events-booking-platform.git
   ```

2. Navigate to the project directory:
   ```bash
   cd events-app
   ```

3. Install dependencies:
   If you're using `pipenv`:
   ```bash
   pipenv install
   pipenv shell
   ```
   If you're using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## PayPal Settings
To work with PayPal, add the following settings in `settings.py`:
```python
PAYPAL_RECEIVER_EMAIL = 'your-paypal-email@example.com'
PAYPAL_TEST = True  # Set to False for production
```

## Usage
- Visit the homepage to browse the list of all events.
- To view events by category, select a category.
- To see more details about an event, click on its title.
- If the event is paid, you will be able to pay for it via PayPal.
- The event page will also display a map showing the event location.

## Notes
- Maps are generated using the Folium library, which uses location coordinates for rendering.
- If the location cannot be found or coordinates are unavailable, the map will display "Location Unknown."
- If there are issues with the map, ensure that geocoding is working correctly for the given locations.

## License
This project is licensed under the MIT License.

---
