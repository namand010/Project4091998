import json

# file = "json_parsing"
# dic0 = {}
# with open(file, 'r') as fh:
#     for i in fh:
#         a, b = i.strip().split()
#         print(a, b)
#         dic0[a] = b
#
#     out = open("open.json", "w")
#     json.dump(dic0, out, indent=4, sort_keys=False)
#     out.close()

with open("open.json", "r") as th:
    out = json.loads(th.read())
    for i in out["glossary"]["GlossDiv"]["GlossList"]["GlossEntry"]["GlossDef"]["GlossSeeAlso"]:
        print(i)
    # print(out)
    th.close()