import os
import json
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument("--n", type=int)

args = parser.parse_args()

end = (math.floor(args.n / 700) + 1) * 700

data_dict = {}

with open("Bool_NER_data.json", "r") as f:
    total_data = json.load(f)

key_list = list(total_data)
key_list.sort()

now = args.n
chars_per_line = 80
count= args.n

for key in key_list[args.n:end]:
    print(count)
    count+=1
    
    data_i = total_data[key]

    for i in range(0, len(data_i['text']), chars_per_line):
      print(data_i['text'][i:i+chars_per_line])
    print()

    print(data_i['q'])
    print()

    text_ner = list(set(data_i['text_ner']))
    q_ner = list(set(data_i['q_ner']))

    tmp_dict = {}
    q_list = "   ".join([str(idx) + " : " + q_ner[idx] for idx in range(len(q_ner))])
    print(q_list)
    print()

    for idx in range(len(text_ner)):
        print(text_ner[idx] + " : ", end="")
        n = input()

        if n == 'q':
            tmp_dict[text_ner[idx]] = -1

        elif n not in ['0','1','2','3','4','5','6','7','8','9','10','11','12']:
          print(text_ner[idx] + " : ", end="")
          n = input()
          if n == 'q':
            tmp_dict[text_ner[idx]] = -1
          elif n not in ['0','1','2','3','4','5','6','7','8','9','10','11','12']:
            break
          else:
            tmp_dict[text_ner[idx]] = int(n)

        else:
            tmp_dict[text_ner[idx]] = int(n)

    data_dict[key] = tmp_dict

    print("save file?", end=" ")
    s = input()

    now += 1

    if s == "y":
        break
    
    print()
    print()
    print()


print("Save", str(args.n), "-", str(now))

with open("dict" + str(args.n) + "_" + str(now) + ".json", "w") as f:
    json.dump(data_dict, f, indent=4, ensure_ascii=False)
