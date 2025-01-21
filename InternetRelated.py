import webbrowser

from pytube import Search


def play_song_on_youtube(query):
    """
    Searches for the song on YouTube and plays the top result.
    """

        # Search for the query on YouTube
    search = Search(query)
    video = search.results[0]  # Get the first video in the search results
    video_url = video.watch_url  # Get the URL of the video

        # Open the top result in the default web browser
    webbrowser.open(video_url)

