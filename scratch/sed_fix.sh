#!/bin/bash
sed -i "s/'ఘ': { full: '\\\\u0153\\\\u00E8', base: '\\\\u0153', vattu: '\\\\u0192'/'ఘ': { full: '\\\\u005A\\\\u00E8', base: '\\\\u005A', vattu: '\\\\u005E'/" src/utils/mappings/shreeLipiTelugu0908.ts
sed -i "s/'ఙ': { full: '\\\\u005C', base: '\\\\u005C', vattu: ']'/'ఙ': { full: '\\\\u005C', base: '\\\\u005C', vattu: '\\\\u005D'/" src/utils/mappings/shreeLipiTelugu0908.ts
sed -i "s/'మ': { full: '\\\\u02DC', base: '\\\\u02DC', vattu: '\\\\u00C3'/'మ': { full: '\\\\u00AC', base: '\\\\u00AC', vattu: '\\\\u00C2'/" src/utils/mappings/shreeLipiTelugu0908.ts
sed -i "s/'హ': { full: '\\\\u00E0', base: '\\\\u00DF', vattu: '\\\\u00E1'/'హ': { full: '\\\\u00E0', base: '\\\\u00DF', vattu: '\\\\u00E1'/" src/utils/mappings/shreeLipiTelugu0908.ts
