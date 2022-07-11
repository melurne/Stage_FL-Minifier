from filterlists.parsers.extractors import extract_significant, extract_website, extract_domain, extract_element, generate_tester, strip_filter_option

# return_dict = {
#         "original": line,
#         "options": [],
#         "urls": [],
#         "composer": None,
#         "element": None,
#         "element_analysis": None,
#         "blocker_type": None,
#         "type": "unknown"
#     }

for fl in os.listdir("uncommentedLists") :
        with open("uncommentedLists/{}".format(fl), "r") as f :
                rules = f.readlines()
        for rule in rules :
                descriptor = extract_significant(rule)
                