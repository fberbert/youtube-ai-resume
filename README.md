# youtube-ai-resume

**Generate concise AI summaries of YouTube videos from the command line.**  
It works in two steps:

1. Downloads the video caption (subtitles) with `pytubefix`.
2. Sends the caption to the OpenAI API and returns a summary in the language you choose.

<p align="center">
  <img src="https://img.shields.io/pypi/v/youtube-ai-resume?color=brightgreen" alt="PyPI">
  <img src="https://img.shields.io/pypi/pyversions/youtube-ai-resume" alt="Python Version">
  <img src="https://img.shields.io/github/license/your-user/youtube-ai-resume" alt="License">
</p>

---

## Features

* **Zero-setup CLI** → `youtube-ai-resume <video_id>`
* Summaries in any language (default `pt_BR`)
* Works with models like **`gpt-4.1-mini`** (configurable)
* Rich-formatted output with colours
* Usable as a *library* (`import youtube_ai_resume`)

---

## Installation

```bash
# Python ≥ 3.9
pip install youtube-ai-resume
```

Or, from source for hacking:

```bash
git clone https://github.com/fberbert/youtube-ai-resume.git
cd youtube-ai-resume
pip install -e ".[dev]"     # editable + dev tools
```

## Quick start

### Command Line Usage

```bash
export OPENAI_API_KEY="sk-..."
youtube-ai-resume dQw4w9WgXcQ     # Rick Astley demo 😄
```

Sample output:

```plaintext
Summary:

• Rick distances himself from breaking promises
• Emphasises commitment (“never gonna give you up…”) …
```

Library usage

```python
from youtube_ai_resume import caption, summarizer

txt = caption.fetch_caption("dQw4w9WgXcQ")
summary = summarizer.summarize(
    transcript=txt,
    api_key="sk-…",
    model="gpt-4.1-mini",
    out_lang="en"
)
print(summary)
```
## Configuration

You can set the OpenAI API key as an environment variable or in a config file.

Environment variable:

```bash
OPENAI_API_KEY="sk-..."
```

Config file at ~/.config/youtube-ai-resume/config.json (auto-created on first run) lets you change the default model.

```json
{
    "model": "gpt-4.1-mini",
    "out_lang": "en"
}
```

## Development

Contributions are welcome!

Fork ➜ branch ➜ PR.

ruff check . and pytest must pass.

Describe your change clearly.

## License

Released under the MIT License – see LICENSE.
