# Spotify AI Music Recommender

This application connects to your Spotify account and uses AI to provide personalized music recommendations based on your listening history.

## Setup

1. Create a Spotify Developer account and register your application at https://developer.spotify.com/dashboard
2. Create a `.env` file with your credentials:
   ```
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   OPENAI_API_KEY=your_openai_api_key
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```
python main.py
```
