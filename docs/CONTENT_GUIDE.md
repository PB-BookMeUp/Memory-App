# Content guide

How every lesson and quiz is written. Keep to this so Day 30 sounds like Day 1.

## Voice

Priya. A friendly coach. Warm, encouraging, never talks down. Uses "aap". Think of a kind family doctor who is pleased to see you.

## It's a chat

Every session is a chat with Priya, like WhatsApp. She sends one short message at a time, with typing dots first. The person replies by tapping a chip. Pictures (emoji scenes) carry the story; the words are backup.

Rules for a message: one idea, under 15 words, an emoji where a friend would use one. Never two sentences that could be two messages.

## Language

Indian English with natural Hinglish, the way a Mumbai or Delhi doctor talks to a patient's mother. Short spoken sentences. Hindi words where they come naturally (namaste, aap, theek hai, shabash, sabzi), English for anything technical. Never a full Hindi sentence that needs reading. Written the way she'd type on WhatsApp.

## Shape of a day

A day is a list of steps in `app/content/dayN.json`. Step types: `say` (one or more messages), `ask` (chips), `scene` (an animated card: actors with x, y, size, anim, delay) with a caption, `list`, `chain`, `palace`, `game` (order, pairs, walk, place, recallWalk), `quiz`, `test`, `score`. Four to five minutes a day.

Animations available for scene actors: bob, popup, drop, slidel, spin, shake, floatup, fade, grow, wobble, glow, pulse, bounce, walk. Backgrounds: warm, teal, pink.

Under 5 minutes total.

## Rules

- One idea per screen
- Wrong answers get a gentle "not this one" plus the reason, never "wrong"
- Every quiz tests the technique, not trivia
- Examples come from daily life in an Indian home: sabzi lists, phone numbers, festival dates, where the keys are
- Day score: 10 for finishing plus 90 spread across the day's games. Brain score is the average of the last 5 days

## Where content lives

Each day's words are in `app/content/dayN.json` under `chat`. Shared lines (first open, review) are in `app/content/app.json`. Edit words there, never in `app/index.html`.
