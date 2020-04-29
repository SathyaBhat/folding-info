import requests
from time import asctime
from json import loads
from sys import exit
from os import environ

def get_and_publish_stats():
  discord_webhook = environ.get('DISCORD_WEBHOOK')
  stats_url = environ.get('STATS_URL')
  response = requests.get(stats_url)
  if response.status_code != 200:
        print(f"Couldn't fetch stats, status code: {response.status_code}")
        exit(1)
  discord_message = {
    "content": f"Folding@Home stats for Hackatta as of {asctime()} UTC",
    "embeds": [
      {
        "description": f"```{response.text}```",
        "title": "Team Summary",
        "url": "https://folding.extremeoverclocking.com/team_summary.php?s=&t=237378",
        "color": 4289797,
        "footer": {
          "icon_url": "https://foldingathome.org/wp-content/uploads/2016/09/cropped-folding-at-home-logo-1-64x64.png",
          "text": "Folding@Home"
        }
      }
    ]
  }

  discord_response = requests.post(url=discord_webhook, json=discord_message)
  if discord_response.status_code != 204:
    print(f"Could not post to discord, status code {discord_response.status_code}")
