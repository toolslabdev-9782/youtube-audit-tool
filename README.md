# YouTube Channel Audit Tool (v1)

A simple, mentor-style YouTube channel audit tool that analyzes public channel data and explains growth health using human-readable rules.

## What This Tool Does
- Fetches public YouTube channel data using the official YouTube Data API
- Evaluates channel health using rule-based logic
- Provides explanations instead of raw analytics
- Works without login, scraping, or private data

## v1 Audit Rules (Frozen)
1. Content Volume Health  
   Evaluates subscriber traction relative to total videos.

2. Upload Consistency  
   Evaluates posting frequency based on channel age.

3. Subscriber Conversion Efficiency  
   Evaluates how effectively videos convert viewers into subscribers.

## Tech Stack
- Python 3.12
- Requests
- YouTube Data API v3

## Project Structure
youtube-audit-tool/
├── yt_test.py
├── youtube_api.py
├── audit_rules.py
└── README.md

## Legal & Safety
- Uses only publicly available YouTube data
- No video downloading
- No private analytics
- Not affiliated with or endorsed by YouTube or Google

## Status
v1 — Stable & Frozen
