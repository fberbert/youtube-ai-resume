from __future__ import annotations
from pytubefix import YouTube

CAPTION_LANG = "a.en"  # auto-generated English

def fetch_caption(video_id: str, lang: str = CAPTION_LANG) -> str:
    """
    Download captions as plain text. Raises RuntimeError if unavailable.
    """
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    if not yt.captions or not yt.captions.get(lang):
        raise RuntimeError(f"Captions not found in language '{lang}'.")
    # generate_srt_captions() if you want timestamps.
    return yt.captions[lang].generate_txt_captions().strip()
