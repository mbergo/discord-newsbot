import discord
import asyncio
import feedparser

# URLs of tech news sites
tech_sites = ['https://www.techspot.com/rss/',
                'https://www.theverge.com/tech/rss/index.xml',
                'https://www.techradar.com/rss',
                'http://feeds.feedburner.com/extremetech',
                'https://www.cnet.com/rss/news/',
                'http://feeds.feedburner.com/DigitalTrends-All',
                'http://feeds.feedburner.com/Gizmodo/Full',
                'https://www.engadget.com/rss.xml',
                'http://feeds.arstechnica.com/arstechnica/index/',
                'https://www.theguardian.com/technology/rss']

# Your bot token
token = 'MTA3MDI3MTk3NDUzNTg2ODQ0Ng.G1byc8.aU852wZ_wKwG1fjNvUbMpLiQ4cWsnkpGJjCaYQ'

# Channel ID to post to
channel_id = '1064552688941027391'

# Client object
client = discord.Client(intents=discord.Intents.all())

# Global list of already posted items
posted_items = []

# Function to parse the RSS feed and post new items
async def check_feed():
    while not client.is_closed():
        # Loop through each tech site
        for site in tech_sites:
            # Parse the RSS feed
            feed = feedparser.parse(site)
            # Loop through each item
            for item in feed['items']:
                # Check if the item has not been posted before
                if item['link'] not in posted_items:
                    # Post the item to the channel
                    await client.get_channel(1064552688941027391).send(item['title'] + '\n' + item['link'])
                    # Add the item to the list of posted items
                    posted_items.append(item['link'])
        # Sleep for 60 seconds
        await asyncio.sleep(60)

# On ready
@client.event
async def on_ready():
    # Start the RSS checking loop
    client.loop.create_task(check_feed())

# Start the bot
client.run(token)