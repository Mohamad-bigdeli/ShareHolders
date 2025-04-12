## Base URL:
```https://domain/shareholder/api/v1/```

## Authentication:
```Authorization: Bearer <your_access_token>```

# Endpoints:
- Title: List of shareholders of a symbol
- Endpoint: ```/shareholders/{symbol}/```
- Method: GET
- Description: Get a list of major shareholders of a specific symbol
- Response: 
    ```Json
        {
    "count": 125,
    "next": "https://domain/shareholder/api/v1/shareholders/خودرو/?page=2",
    "previous": null,
    "results": [
        {
        "id": 12345,
        "date": "2025-04-10",
        "shareholder_id": 22838937,
        "shareholder_name": "شرکت سرمایه گذاری تأمین اجتماعی",
        "shareholder_percentage": 15.2,
        "shareholder_shares": 1412104137,
        "change": 1,
        "symbol": "خودرو",
        "shareholder_instrument_id": "IRO1LKGH0008"
        }
    ]
    }
    ```
_____________________________________________________________________________

- Title: Advanced shareholder search
- Endpoint: ```/shareholders/search/```
- Method: GET
- Description: Search for shareholders based on various criteria
- Parameters:
    **q : Search text (shareholder name)**
    **symbol (optional): Filter by symbol**
- Response: 
    ```Json
        {
    "results": [
        {
        "id": 12345,
        "shareholder_name": "شرکت سرمایه گذاری تأمین اجتماعی",
        "symbol": "خودرو",
        "latest_percentage": 15.2,
        "latest_date": "2025-04-10",
        "instrument_id": "IRO1LKGH0008"
        }
    ]
    }
    ```
_____________________________________________________________________________

- Title: Daily ownership changes
- Endpoint: ```/changes/daily/{symbol}/```
- Method: GET
- Description: Receive changes in ownership percentage compared to the previous day
- Response: 
    ```Json
    {
    "symbol": "خودرو",
    "changes": [
        {
        "shareholder_id": 22838937,
        "shareholder_name": "شرکت سرمایه گذاری تأمین اجتماعی",
        "current_percentage": 15.2,
        "previous_percentage": 14.7,
        "percentage_change": 0.5,
        "current_shares": 1412104137,
        "shares_change": 5000000,
        "direction": "increase"
        }
    ],
    }
    ```
_____________________________________________________________________________

- Title: Weekly ownership changes
- Endpoint: ```/changes/weekly/{symbol}/```
- Method: GET
- Description: Get average ownership percentage changes from the previous week
- Response: 
    ```Json
    {
    "symbol": "خودرو",
    "changes": [
        {
        "shareholder_id": 22838937,
        "shareholder_name": "شرکت سرمایه گذاری تأمین اجتماعی",
        "current_avg_percentage": 15.1,
        "previous_avg_percentage": 14.9,
        "percentage_change": 0.2,
        "direction": "increase"
        }
    ],
    }
    ```
_____________________________________________________________________________

- Title: Monthly ownership changes
- Endpoint: ```/changes/monthly/{symbol}/```
- Method: GET
- Description: Get average ownership percentage changes compared to the previous month
- Response: 
    ```Json
    {
    "symbol": "خودرو",
    "changes": [
        {
        "shareholder_id": 22838937,
        "shareholder_name": "شرکت سرمایه گذاری تأمین اجتماعی",
        "current_avg_percentage": 15.0,
        "previous_avg_percentage": 14.5,
        "percentage_change": 0.5,
        "direction": "increase"
        }
    ],
    }
    ```