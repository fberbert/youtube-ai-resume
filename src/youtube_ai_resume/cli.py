import os, sys, textwrap, argparse, rich
from rich.console import Console
from .caption import fetch_caption
from .summarizer import summarize, DEFAULT_MODEL

console = Console()

def app() -> None:
    parser = argparse.ArgumentParser(
        prog="youtube-ai-resume",
        description="Generate an AI summary of a YouTube video."
    )
    parser.add_argument("video_id", help="YouTube video ID (the bit after v=)")
    parser.add_argument(
        "-m", "--model", default=DEFAULT_MODEL, help="OpenAI model (default: %(default)s)"
    )
    args = parser.parse_args()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        console.print("[red]Set OPENAI_API_KEY in your environment.[/red]")
        sys.exit(1)

    try:
        transcript = fetch_caption(args.video_id)
    except Exception as exc:
        console.print(f"[red]❌  {exc}[/red]")
        sys.exit(1)

    with console.status("[green]Contacting OpenAI…"):
        summary = summarize(transcript, api_key, args.model)

    console.print("\n[bold cyan]Summary:[/bold cyan]\n")
    console.print(textwrap.dedent(summary))

if __name__ == "__main__":
    app()
