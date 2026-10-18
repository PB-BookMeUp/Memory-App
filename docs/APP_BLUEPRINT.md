# App blueprint

What a finished version looks like, worked back from memoryOS, Elevate and Duolingo. Everything below is a proposal until ticked in DECISIONS.md.

## The one idea that makes these apps work

Show the person their own improvement within the first five minutes. memoryOS does this with a before-and-after word test. Elevate does it with a placement test that produces a score. The person remembers 3 words, learns a trick, then remembers 8. That moment sells the habit. Nothing else matters as much.

## Screens

### 1. First open (once)
1. Welcome from the coach, 1 screen, voice on
2. "What do you forget most?" four big tiles: names, where I kept things, shopping lists, what I walked into the room for
3. "How old are you?" four bands. Sets the examples and the pace
4. Memory test: 8 everyday items, 20 seconds, then tap what you remember. Result: "You remembered 3 of 8." This is the starting brain score
5. Straight into Day 1, which teaches the Story Chain and ends with the same test. "Now you remembered 7 of 8." Brain score jumps on screen

### 2. Home (every day after)
- Greeting with name and the coach's face
- Today's session, one big card, with time to finish (3 min)
- Brain score, streak days, and this week as seven dots
- Review card when something is due ("Still remember Monday's list?")
- The path: days ahead, locked, with the technique name on each

### 3. A session
Same shape every day so it never needs explaining:
1. Learn: the coach talks, visuals build as she speaks, 60 to 90 seconds
2. Practise: do the technique on today's list, with help
3. Test: the list is hidden, play 2 short rounds
4. Score: ring fills, coach reacts, one thing to try at home

### 4. Review (spaced repetition)
Old lists come back after 1, 3 and 7 days. One minute. This is what makes the memory real, and it gives the person a reason to open the app on days they'd skip.

### 5. Progress
- Brain score over time, a line going up
- Days done, longest streak
- Techniques learned, as badges
- Lists remembered, as a count that keeps growing

### 6. Daily reminder
- She picks a time on first open ("When do you have three quiet minutes?" morning, afternoon, evening)
- The coach's voice says the reminder line once so it feels like her, not the phone
- On Android, a reminder works once the app is added to the home screen (one tap, we show how). On iPhone it also needs that step. Reminders need a small free server to send them, which comes with the leaderboard below
- Until that server exists, the founder sends the link on WhatsApp at her chosen time
- Missed two days: the reminder softens ("No pressure. Two minutes when you're ready.") instead of nagging

### 7. Family leaderboard
- A family is a six-letter code. The founder makes one, shares it on WhatsApp, each person types it in once. No accounts, no passwords
- The board shows each family member's first name, brain score, and streak. One screen, ranked, with a crown on the leader
- Weekly reset of a "this week" column so a newcomer can still win a week. Lifetime score stays alongside
- A nudge card: "Rohan did his session today. Your turn." This is the single stickiest thing in Duolingo's design and it works harder with family than with strangers
- Shared scores need a small free database. Options at zero cost: Supabase or Firebase free tier. Decision in DECISIONS.md once chosen

## The course, 30 days

| Days | Technique | What she practises it on |
|---|---|---|
| 1 to 5 | Story Chain | Shopping lists, errands |
| 6 to 10 | Memory Palace, using rooms of her own home | Longer lists, things to do |
| 11 to 15 | Names and faces | Relatives, neighbours, new people |
| 16 to 20 | Numbers as pictures | Phone numbers, PINs, dates |
| 21 to 25 | Where did I keep it | Keys, glasses, documents |
| 26 to 30 | Long text | Prayers, verses, speeches |

Each day: one new idea, never two.

## The coach
- A name and a face. Always the same voice
- Warm, unhurried, a little playful. Never a quiz master
- Speaks every screen. Text on screen is one line, never a paragraph

## Visual style, three directions to choose from
1. **Calm clinic**: soft off-white, deep indigo, marigold accents, rounded cards. Feels trustworthy, like a good doctor's app
2. **Warm home**: terracotta, cream, botanical greens, hand-drawn feel. Feels like a family kitchen
3. **Bright game**: saturated colours, big friendly shapes, bouncy motion. Feels like Duolingo

## What is free and what isn't
Free today: the web app, the coach's voice (Kokoro, open source), hosting, the content. Not free later: an app store listing (Google Play is a one-time 25 dollars, Apple is 99 dollars a year), and proper illustrations unless drawn in-house.
