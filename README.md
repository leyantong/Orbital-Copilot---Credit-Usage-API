# Orbital-Copilot---Credit-Usage-API
This project provides an async FastAPI backend for computing credit usage in Orbital Copilot, an AI assistant for real estate lawyers. It aggregates message data and calculates credit consumption based on predefined rules.

#### **Features**
- **Efficient Asynchronous API Calls**: Uses `aiohttp` to fetch messages and report details concurrently.
- **Optimized Credit Calculation**: Implements multiple business rules, including text-based calculations and report-specific credit costs.
- **Scalable and Maintainable**: Modular architecture with separate concerns for API requests, credit calculation, and configuration.

---

## **Setup & Installation**
### **Prerequisites**
- Python 3.8+
- `pip` (Python package manager)

### **Installation Steps**
1. Clone the repository:
   ```sh
   git clone https://github.com/<your-username>/Orbital-Copilot-Credit-Usage-API.git
   cd Orbital-Copilot-Credit-Usage-API
   ```
2. Create a virtual environment (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

---

## **Running the API**
Start the FastAPI server:
```sh
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
The API will be available at:
- **Docs**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)
- **Redoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Usage**
### **GET `/usage`**
Fetches credit usage data for the current billing period.

#### **Request**
```sh
curl http://127.0.0.1:8000/usage
```

#### **Response Example**
```json
{
  "usage": [
    {
      "id": 1000,
      "timestamp": "2024-04-29T02:08:29.375Z",
      "credits": 79,
      "report_name": "Tenant Obligations Report"
    },
    {
      "id": 1001,
      "timestamp": "2024-04-29T03:25:03.613Z",
      "credits": 5.2
    }
  ]
}
```
- Messages linked to reports display the report name.
- Messages without reports are calculated based on text rules.

---

## **Project Structure**
```
Orbital-Copilot-Credit-Usage-API/
│── app.py          # FastAPI entry point
│── services/
│   ├── api.py      # Handles external API requests (messages & reports)
│   ├── calculator.py # Implements credit calculation logic
│── config.py       # Stores API endpoint configurations
│── tests/
│   ├── test_api.py
│   ├── test_calculator.py
│── requirements.txt # Dependency list
│── README.md       # Project documentation
```

### **Key Highlights**
- **Asynchronous API Requests**: Uses `aiohttp` for concurrent fetching of messages and reports.
- **Optimized Batch Processing**: Minimizes API calls using bulk report retrieval.
- **Robust Text-Based Credit Calculation**: Implements multiple rules, including character count, word length, palindromes, and penalties.
- **Modular and Extensible**: Clean separation of concerns for better maintainability.

---

## **Development & Contribution**
### **Testing**
Run API locally and use:
```sh
pytest
```
### **Code Formatting**
Follow PEP8 conventions:
```sh
black .
```
### **Extending the API**
- Modify `calculator.py` to adjust credit computation rules.
- Extend `api.py` to integrate new external data sources.

---

## **License**
This project is licensed under the MIT License.
