import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from openai import OpenAI
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()

class SpotifyAIRecommender:
    def __init__(self):
        # Initialize Spotify client
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id=os.getenv('SPOTIFY_CLIENT_ID'),
            client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
            redirect_uri='http://localhost:8888/callback',
            scope='user-top-read user-library-read playlist-modify-public'
        ))
        
        # Initialize OpenAI client
        self.openai_client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def get_top_artists(self, limit=20):
        """Get user's top artists"""
        results = self.sp.current_user_top_artists(limit=limit, time_range='medium_term')
        return [(item['name'], item['genres']) for item in results['items']]

    def get_artist_features(self, artist_id):
        """Get detailed information about an artist"""
        artist = self.sp.artist(artist_id)
        return {
            'name': artist['name'],
            'genres': artist['genres'],
            'popularity': artist['popularity'],
            'followers': artist['followers']['total']
        }

    def generate_ai_recommendations(self, top_artists):
        """Generate AI-powered recommendations based on user's top artists"""
        # Create a prompt for the AI
        artists_str = ", ".join([artist[0] for artist in top_artists[:5]])
        genres_str = ", ".join(set([genre for _, genres in top_artists for genre in genres]))
        
        prompt = f"""Based on the user's top artists: {artists_str}
        And their preferred genres: {genres_str}
        Suggest 5 new artists they might enjoy. Consider musical style, genre, and artistic influence.
        Format your response as a comma-separated list of artist names only."""

        # Get AI recommendations
        response = self.openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a music recommendation expert."},
                {"role": "user", "content": prompt}
            ]
        )
        
        return response.choices[0].message.content.strip().split(", ")

    def search_recommended_artists(self, artist_names):
        """Search for recommended artists on Spotify"""
        recommendations = []
        for name in artist_names:
            results = self.sp.search(q=name, type='artist', limit=1)
            if results['artists']['items']:
                artist = results['artists']['items'][0]
                recommendations.append({
                    'name': artist['name'],
                    'genres': artist['genres'],
                    'popularity': artist['popularity'],
                    'spotify_url': artist['external_urls']['spotify']
                })
        return recommendations

def main():
    recommender = SpotifyAIRecommender()
    
    # Get user's top artists
    print("Fetching your top artists...")
    top_artists = recommender.get_top_artists()
    
    # Generate AI recommendations
    print("\nGenerating AI-powered recommendations...")
    ai_suggestions = recommender.generate_ai_recommendations(top_artists)
    
    # Search for recommended artists on Spotify
    print("\nFinding detailed information about recommendations...")
    recommendations = recommender.search_recommended_artists(ai_suggestions)
    
    # Display recommendations
    print("\nRecommended Artists:")
    for i, rec in enumerate(recommendations, 1):
        print(f"\n{i}. {rec['name']}")
        print(f"   Genres: {', '.join(rec['genres'])}")
        print(f"   Popularity: {rec['popularity']}/100")
        print(f"   Spotify URL: {rec['spotify_url']}")

if __name__ == "__main__":
    main()
