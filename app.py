from fastapi import FastAPI
import asyncio
from services.api import get_messages, get_reports_bulk
from services.calculator import calculate_credits

app = FastAPI()

@app.get("/usage")
async def usage():
    """Fetch messages, compute credit usage, and return structured data."""
    messages = await get_messages()
    report_ids = [msg['report_id'] for msg in messages if 'report_id' in msg]
    report_lookup = await get_reports_bulk(report_ids)

    usage_data = []
    for msg in messages:
        credits, report_name = calculate_credits(msg, report_lookup)

        usage_entry = {
            "id": msg["id"],
            "timestamp": msg["timestamp"],
            "credits": credits
        }

        if report_name:  # Only include report_name if it exists
            usage_entry["report_name"] = report_name

        usage_data.append(usage_entry)

    return {"usage": usage_data}
