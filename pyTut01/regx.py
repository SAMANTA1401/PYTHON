import re

mystr = '''MENA
Resident Director, Tata Sons
Representative Office DMCC Branch
2001 to 2005, 20th Floor
Jumeirah Bay X-3 Tower
Cluster X, JLT, P.O Box 120933
Dubai, United Arab Emirates
Email: info@tata.com
Site: www.tata.com/mena

EuropeEurope
Resident Director, Tata Limited
18, Grosvenor Place
London SW1X 7HSc
Phone:+44 (20) 7235 8281
Fax:+44 (20) 7235 8727
Email: tata@tata.co.uk
Site: www.tata.com

North AmericaNorth America
Resident Director, Tata Sons
North America
1700 North Moore St,Suite 1520,
Arlington, VA 22209-1911
Phone:+1 (703) 243 9787
Fax:+1 (703) 243 9791
Email: northamerica@tata.com
Site: www.tata.com'''

# findall, search, split, sub, finditer
# [] a set of charecters
# \ signal a special sequence
# . any charecter(except new line charecter)
# ^ start with
# $ Ends with
# * Zero or more occurances
# + one or more occurances
# {} Exactly the specified number of occurences
# | Either or
# () Capture and group

# special sequences:
# \A return a match if the specified charecters are the beginning of the string
# \b return a match where the specified charecters are at the beginning or at the end of a word
# r"ain\b"
# \B returns a match where the specified charecters arer present but not at athe beginning (or ata the end) of a word

# patt = re.compile(r'Moore')
patt = re.compile(r'^Tata')
patt = re.compile(r'iin$')
patt = re.compile(r'ai*')
patt = re.compile(r'ai{2}|t')
patt = re.compile(r'27\b')
patt = re.compile(r'\d{5}-\d{4}')

# +91 10 digit

matches = patt.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[446:452])
