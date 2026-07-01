import os

bind = f"0.0.0.0:{os.environ.get('PORT', '8080')}"
workers = 2
timeout = 300       # Claude API calls can take 60-120s on long prompts
