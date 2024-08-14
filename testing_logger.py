import requests
import pandas as pd
from time import sleep
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_ticker(company_name):
    try:
        yfinance = "https://query2.finance.yahoo.com/v1/finance/search"
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
        params = {"q": company_name, "quotes_count": 1, "country": "United States"}

        res = requests.get(url=yfinance, params=params, headers={'User-Agent': user_agent})
        data = res.json()

        company_code = data['quotes'][0]['symbol']
        print(f"Ticker for {company_name}: {company_code}")
        return company_name, company_code
    except Exception as e:
        print(f"Error for {company_name}: {e}")
        return company_name, None

def process_company(company_name):
    ticker = get_ticker(company_name)
    sleep(1)  # Add a small delay to avoid overwhelming the API
    return ticker

df = pd.read_csv("JAY_SHAH_DATA.csv")

# Create a list to store results
results = []

# Use ThreadPoolExecutor to run the tasks in parallel
with ThreadPoolExecutor(max_workers=4) as executor:
    # Submit tasks for each company
    future_to_company = {executor.submit(process_company, row['full_name']): row['full_name'] for _, row in df.iterrows()}
    
    # Process completed tasks
    for future in as_completed(future_to_company):
        company_name, ticker = future.result()
        if ticker:
            results.append({'Company Name': company_name, 'Ticker Symbol': ticker})

# Create a new dataframe from the results list
result_df = pd.DataFrame(results)

# Save the result to a new CSV file
output_file = 'company_tickers.csv'
result_df.to_csv(output_file, index=False)

print(f"Results saved to {output_file}")