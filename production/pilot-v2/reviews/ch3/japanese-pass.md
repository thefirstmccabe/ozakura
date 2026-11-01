# Ch3 Japanese pass (native-editor check), Nov 1

Scope: every voiced line in `production/pilot-v2/script/ch03.ozs` ("Windows"), including the five lines changed by the overcorrection fixes during the pass (c3_0333, c3_0348, c3_0364, c3_0392, c3_0393). Those were re-read from the current file; `git diff` shows no other voiced line changed. Checked against style guide §3b, §3c and §5, and against the Japanese in Ch1 and Ch2 (grepped). Fresh agent using `production/pipeline/review/japanese-pass.md`. The reviewer edited nothing. Most important first.

## Must fix

1. **c3_0332** (Takatsuki): 公平 is read こうへい, so 公平のために sounds like "for Kōhei's sake," as if Takatsuki, who only ever says "Fujisawa," used his given name. Separately, with みずのは still the topic, 一度も気づいていなかった is heard as "Mizuno never noticed."
   → 「ふじさわ。みずのは、めんを打つ前に、まだ左肩が下がる。ふじさわは、一度も気づいていなかった。対等にするために、言っておく。」
   (Using the surname as the subject is how he avoids "you" (§3c).) The new c3_0333, 「どっちの味方なの？」 ("Whose side are you on?"), makes the mishearing more likely, because "for Kōhei's sake" seems to answer it. With 対等, her question still works.

## Should fix (meaning, listening, register)

2. **c3_0357** (Natsuki): 左手…振ってる most naturally means "waving your left hand." Shaking it out is ぶらぶら.
   → 「あと、左手。十段ごとくらいに、ぶらぶらさせてる。授業中もやってるよ。三時間目。」
3. **c3_0343** (Natsuki): with no object, 聞いたよね can mean "you heard" as easily as "you asked."
   → 「橋の上で、きみ、私に聞いたよね。」
4. **c3_0082** (Nanoha): 〜からと、〜から is ungrammatical, and the "only" is lost.
   → 「大したことじゃないよ。こっちに来たのは、テレビが大きいのと、外科医の先生がかっこいいから。それだけ。」
5. **c3_0075** (Akane): the TTS can read 十分 as じゅうぶん ("enough") instead of じゅっぷん ("ten minutes").
   → 「学校の帰りに、ちょっとふらっとしただけ。駅の階段で。じゅっぷんくらい座ってたら、治ったよ。」
6. **c3_0325** (Kirishima): the TTS may read 地稽古 as ちけいこ. Write the term in kana, as was done for めん in Ch2.
   → 「最後の三十分は、じげいこ。ふじさわ。みずの。」
7. **c3_0382** (Genji): a shrine's office is the 社務所. 事務所 sounds like a company office, which is wrong in a shrine keeper's mouth.
   → 「なのは。茶は社務所じゃ。みんなの分、湯のみも持ってきておくれ。」
8. **c3_0417** (Akane): this is her first meeting with an older girl, in someone else's house. Opening in plain form is too familiar; a polite opener goes with "-san." Her next line (c3_0419, ううん…) can stay casual, because slipping into casual as she warms up is natural.
   → 「なつきさん、ですよね？ お兄ちゃんから一本取ったって、聞きました！」

## Polish (naturalness, register, the joke)

9. **c3_0066** (Nanoha): 全部 doesn't fit people. Use 全員.
   → 「食べたよ。薬も飲んだ。医療ドラマを三話見て、出てくるお医者さん全員にダメ出ししてた。一人は逮捕されるべきだって。」
10. **c3_0081** (Akane): three だから in four lines, and "instead" is lost.
    → 「で、代わりに、なのはちゃんにメッセージしたの。すぐ来てくれたよ。写真も、ちゃんと送ったでしょ。二枚とも。」
11. **c3_0108** (Nanoha): 言えません is a plain "I can't say." "We don't discuss it" is mock-official, and it sets up her 権威 and 減刑 lines.
    → 「その件については、お答えできません。」
12. **c3_0116** (Nanoha): 権威を損なう is a stiff written collocation, and it drops the "you."
    → 「それは、私の権威を傷つける行為です。」 (c3_0117 still answers it.)
13. **c3_0330** (Kōhei): with no subject, a listener can take it as "*I* didn't get much."
    → 「そっちは、大して取れてなかったな。」
14. **c3_0354** (Kōhei): 足りるくらい is a slightly odd reply.
    → 「足りてる。」
15. **c3_0380** (Genji): お嬢さんがカメラの子か doubles up ("the young lady is the camera kid").
    → 「で、こちらがカメラのお嬢さんか。好きなだけ撮りなさい。木は気にせんよ。」
16. **c3_0270** (Natsuki): そろそろおいとまします and じゃあ、私はこれで both say "I'm leaving," and "intruded" is lost.
    → 「よし！ すっかりお邪魔しちゃいました。お茶、ごちそうさまでした。あと、木も。じゃあ、私はこれで。」
17. **c3_0407** (Kōhei): はいはい is an indulgent "yeah, yeah." "Yes, ma'am" plays along with her order, and this is his work register.
    → 「かしこまりました。」
