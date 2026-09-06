txt = "શિક્ષણ અને વિજ્ઞાનના ક્ષેત્રમાં પણ ગુજરાતે ખૂબ પ્રગતિ કરી છે."
expected = "(SxN an[ (vXinni x[#imi> pN g&jrit[ K*b p\\g(t kr) C[."

# let's map word by word
txt_words = txt.split()
exp_words = expected.split()

for t, e in zip(txt_words, exp_words):
    print(f"{t} -> {e}")
