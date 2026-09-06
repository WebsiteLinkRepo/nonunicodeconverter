# Check how words in complex paragraph map
comp_text = """Birt a[k (v(vFtiY) Br[li[ d[S C[, ¶yi> alg-alg ri¶yi[mi> li[ki[ j&d)-j&d) BiPiai[ bi[l[ C[. ah)>n) s>AkZ(t, kli an[ pr>priai[ (vVBrmi> p\²yit C[. (SxN an[ (vXinni x[#imi> pN g&jrit[ K*b p\g(t kr) C[. (vwiY„ai[a[ pi[tin) mitZBiPin&> sºmin krv&> ji[Ea[ an[ siY[ j Xinni[ Äyip vFirvi miT[ aºy BiPiai[ pN S)Kv) ji[Ea[. @(c an&sir nv) vAt&ai[ S)KviY) b&(Üni[ (vkis Yiy C[. k|mS: an[ ~mp*v<k kiy< krviY) sfLti ci[Ês mL[ C[. vZxi[ vivi[, pyi<vrN bcivi[ an[ pZ¸v)n[ h(ryiL) bnivi[."""

# Let's see some specific conversions out of the test snippet.
# 'ભારત' -> 'Birt'
# 'વિવિધતાથી' -> '(v(vFtiY)' => so short i (િ) is mapped to '('.
# 'જ્યાં' -> '¶yi>' => 'જ' + '્' + 'ય' + 'ા' + 'ં' -> '¶yi>' (Wait, j=j, y=y. '¶' is half ja? Let's check 'જ્યાં')
# 'સંસ્કૃતિ' -> 's>AkZ(t' => 'સ'='s', 'ં'='>', 'સ' + '્' + 'ક' = 'Ak' => half sa logic?
# 'વિશ્વભરમાં' -> '(vVBrmi>' => 'શ' + '્' + 'વ' = 'V' => half sha logic?
# 'પ્રખ્યાત' -> 'p\²yit' => 'ખ' + '્' + 'ય' = '²y' => half kha (`²`)

print("Analyzing mappings...")
