# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"

a = "The_Stealth_Warrior"
b = "the-stealth-warrior"
c = "the_stealth-warrior_xtreme-test"
d = "A-B-C"

# def to_camel_case(text):
#     tl = [t for t in text.replace("-"," ").replace("_"," ").split(" ")]
#     text_list = [t.title() for t in text.replace("-"," ").replace("_"," ").split(" ")]
#     text_list[0] = tl[0]
#     return ''.join(text_list)

def to_camel_case(s):
 	return s[0] + s.title().translate({95:45}).translate({45:None})[1:] if s else s


print(to_camel_case(""))




