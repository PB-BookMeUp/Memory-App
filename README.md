# Memory-App

A daily memory and brain-fitness app for Indian adults aged 40 to 60. Bite-sized lessons, quizzes, and streaks, built to be relatable and habit-forming.

## Where things live

- `docs/VISION.md`: what we're building and the decisions made so far
- `docs/DECISIONS.md`: running log of choices, newest at the bottom
- `docs/CONTENT_GUIDE.md`: how lessons and quizzes are written
- `app/index.html`: the app screens and games
- `app/content/app.json`: Priya's lines for onboarding, home, review, family, progress
- `app/content/day1.json`: Day 1 words, list, story and quiz
- `app/audio/`: one MP3 per line, made from the content files
- `tools/make_audio.py`: turns a content file into Priya's voice (`python3 tools/make_audio.py day1`)
- `docs/APP_BLUEPRINT.md`: the full app, screen by screen

More folders (app code, lesson content) get added as we reach those steps.
