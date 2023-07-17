# YouTube Time Code Scraper

This Python program allows you to retrieve comments from a YouTube video and displays only the comments that contain a time code. It uses the YouTube Data API v3 to fetch the comments associated with a given video link and filters them based on the presence of a time code in the format "MM:SS".

## Prerequisites

- Python 3.6 or higher
- `google-api-python-client` package
- A valid YouTube Data API v3 key

## Installation

1. Clone the repository:

`git clone https://github.com/developedbyalex/youtube-time-code-scraper.git`


2. Install the required dependencies:

`pip install google-api-python-client`


3. Set up your YouTube Data API v3 key:
   
- Visit the [Google Cloud Console](https://console.cloud.google.com/).
- Create a new project or select an existing one.
- Enable the YouTube Data API v3 for your project.
- Generate an API key.

4. Update the API key:
   
- Open `app.py` in a text editor.
- Replace `'YOUR_YOUTUBE_API_KEY'` with your actual YouTube Data API v3 key.
- Save the file.

## Usage

1. Run the program:

`python app.py`


2. Enter the YouTube video link when prompted.

3. The program will retrieve the comments from the video and display only the comments that contain a time code in the format "MM:SS".


## Limitations

- The program relies on the availability of comments and their associated time codes in the video. If there are no comments or no comments with time codes, the program will display a message indicating that.

## License

This project is licensed under the [MIT License](LICENSE).
