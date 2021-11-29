import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--task", type=str, required=True)

args = parser.parse_args()

file_name = args.task + "_result.log"
metric = "score" if args.task == "CoLA" else "acc"

lines = []

with open(file_name, "r") as f:
    for line in f:
        lines.append(line.strip())

results = []
total = 0
target = 0

best = -1
lr = -1
bs = -1
cur_step = -1
best_step = -1

for line in lines:
    if line == "***** Running training *****":
        if best == -1:
            pass
        else:
            results.append((bs, lr, best, best_step))
            bs = -1
            lr = -1
            best = -1
        
    if "learning_rate" in line:
        lr = float(line[16:])

    if "Total train batch size" in line:
        bs = int(line[25:])

    if "Running evaluation on dev dataset" in line:
        cur_step = int(line[41:-12])

    if metric + " = " in line:
        score = float(line.split()[2])

        if score > best:
            best_step = cur_step
            best = score

results.append((bs, lr, best, best_step))

results.sort(key=lambda x: -x[2])

for result_i in results:
    print(result_i)