18. **c3_0292** (Mio): のぞむところ is a grown-up, shōnen-manga phrase (§3b: she never sounds older than about 7).
    → 「ぜったい負けないもん！」
19. **c3_0285** (Emi): two わよ in a row.
    → 「お邪魔だなんて、とんでもない！ さあ、上がって、上がって。冷めちゃうわよ。あかねちゃんも、もう来てるから。」
20. **c3_0393** (Natsuki, new): she never took the shot, so the past tense いい写真じゃなかった is a little off ("it wasn't a good photo"). "Wouldn't make" fits better, and もん echoes her いい写真だもん (c3_0364).
    → 「いい写真にならないもん！ 花びら、多すぎ。」

## Lines changed during the pass (overcorrection fixes; current file)
- **c3_0333** 「たかつきくん！ どっちの味方なの？」 Natural, and casual to a classmate is right. Fine as written; see item 1 for how it interacts with Takatsuki's line.
- **c3_0348** 「進捗報告つきでね。」 Natural. Kōhei's 「ゴミ袋だぞ。」 still answers it cleanly. Fine.
- **c3_0364** 「やだ。いい写真だもん。」 Natural and playful; だもん suits the tease. It answers 消せ well. Fine.
- **c3_0392** 「さっき。写真、撮らなかったな。」 Natural for Kōhei: fragments, no お前, and さっき covers "back there." Fine.
- **c3_0393** 「いい写真じゃなかったの！ 花びら、多すぎ。」 Polish only (item 20). The いい写真 echo of c3_0364 is worth keeping.

## Listen on render
- **c3_0426** なつきねえ: this is Mio's first "-nee" for Natsuki, and it could be heard as "Natsuki, ねえ (hey)…". If the render splits it into two words, regenerate the line; don't change the §3c form.
- **c3_0382** 社務所 (once item 7 is applied): it should be read しゃむしょ.

## Checked and kept
- **c3_0072/0073** しゃがんでる means crouching, not kneeling, but the literal deadpan answer to 見張ってる works, and Akane's よそでしゃがんで echoes it.
- **c3_0363** 消せ is blunt, but he's flustered, and her new やだ (c3_0364) needs a command to refuse.
- **c3_0397** Nanoha says ひと休み twice where the English says it once. It's the formula, so it should match Genji's.

## Address and pronouns (§3c): no violations (apart from how item 1 sounds)
- Kōhei uses 俺, and お前 only to Nanoha (c3_0111, c3_0117). He never uses お前 to or about Natsuki, says bare あかね, is casual with Genji, and keeps おやすみ、チビ.
- Nanoha uses 私 and こうへい, with こうちゃん only at the window. She says なつきさん (c3_0271), あかねちゃん, おじいちゃん, お母さん, and never あなた.
- Natsuki uses 私, きみ only to Kōhei, a bare ふじさわ, なのは, りか, たかつきくん and みおちゃん, and is polite to Genji and Emi.
- Akane says お兄ちゃん, なのはちゃん and なつきさん. Mio refers to herself as みお and says こうにい and なつきねえ. Emi says こうへいくん. Genji uses bare names. Kirishima uses bare surnames. Takatsuki uses surnames and no "you."
- §3c plans no name changes for Ch3.

## Kendo (§5) and consistency with Ch1–2
- めん is in kana, 小手 and 一本 are right, and 地稽古 is the correct term (item 6 is only about the reading). Takatsuki's tell, めんを打つ前に…左肩が下がる, matches Kirishima's wording in c2_0153.
- These match the earlier chapters: お兄ちゃん、また見張ってるー (c1_0018), おやすみ、こうちゃん／おやすみ、チビ (c1_0255–0256), もう病気だね and 作りすぎ (c1_0034, c1_0032), 都合のいい腰 and 花びらの多い日だけ (c1_0095), 課題 and 「何が」 (c2_0241–0242), ゴミ袋, ……ほんとに？ (c1_0192), おばけ and 水曜. 進捗報告 is new and used the same way all three times.

## Consistently good
- **Nanoha** has the best Japanese in the chapter. The private bits land exactly: 反省中, 常習犯, 減刑です。模範囚なので, 「おかえり」には「ただいま」って返すものです. Her only real error is the grammar in item 4.
- **Kōhei** is terse, natural and correctly addressed throughout (……窓な, 買ってやったの、俺だろ). He needs polish only.
- **Emi and Mio** are natural and in character. Mio stays third-person and kid-blunt.
- **Genji** has a natural, easygoing old-man register (よう来た、よう来た, 都合のいい腰でな, ひと休み、ひと休み). His one wrong word is item 7.
- **Akane** has the right sibling voice. She needs only the TTS fix and the register on meeting Natsuki.
- **Natsuki** is strong where it matters most: the rice-planting story, やだ。いい写真だもん, どっちの味方なの, じゃあ、遠回りする. Two lines are ambiguous (items 2–3).
- **Takatsuki and Kirishima** have the right voices, but each has only one line, and both lines need a fix.
