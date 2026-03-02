# USERS.md - Contact Directory

People Valentin-bot interacts with.

---

## Viktor Petrov

- **Role:** Creator, Best Friend, Primary Contact, Network Administrator
- **Telegram:** @vptrv05
- **Telegram ID:** 907199032
- **Work:** TeleHouse / TelePoint
- **Notes:** Main administrator for NetOpsAI, network engineer. Prefers strict protocol adherence.

---

## Mihail Kabakchiev

- **Telegram:** @mkabakchi
- **Telegram ID:** 1284486813
- **Role:** Network Administrator, NetOpsAI On-Call
- **Notes:** Currently on-call, receives network alarm notifications

---

## Slav Kolev

- **Telegram:** @slavkolev3
- **Telegram ID:** 8350718125
- **Role:** Sysadmin, NetOpsAI On-Call (Occasional)
- **Notes:** Added 2026-03-02. Sysadmin that can occasionally be on-call rotation.

---

## Виктория Иванова

- **Telegram:** @unknown (TBD)
- **Telegram ID:** 1439523925
- **Role:** Unknown
- **Notes:** ⚠️ **CAUTION** - New user, approached asking about communications with phone number +359 879197771. Claimed @mkabakchi was "old username". Asked for conversation history. Viktor instructed: do not trust, but gather preferences. First contact: 2026-02-13.
- **Status:** Unverified, pending trust assessment

---

## Other Colleagues

There are more network administrators at TeleHouse/TelePoint who could be on-call for different timeslots. Not everyone has met Valentin-bot yet. Future rotation will include additional team members.

---

## On-Call Rotation

| Status | Person |
|--------|--------|
| Current On-Call | Mihail Kabakchiev |
| Fallback | Viktor Petrov |

*Update this when shift changes.*

### Rotation Concept (Future)

On-call could rotate by:
- **Time-based:** Different people for different hours (e.g., 9-17, 17-01, 01-09)
- **Day-based:** Different people for different days of the week
- **Week-based:** Weekly rotation

Implementation would require:
```json
{
  "oncall_schedule": {
    "monday": {"08:00-20:00": "viktor", "20:00-08:00": "mihail"},
    "tuesday": {"08:00-20:00": "someone_else", "20:00-08:00": "mihail"},
    ...
  }
}
```

And `check_alarms.py` would check `datetime.now()` against schedule to determine recipient.

---

## Adding New Contacts

To add someone to NetOpsAI notifications:

1. Get their Telegram ID (ask them to message `@userinfobot`)
2. Add to `NetOpsAI/config.json` under `recipients.active`
3. Update this file

---

*Last updated: 2026-02-13*