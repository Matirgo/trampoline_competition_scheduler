# test_competitor.py
from classes.competitor import Competitor, TrampolineLevel

# Create competitors
alice = Competitor("Alice", "Johnson", True)
bob = Competitor("Bob", "Smith", False)
carol = Competitor("Carol", "Davis", True)

# Use a simple list to manage competitors
competitors = []

# Test adding
print(f"Start: {len(competitors)} competitors")

competitors.append(alice)
print(f"After adding Alice: {len(competitors)} competitors")

competitors.append(bob)
print(f"After adding Bob: {len(competitors)} competitors")

competitors.append(carol)
print(f"After adding Carol: {len(competitors)} competitors")

# Test removing
competitors.remove(bob)
competitors.remove(alice)
competitors.remove(carol)
print(f"After removing competitors: {len(competitors)} competitors")

# Show who's left
print("\nRemaining competitors:")
for competitor in competitors:
    print(f"- {competitor.first_name} {competitor.sur_name}")