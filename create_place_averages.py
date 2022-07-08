import csv
import numpy as np

run_avgs = np.zeros((2000, 2000))
run_cnts = np.zeros((2000, 2000))

with open("2022_place_canvas_history.csv") as f:
    csv_reader = csv.reader(f, delimiter=',')
    start = True
    for row in csv_reader:
        if start:
            start = False
            continue
        color = int(row[2][1:], 16)
        coords = list(map(lambda x: int(x), row[3].split(",")))

        cur_avg = run_avgs[coords[0], coords[1]]
        cur_cnt = run_cnts[coords[0], coords[1]]
        run_avgs[coords[0], coords[1]] = (cur_avg * cur_cnt + color) / (cur_cnt + 1)
        run_cnts[coords[0], coords[1]] += 1

np.save("averages.npy", run_avgs)