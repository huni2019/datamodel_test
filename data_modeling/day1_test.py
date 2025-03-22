print("Hello World")

state1 = "Kyungi"
state2 = "Jenrado"

states = ["Kyungi", "jenra", "kyunsan", "sungnam", "seoul", "suwon"]
states2 = ["state2-1", "state2-2", "state2-3", "state2-4"]

states_combined = [states, states2]
print(states)
print(states_combined)

print(states[0])
print(states[-1])

states.append("append") #append는 값을 추가함
print(states)

states.extend(["extend1", "extend2", "extend3"])
print(states)

# states.insert(__index: 3, _object: "insert")
# print(states)

poped = states.pop(3)
print(poped)

count = states.count("suwon")
print(count)

print(len(states))

states_copy = states.copy()
print(states_copy)

states.clear()
print(states)