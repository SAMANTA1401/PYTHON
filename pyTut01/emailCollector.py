import re

str = """
ChinaChina
Resident Director, Tata Sons,
Tata group Beijing Office
Suite 10A, Tower A, Gateway Plaza
18 Xiaguangli, East 3rd Ring North Road, Chaoyang District
Beijing 100027, China
Phone:+86 (10) 8441 7530, +86 (10) 8441 7532
Email: tatachina@tata.com
Site: www.tata.com


Contact us
SingaporeASEAN
Resident Director, Tata Sons,
Singapore
78 Shenton Way, #17-01/02
Singapore 079120
Phone:+65 6220 9187
Fax:+65 62262130
Email: aseaninfo@tata.com
Site: www.tata.com


Contact us
IndiaIndia
Tata Sons,
Bombay House
24, Homi Mody Street
Mumbai 400 001
Phone:+91 (22) 6665 8282
Fax:+91 (22) 6665 8080
Email: info@tata.com
Site: www.tata.com


Contact us
MENAMENA
Resident Director, Tata Sons
Representative Office DMCC Branch
2001 to 2005, 20th Floor
Jumeirah Bay X-3 Tower
Cluster X, JLT, P.O Box 120933
Dubai, United Arab Emirates
Email: info@tata.com
Site: www.tata.com/mena


Contact us
EuropeEurope
Resident Director, Tata Limited
18, Grosvenor Place
London SW1X 7HSc
Phone:+44 (20) 7235 8281
Fax:+44 (20) 7235 8727
Email: tata@tata.co.uk
Site: www.tata.com


Contact us
North AmericaNorth America
Resident Director, Tata Sons
North America
1700 North Moore St,Suite 1520,
Arlington, VA 22209-1911
Phone:+1 (703) 243 9787
Fax:+1 (703) 243 9791
Email: northamerica@tata.com
Site: www.tata.com
"""

email = re.findall(r"[0-9a-zA-Z._+%]+@[0-9a-zA-Z._+%]+[.][a-zA-Z.0-9]+",str)
print(email)