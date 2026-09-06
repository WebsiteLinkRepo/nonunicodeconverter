# FAILED Ka Family: Expected `±y`, got `k`y`.
# `±y` is `ક્ય`. But `k`y` is `ક` (k) + `્` (`) + `ય` (y).
# So `ક` + `્` + `ય` should map to `±y`. 
# Wait, let's just map `ક્ય` -> `±y` instead of letting `ક્` -> `k\``. Oh, I removed `ક્ય` -> `±y` in the last edit? Let me check.

# FAILED Conjuncts: Expected `à`, got `A#`.
# Expected is `સ્ત્ર` -> `à`.
# Actual generated `A#`. A is `સ્`, `#` is `ત્ર`.
# Our mappings have `સ્ત્ર` -> `à` but if `સ્` (સ + ્ = A) runs first, it becomes A + ત્ર -> A#.
# The mapping order matters! Ligatures/conjuncts with multiple characters (like સ્ત્ર, ક્ય) must be processed before single half characters (like સ્, ક્)!
