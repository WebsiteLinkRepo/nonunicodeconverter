with open('src/utils/mappings/neo.ts', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Remove duplicate entries at the END that are already defined earlier  
# The appended block has duplicates of 'द', 'र्' etc.
# We want to KEEP the appended overrides (they have correct values)
# and REMOVE the originals from map_dict

# Actually, in JS objects, the LAST definition wins. 
# So duplicates are OK - the last one overrides.
# But let's clean up anyway for clarity.

# The important thing is: do we have the right final values?
# Let me just verify the final state
seen = {}
for i, line in enumerate(lines):
    line_stripped = line.strip()
    if line_stripped.startswith("'") and ":" in line_stripped:
        key = line_stripped.split(":")[0].strip()
        seen[key] = (i+1, line_stripped)

for key, (lineno, val) in sorted(seen.items(), key=lambda x: x[1][0]):
    if key in ["'द'", "'द्'", "'र्'", "'प्र'", "'्'", "'्र'"]:
        print(f"Line {lineno}: {val}")

