# Let me look at what the Kruti Dev converter maps for each failing conjunct
# and compare with what bytes in NeoGanesh might correspond

# From Kruti Dev converter (unicodeToKrutidev):
# द्द → í (byte 237)
# द्य → | (byte 124)
# श्र → J (byte 74)
# क्ष → Õ (byte 213)
# ज्ञ → T (byte 84) -- Wait, T is also used for ज in Kruti
# त्र → = (byte 61)
# प्र → ç (byte 231)
# क्र → d (byte 100) -- Wait, that's also used for क
# Reph → Z (byte 90) placed AFTER consonant+matras

# The KEY insight is: in Kruti Dev, the reph is represented by "Z" 
# placed AFTER the consonant and matras. The mapping table handles 
# this in the REVERSE direction.

# For NeoGanesh, I need to find:
# 1. What byte is the Reph glyph?
# 2. What byte is द्द?

# From chart3.png I can see:
# 220: र̄ (this small r on top = Reph!)
# Let me verify by looking at the row

# Row in chart3.png: 
# 209: ष  210: ह  ...
# Let me look at the row with 220
# 219: ह्र  220: र̄  (YES! This is the Reph!)

# For द्द, I need to find it in the charts
# From chart2.png, row starting ~141:
# 141: ग्र  142: ?  143: द्र  144: क्त्र

# Let me check what गlyph 183 actually is
# In chart2.png or chart3.png

# 183 is in the range 181-190
# Chart3 row: 181: ह्ल  182: =  183: द्र  184: ळ  185: [
# So 183 IS द्र, NOT द्द! That's why उद्देश्य shows उद्रेश्य

# Now where is द्द?
# From chart3: 231: द्र... no
# Let me look at 233: द्ध  234: द्ध

# Actually from chart3.png I can clearly read:
# 231:  (something)  232: द्र  233: द्ध  234: द्ध
# No wait, those are in the 230s range

# Let me check 240-255 range in chart3.png:
# 240: त्त  241: ग्र  242: ढ  243: fˆ  244: क्त  245: ˘
# 246: चा  247: हु  248: ˘˘  249: ग्ल  250: ˙
# 251: द्ध  252: द्र  253: fˆ  254:    255: 

# So: 251 = द्ध, NOT द्द! And 252 = द्र

# Hmm, where is द्द then?
# From chart3.png: 
# Row 231-240:
# 231: I  232: द्र  233: द्ध  234: द्ध  235: ी  236: ु  237: ु̃  238: ू̃  239: ँ  240: त्त

# Wait I'm confused. Let me look at the ACTUAL entries in chart3.png more carefully
# The rows are:
# Row 1: 231: I  232: द्र  233: द्ध  234: द्ध  235: ˘ी  236:  237:  238:  239:  240: त्त

print("Need to look at charts more carefully for द्द")
print("Current mappings that are WRONG:")
print("  र् (Reph) → 124 (half-Ra) — should be the flying reph glyph") 
print("  द्द → 183 — but 183 is actually द्र in the font!")
print("")
print("From chart analysis:")
print("  220 = flying Reph (र̄)")
print("  183 = द्र (NOT द्द!)")
print("  252 = also द्र")
