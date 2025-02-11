# Spotify-Claude AI Recommender

This application connects to your Spotify account and uses Anthropic's Claude AI to provide personalized music recommendations based on your listening history. It analyzes your top artists and their genres to suggest new artists you might enjoy.

## Features

- 🎵 Fetches your top artists from Spotify
- 🤖 Uses Claude 3.5 for AI-powered recommendations
- 📊 Provides detailed artist information including genres and popularity
- 🔗 Includes direct Spotify URLs for recommended artists
- ✨ Clean, type-checked Python implementation

## Requirements

- Python 3.9 or higher
- Spotify Developer account
- Anthropic API key

## Setup

1. Create a Spotify Developer account and register your application at https://developer.spotify.com/dashboard
2. Get an API key from Anthropic at https://console.anthropic.com/
3. Create a `.env` file with your credentials:
   ```env
   SPOTIFY_CLIENT_ID=your_client_id
   SPOTIFY_CLIENT_SECRET=your_client_secret
   ANTHROPIC_API_KEY=your_anthropic_api_key
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main script:
```bash
python main.py
```

The application will:
1. Connect to your Spotify account (will open browser for authentication)
2. Fetch your top artists
3. Generate AI-powered recommendations using Claude
4. Display detailed information about recommended artists

## Development

This project uses several tools to maintain code quality:

- `mypy` for static type checking
- `flake8` for code linting
- `black` for code formatting
- `isort` for import sorting

Run the checks locally:
```bash
mypy main.py
flake8 .
black . --check
isort . --check-only
```

## GitHub Actions

Continuous Integration is set up to run automatically on pull requests and pushes to main. It includes:
- Type checking with mypy
- Code linting with flake8
- Import sorting with isort
- Code formatting with black
- Testing on Python 3.9, 3.10, and 3.11

## License

MIT License
