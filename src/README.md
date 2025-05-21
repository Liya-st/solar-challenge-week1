# Solar Dashboard

This is a Streamlit dashboard to explore solar irradiance data across African countries.

## Features

- Select multiple countries
- Boxplot visualization for GHI, DNI, or DHI
- Table of top 10 regions by solar potential

## 🚀 How to Run

1. Clone the repo and checkout the `dashboard-dev` branch:

```bash
git clone <repo-url>
cd <repo-name>
git checkout -b dashboard-dev
Create a data/ directory and place solar_data.csv inside (not tracked by Git).
```
## Install dependencies:
```

pip install -r requirements.txt
```
### Run the app:

````
streamlit run app/main.py
````