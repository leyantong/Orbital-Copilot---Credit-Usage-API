import asyncio
import aiohttp
from config import MESSAGES_API, REPORTS_API_BASE

async def fetch_json(session, url):
    """Asynchronously fetch JSON data from a given URL."""
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()
    except aiohttp.ClientError as e:
        print(f"Request failed: {url} - {e}")
        return None

async def get_messages():
    """Fetch messages for the current billing period."""
    async with aiohttp.ClientSession() as session:
        response = await fetch_json(session, MESSAGES_API)
        return response.get("messages", []) if response else []

async def get_reports_bulk(report_ids):
    """Fetch multiple reports asynchronously to optimize API calls."""
    reports = {}
    async with aiohttp.ClientSession() as session:
        tasks = {rid: fetch_json(session, f"{REPORTS_API_BASE}{rid}") for rid in set(report_ids)}
        results = await asyncio.gather(*tasks.values())
        for rid, result in zip(tasks.keys(), results):
            if result:
                reports[rid] = result
    return reports