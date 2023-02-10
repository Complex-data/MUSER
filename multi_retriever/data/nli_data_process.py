import json


def generate_doc(c,e,l,p):
    f_write_doc = open('allnli/'+p+'.jsonl', 'a', encoding='utf-8')
    djson = {"statement": c, "evidence": e, "label": l,"source": p}
    jStr = json.dumps(djson, ensure_ascii=False)
    f_write_doc.write(jStr + "\n")
    f_write_doc.close()

platform = "gossipcop"
# platform = "politifact"
# platform = "weibo"
f_r_c_e = open('en/'+platform+'_evidences_claims.txt', 'r', encoding='utf-8')
f_r_label = open('en/'+platform+'_id_label.tsv', 'r', encoding='utf-8')

all_label = []

for line in f_r_label:
    label = line.strip("\n").split("\t")[1]
    all_label.append(label)

idx = 0
for line in f_r_c_e:
    line = line.strip("\n").split("\t")
    claim = line[0]
    evidence = line[1]
    label = all_label[idx]
    idx = idx+1
    generate_doc(claim, evidence, label,platform)
f_r_c_e.close()
f_r_label.close()