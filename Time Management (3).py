def find_common_meeting_slots(participants):
    common_slots = participants[0]
    for participant in participants[1:]:
        common_slots = [(max(s[0], p[0]), min(s[1], p[1]))
                        for s in common_slots for p in participant
                        if s[1] > p[0] and s[0] < p[1]]
    return common_slots

participants = [
    [(4, 16), (18, 25)],
    [(2, 14), (17, 24)],
    [(6, 8), (12, 20)],
    [(10, 22)]
]

common_slots = find_common_meeting_slots(participants)

if common_slots:
    print("Common meeting time slots:")
    for s in common_slots:
        print(f"{s[0]} - {s[1]}")
else:
    print("No common meeting time slots found.")