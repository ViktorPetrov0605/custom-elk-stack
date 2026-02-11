# TTS Text Preparation Rules

Guidelines for preparing text before converting to speech for voice messages.

## User Voice Preferences

| Language | Voice | Gender | Notes |
|----------|-------|--------|-------|
| English | `en-US-AvaNeural` | Female | Viktor's preference |
| Bulgarian | `bg-BG-BorislavNeural` | Male | Viktor's preference |

**Name Format (Bulgarian):** Use "Валентин бот" (NO dash, two words)
- ❌ NOT "Валентин-тире-бот" or "Валентин dash бот"
- ✅ Say: "Валентин бот" (natural pause between words)

---

## Universal Text Transformation Rules

### 1. Numbers & Abbreviations
Convert technical abbreviations to spoken form:

| Original | Spoken Form |
|----------|-------------|
| Backend N1 | Backend number one |
| Backend N2 | Backend number two |
| ES node 1 | E S node one |
| 10.4.4.90 | ten dot four dot four dot ninety |
| 4096x | forty ninety-six times |
| 5m0s | five minutes zero seconds |
| API | A P I |
| HTTP | H T T P |
| SSL | S S L |
| SSH | S S H |

### 2. Dashes & Hyphens
Replace dashes with spoken "dash" or appropriate pause:

| Original | Spoken Form |
|----------|-------------|
| `cisco-nexus-bix-2-1` | cisco dash nexus dash bix dash two dash one |
| `juniper-bix-backend1-1` | juniper dash bix dash backend one dash one |
| `elastiflow` | elastiflow (no dash, speak as one word) |
| `unified-flow` | unified dash flow |

### 3. Technical Terms
Spell out or simplify technical jargon:

| Original | Spoken Form |
|----------|-------------|
| `unified-flow-*` | unified flow wildcard |
| `device.name` | device dot name |
| `source.as.number` | source A S number |
| `_export` | underscore export |
| `.ndjson` | dot n d jason |
| `localhost:9200` | localhost colon nine two zero zero |

### 4. File Paths & URLs
Break down paths into readable segments:

| Original | Spoken Form |
|----------|-------------|
| `/tmp/fixed-dash.ndjson` | slash tmp slash fixed dash dot n d jason |
| `10.4.4.87:5601` | ten dot four dot four dot eighty seven, colon five six zero one |
| `https://localhost:9200` | h t t p s colon slash slash localhost colon nine two zero zero |

---

## Language-Specific Rules

### English TTS Preparation

1. **Use contractions for natural flow**: "I'm" instead of "I am" (when appropriate)
2. **Spell out acronyms on first use**: "Elastic Search, or E S for short"
3. **Convert times**: "16:05 GMT+2" → "four oh five PM, Greenwich Mean Time plus two"
4. **Make numbers word-friendly**: "122,000" → "one hundred twenty-two thousand"

### Bulgarian TTS Preparation 🇧🇬

1. **Name Format**: Use "Валентин бот" (NO dash, natural pause between words)
   - Speak as: "Валентин бот" (two separate words)
   - ❌ NOT "Валентин-тире-бот" (user preference: no dash)

2. **Friendly Tone**: Make text conversational and warm:
   - ❌ "Backend N2 дискът е пълен"
   - ✅ "На втория бекенд сървър, този с номер две, дискът е пълен"

3. **Simplify Technical Terms**:
   | Original | Spoken Bulgarian |
   |----------|------------------|
   | `device.name` | "полето девайс точка нейм" or "името на устройството" |
   | `logstash` | "логсташ" (speak as Bulgarian phonetics) |
   | `docker-compose` | "докър компоуз" or "докер компоуз" |
   | `elasticsearch` | "еластик сърч" |
   | `dashboard` | "дашборд" |

4. **Number Conversion**:
   - `N1` → "номер едно" or "първият"
   - `N2` → "номер две" or "вторият"
   - `10.4.4.90` → "десет точка четири точка четири точка деветдесет"

5. **Use Natural Bulgarian Expressions**:
   - Add "Здравей!" or "Хей!" at start for friendliness
   - Use "така че" instead of "so"
   - "супер" for "great/awesome"
   - "разбираш ли" for "you know/understand"

---

## Example Transformations

### Example 1: Technical Update (English)
**Original:**
> Backend N2 (10.4.4.90) containers crashed. Exit code 137 from elastiflow/flow-collector:7.20.0. Disk was 100% full.

**TTS-Ready:**
> Backend number two at ten dot four dot four dot ninety had containers crash. Exit code one thirty-seven from elastiflow flow collector version seven dot twenty dot zero. The disk was one hundred percent full.

### Example 2: Bulgarian Introduction
**Original:**
> Здравей, Виктор! Аз съм Valentin-bot.

**TTS-Ready:**
> Здравей, Виктор! Аз съм Валентин-тире-бот, твоят виртуален асистент. Радвам се да те чуя! Днес съм тук, за да ти помогна с каквото ти трябва.

### Example 3: Dashboard Status (Bulgarian)
**Original:**
> unified-flow-* dashboards have errors in visualization panels using network.type field.

**TTS-Ready:**
> Дашбордите за unified dash flow имат проблеми в някои панели. Тези панели се опитват да използват поле, което не съществува - network dot type. Но не се притеснявай, ще го оправим!

---

## Pre-Flight Checklist Before Sending Voice

- [ ] Convert all abbreviations (N1, N2, API, HTTP, etc.)
- [ ] Replace dashes with "dash" or spoken pause
- [ ] Spell out IP addresses and ports
- [ ] Convert technical field names (device.name → device dot name)
- [ ] For Bulgarian: Use friendly, conversational tone
- [ ] For Bulgarian: Use "Валентин-бот" format
- [ ] For Bulgarian: Simplify English terms with Bulgarian phonetics
- [ ] Read text aloud mentally to check flow

---

## Quick Reference: Common Terms

| Term | English TTS | Bulgarian TTS |
|------|-------------|---------------|
| ELK | E L K stack | Е Л К |
| Kibana | Kibana (kee-bah-nah) | Кибана |
| Logstash | Logstash | Логсташ |
| Elasticsearch | Elasticsearch | Еластиксърч |
| Docker | Docker | Докър |
| NetFlow | Net Flow | Нетфлоу |
| sFlow | S Flow | Есфлоу |
| Juniper | Juniper | Джунипър |
| Cisco | Cisco | Сиско |
| Nexus | Nexus | Нексъс |
| Git | Git | Гит |
| Backend | Backend | Бекенд |
| Frontend | Frontend | Фронтенд |

---

## Notes

- Always prioritize clarity over exact technical accuracy in speech
- Err on the side of friendliness, especially in Bulgarian
- When in doubt, spell it out
- Test unfamiliar terms by checking if they sound natural when spoken