# Tokyo Wards Map

This repository provides a small Streamlit application that plots the 23 special wards of Tokyo using [pydeck](https://pydeck.gl/).

## Setup

1. Install Python 3.11 or later.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application with Streamlit:

```bash
streamlit run app.py
```

The app will open in your browser and display a map centered on Tokyo with a point for each ward.

## Data

The `wards.csv` file contains the latitude and longitude for each ward. It is loaded automatically by `app.py`.

## Contributing

Pull requests and issues are welcome.
