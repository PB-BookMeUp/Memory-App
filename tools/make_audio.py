"""Turn every spoken line in a content file into an MP3 in Priya's voice.

Usage:  python3 tools/make_audio.py day1      (reads app/content/day1.json)
        python3 tools/make_audio.py app       (reads app/content/app.json, the shared lines)
Needs:  pip3 install kokoro-onnx soundfile, ffmpeg, and the Kokoro model files in tools/voice/
        (kokoro-v1.0.onnx and voices-v1.0.bin from github.com/thewh1teagle/kokoro-onnx/releases)

Output: app/audio/<name>/<line id>.mp3. Only lines whose text changed are regenerated.
"""
import hashlib, json, pathlib, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
VOICE = "hf_alpha"      # Priya's voice. Indian, Hindi-trained. Change here to change her everywhere.
LANG = "hi"
SPEED = 0.95

name = sys.argv[1] if len(sys.argv) > 1 else "day1"
content = json.loads((ROOT / "app" / "content" / f"{name}.json").read_text())
out = ROOT / "app" / "audio" / name
out.mkdir(parents=True, exist_ok=True)
stamp_file = out / ".stamps.json"
stamps = json.loads(stamp_file.read_text()) if stamp_file.exists() else {}

todo = {k: t for k, t in content["lines"].items()
        if stamps.get(k) != hashlib.md5((VOICE + t).encode()).hexdigest() or not (out / f"{k}.mp3").exists()}
if todo:
    import soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(str(ROOT / "tools/voice/kokoro-v1.0.onnx"), str(ROOT / "tools/voice/voices-v1.0.bin"))
    for key, text in todo.items():
        samples, sr = k.create(text, voice=VOICE, speed=SPEED, lang=LANG)
        wav = out / f"{key}.wav"
        sf.write(wav, samples, sr)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(wav), "-ac", "1", "-b:a", "48k", str(out / f"{key}.mp3")], check=True)
        wav.unlink()
        stamps[key] = hashlib.md5((VOICE + text).encode()).hexdigest()
        print("made", key)
stamp_file.write_text(json.dumps(stamps, indent=1))
print(f"{name}: {len(content['lines'])} lines, {len(todo)} made")
