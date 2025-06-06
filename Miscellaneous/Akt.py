# Importing the yfinance package
import yfinance as yf
 
# Set the start and end date
start_date = '2020-01-01'
end_date = '2023-01-01'
 
# Set the ticker
ticker = 'GOOGL'
 
# Get the data
data = yf.download(ticker, start_date, end_date)
 
# Print the last 5 rows
data.to_excel('Akt.xlsx', index=False)
