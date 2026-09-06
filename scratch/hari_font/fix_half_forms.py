import re

# In 'વિશ્વભરમાં', 'શ્' is V. So 'શ્વ' = V+v. But wait, in actual it gave (vVvBrmi>.
# Ah! 'શ્' -> V, and 'વ' -> v. In Hari Gujarati mappings we have:
# { from: 'શ્', to: 'V' }
# If 'શ્' translates to 'V', then 'શ્વ' (શ્ + વ) translates to 'Vv'. But expected is 'VBrmi>' (wait, 'ભરમાં' is Brmi>).
# Did the competitor render 'શ્વ' as just 'V'?
# Let's check our actual output length vs expected.
# 'વિશ્વભરમાં' -> વ + િ (->(v) + શ + ્ + વ + ભ + ર + મ + ા + ં
# -> expected: (vVBrmi>
# So (v V B r m i >
# That means 'શ્વ' -> 'V' !!
# Let's verify 'વિશ્વ'. 
# V is a ligature for શ્વ!
