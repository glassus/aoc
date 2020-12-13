
raw_data = open("input.txt").read().split('\n')
#raw_data = open("input_test.txt").read().split('\n')

timestamp = int(raw_data[0])

raw_bus_ids = raw_data[1].split(',')

bus_ids = [int(k) for k in raw_bus_ids if k != 'x']

  


waiting_time = {}
for bus_id in bus_ids:
    waiting_time[bus_id] = bus_id - timestamp % bus_id
    
bus_id_sorted = sorted(waiting_time.keys(), key = lambda x : waiting_time[x])
best_bus = bus_id_sorted[0]
sol = best_bus * waiting_time[best_bus]
print(sol)
