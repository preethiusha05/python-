colours = ["red", "green", "yellow", "blue"]
things = ["house", "car", "tree"]
coloured_things = [(c, t) for c in colours for t in things]
print("\nAll Combinations (Tuple Format):")
for item in coloured_things:
    print(item)
sentences = [c + " " + t for c, t in coloured_things]
print("\nSentence Format:")
for s in sentences:
    print(s)
filtered = [(c, t)
            for c, t in coloured_things
            if c == "blue" or t == "car"]
print("\nFiltered Combinations (blue or car):")
print(filtered)
total_combinations = len(coloured_things)
print("\nTotal Combinations:", total_combinations)
grouped = {
    colour: [thing for c, thing in coloured_things if c == colour]
    for colour in colours
}
print("\nGrouped by Colour:")
for key, value in grouped.items():
    print(key, ":", value)
print("\nNumbered Combinations:")
for i, item in enumerate(coloured_things, start=1):
    print(i, "->", item)
