"""Turn every spoken line in a day's content file into an MP3.

Usage:  python3 tools/make_audio.py 1
Needs:  pip3 install piper-tts, ffmpeg, and a Piper voice in tools/voice/
        (download: https://github.com/rhasspy/piper/releases/tag/v0.0.2)

Output: app/audio/day1/<line id>.mp3, one file per line. Only lines whose
text changed since the last run are regenerated.
"""
import hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VOICE = ROOT / "tools" / "voice" / "en-us-lessac-medium.onnx"

day = sys.argv[1] if len(sys.argv) > 1 else "1"
content = json.loads((ROOT / "app" / "content" / f"day{day}.json").read_text())
out = ROOT / "app" / "audio" / f"day{day}"
out.mkdir(parents=True, exist_ok=True)
stamp_file = out / ".stamps.json"
stamps = json.loads(stamp_file.read_text()) if stamp_file.exists() else {}

for key, text in content["lines"].items():
    h = hashlib.md5(text.encode()).hexdigest()
    mp3 = out / f"{key}.mp3"
    if stamps.get(key) == h and mp3.exists():
        continue
    wav = out / f"{key}.wav"
    subprocess.run(["python3", "-m", "piper", "-m", str(VOICE), "-f", str(wav), "--sentence-silence", "0.25"],
                   input=text.encode(), check=True, capture_output=True)
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ac", "1", "-b:a", "40k", str(mp3)], check=True)
    wav.unlink()
    stamps[key] = h
    print("made", mp3.name)

stamp_file.write_text(json.dumps(stamps, indent=1))
print("done:", len(content["lines"]), "lines")
