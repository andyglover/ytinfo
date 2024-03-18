#!/usr/bin/env python

#imports
from pytube import YouTube
import pyperclip
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

# Function to convert seconds to minutes and seconds format
def convert_seconds_to_minutes(seconds):
    minutes = seconds // 60
    seconds %= 60
    return f"{minutes:02d}:{seconds:02d}"

#sanitize youtube URL
def clean_youtube_url(url):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    # Remove the 'pp' parameter if it exists
    if 'pp' in query_params:
        del query_params['pp']
    # Reconstruct the query string without the 'pp' parameter
    cleaned_query = urlencode(query_params, doseq=True)
    # Reconstruct the URL with the cleaned query
    cleaned_url = parsed_url._replace(query=cleaned_query)
    return urlunparse(cleaned_url)

#main function
def main():
    print("Enter YouTube video URLs (one URL per line). Press Enter on an empty line when done:")
    # make input from lines of URLS
    urls = []
    while True:
        url = input().strip()
        if not url:  # If the input is empty, break the loop
            break
        urls.append(url)

    #initialize all output variable.
    all_output= ""

    #loop through urls
    for url in urls:
        # Clean up the YouTube URL
        cleaned_url = clean_youtube_url(url)

        # Create a YouTube object
        yt = YouTube(cleaned_url)

        # Extract video details
        video_title = yt.title
        channel_name = yt.author
        video_length_seconds = yt.length

        # Convert video length to minutes and seconds format
        video_length_formatted = convert_seconds_to_minutes(video_length_seconds)

        # Construct the output string
        output = f"{channel_name} - {video_title} ({video_length_formatted})"

        # Add a line break before appending the YouTube URL
        output += "\n"

        # Append the YouTube URL
        output += cleaned_url
        # Add 2 line breaks after the YouTube URL
        output += "\n\n"

        # Add the output for this URL to the all_output string
        all_output += output

    # Copy all output to the clipboard
    pyperclip.copy(all_output)
    # Print all output
    print(all_output)

    # Indicate that the script has finished execution
    print("Output copied to clipboard, script execution complete.")

#run main function
if __name__ == "__main__":
    main()
