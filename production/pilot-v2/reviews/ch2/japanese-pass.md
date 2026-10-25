# Ch2 Japanese pass (native-editor check)

Scope: every voiced line in `production/pilot-v2/script/ch02.ozs`, including the `ins_match` insert. Checked against style guide §3b, §3c and §5, and against Ch1's Japanese. Most important first.

## Must fix (meaning, joke or subtext lost)

1. **c2_0298** 「……赤くない。」 In English, "…No." answers "always?", so it's an accidental admission: not always, so it's you. 赤くない is a flat denial, which is a different joke.
   → 「……いつもじゃない。」
2. **c2_0206** 「ああ。みずのも。いや……どういたしまして。」 みずのも isn't an autopilot slip anyone would recognize in Japanese; it just sounds odd. The natural Japanese flub is こちらこそ ("no, thank *you*"), and it keeps the subtext that he was very aware of his hand.
   → 「ああ。こちらこそ。……いや、どういたしまして。」
3. **c2_0167** 「転校生ボーナスだよ。」 She never says "luck," so Takatsuki's 「運は、技ではない。」 (c2_0168) answers something nobody said.
   → 「転校生のビギナーズラックだよ。金曜には切れるから。」
4. **c2_0070** 「新入部員はもう一人いる。」 A listener hears "there's *one more* new member," not "one already." Also, 「おかえり。」 from a captain to the whole club is translationese for "Welcome back," and 転入生 doesn't match Ch1's 転校生 (c1_0122).
   → 「久しぶりだな。一年の体験入部は来週からだ。一足先に、新入部員が一人入った。二年の転校生だ。みずの。」
5. **c2_0079** 「一年が来たら」 can also be heard as "when a year has passed."
   → 「たかつき。一年生が入ったら、そっちを任せる。辛抱強いやつが要る。」
6. **c2_0161** 「ああ。」 Agreeing with a negative question this way is correct Japanese, but by ear it can sound like "yeah, I did." The beat is that he didn't.
   → 「取らせてない。」
7. **c2_0222** 居残り稽古 means staying behind after club practice, which contradicts "mornings, weekends."
   → 「もし、自主練とかしたくなったら。朝でも、週末でも、いつでも。私、空いてるから。」
8. **c2_0115** 「狙ってやるのが、剣道で一番難しい技だ。」 says "doing it on purpose is the hardest technique." It doesn't hold together, and Takatsuki's sentences have to be correct.
   → 「出ばなは、狙って決めるのが剣道で最も難しい技だ。」

## Should fix (listening and TTS risks)

9. **面 in voiced lines.** On its own, or as 面が, the TTS can read it つら or おもて. Write it in kana:
   - c2_0095 → 「めん。あたま。」
   - c2_0297 → 「『めんあり』。めんが、ありました。」
   - c2_0125 → 「…めんを打つ間合いがおかしいのに…」
   - c2_0153 → 「みずの。いい小手だった。めんを打つ前に、左肩が下がる。直せ。」 (面の前に can also mean "in front of the face.")
10. **c2_0166** In 先を取れた, the TTS will probably say さき, but the kendo term is せん.
    → 「…僕は一年間ふじさわと稽古してきたが、せんを取れたことは一度もない。」
11. **c2_0017** 「火、木、日な。」 Single-kanji weekdays invite misreadings (ひ、き、ひ), and this doesn't match Ch1 (c1_0085) or c2_0225.
    → 「火曜、木曜、日曜。」
12. **c2_0132** 板 is an odd word for a whiteboard, and そのいたには is easy to mishear.
    → 「みずの。そのホワイトボードには、練習の予定が書いてあった。」
13. **c2_0102** A bare 気剣体 (きけんたい) sounds like 危険 ("danger"), and the standard term is 気剣体一致.
    → 「…全部いっしょに。気剣体一致。」
14. **竹刀 (c2_0102)**: listen on render for しない, not ちくとう. Keep the kanji, because kana しない gets the intonation of the verb "don't."

## Polish (naturalness, register)

15. **c2_0071** 「最初は、誰と打ち合えますか？」 is correct but flat, and the cheek is what gets the laugh. → 「で、最初の相手は誰ですか？」
16. **c2_0043** 「やめろ」 is rough toward a girl he met yesterday; elsewhere he keeps a courteous distance from her. → 「その話は勘弁してくれ。」
17. **c2_0164** 今の doesn't fit a debrief after practice has ended. → 「あれは、出ばな小手だった。」
18. **c2_0157** 半秒 is bookish when spoken. → 「一瞬、止まったな。止まるな。」 (The narration still says "half a second.")
19. **c2_0156** 「はい、主将。」 duplicates c2_0158 two lines later. → 「はい。」 so that 「……はい、主将。」 lands.
20. **c2_0126** → 「ビフォーアフターの、ビフォーだ！」 (ビフォーの写真 isn't idiomatic.)
21. **c2_0122** 「ふーじさわ！」 isn't how people chant. → 「ふじさわっ！ ふじさわっ！」 (Dropping -くん in a chant is natural.)
22. **c2_0093** 「剣道、第一回。」 → 「剣道講座、第一回。」
23. **c2_0098** 「突きだけ。」 reads as "only tsuki." → 「突くだけ。」 ("thrusts only")
24. **c2_0232** 「何の。」 → 「条件って？」
25. **c2_0233 / c2_0239** 楽しみでやってること is a little stiff. → 「きみが楽しくてやってること、ひとつ教えて。」 / 「それ、楽しくてやってるの？」 (c2_0240 still answers it.)
26. **c2_0085** At school Rika is wearing indoor shoes. → 「上履きを脱げ。」
27. **c2_0177** 「一年の仕事」 → 「一年生の仕事」 (the same ambiguity as item 5, milder).

## Address and pronouns (§3c): no violations
- Natsuki: 私; きみ only to Kōhei (c2_0233, c2_0239); bare ふじさわ; たかつきくん; polite to Kirishima, with 主将.
- **Natsuki → Rika: bare りか (c2_0108) is correct per §3c.** No change.
- Kōhei never says お前 in Ch2 and is polite to the manager.
- Takatsuki uses 僕, surnames and no "you."
- Kirishima uses bare surnames.
- The club says 主将.
- The classmates and Rika say なっちゃん; Rika uses あたし.
- The manager says ふじさわくん.

## Kendo (§5)
The insert calls are right: はじめ, 小手あり, 二本目, 胴あり, やめ, and the kiai めぇぇんっ / こてぇぇっ / どぉぉっ. 1–1 at time with only やめ (no 勝負) is correct. The terms are natural and right: 残心, 出ばな, 誘いに乗らずに, 切り返し, 試合稽古, 剣先, 間合い. Ch1 matches: 水曜, 土曜の午後は空いてる, ゴミ袋運び, 頭から/しっぽから, and the dojo count of six.

## Consistently good
- **Rika, the manager and the classmates** need no changes; they're natural, in register and funny.
- **Natsuki** has the strongest Japanese in the chapter outside items 3, 7 and 25: natural teen-girl speech, a clean polite switch with Kirishima, and well-judged comedy (お子様ランチ／年齢確認, 教材, 心は一年生, 遅咲き).
- **Kirishima**'s terse plain style is right; his only problems are the two ambiguities in items 4 and 5.
- **Takatsuki**'s register and form are right; his problems are grammar and TTS (items 8 and 10).
- **Kōhei** is fine apart from his two short replies (items 1 and 6) and the flub (item 2).
