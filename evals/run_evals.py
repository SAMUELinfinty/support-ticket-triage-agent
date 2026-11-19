import json, sys
sys.path.append("src")
from triage import triage

tickets = json.load(open("evals/tickets.json"))
correct, failures = 0, []

for t in tickets:
    try:
        result = triage(t["ticket"])
        if result["category"] == t["category"]:
            correct += 1
        else:
            failures.append((t["ticket"], t["category"], result["category"]))
    except Exception as e:
        failures.append((t["ticket"], t["category"], f"ERROR: {e}"))

print(f"Accuracy: {correct}/{len(tickets)} = {correct/len(tickets):.0%}")
for f in failures:
    print("MISS:", f)