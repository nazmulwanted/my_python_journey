bd_division_info = {}

bd_division_info["Barishal"] = {"District": 6,"Upazilla": 39,"Council":333}
bd_division_info["Chittagong"] = {"District": 11,"Upazilla": 97,"Council": 336}
bd_division_info["Dhaka"] = {"District": 13,"Upazilla": 93,"Council":1833}
bd_division_info["Khulna"] = {"District": 10,"Upazilla": 59,"Council":270}
bd_division_info["Mymensingh"] = {"District": 4,"Upazilla": 34,"Council":350}
bd_division_info["Rajshahi"] = {"District": 8,"Upazilla": 70,"Council":558}
bd_division_info["Rangpur"] = {"District": 8,"Upazilla": 58,"Council":536}
bd_division_info["Sylhet"] = {"District": 4,"Upazilla": 38,"Council":334}

divisions = bd_division_info.keys()
print(divisions)
for division in divisions:
    print("Division",division,"Upazilla",bd_division_info[division]["Upazilla"])
for key in bd_division_info:
    print(key)
    print(bd_division_info[key])
for key,value in bd_division_info.items():
    print(key)
    print(value)

district = 0
upazilla = 0
union = 0

for key in bd_division_info:
    district += bd_division_info[key]["District"]
    upazilla += bd_division_info[key]["Upazilla"]
    union += bd_division_info[key]["Council"]
print("Total district = ",district)
print("Total upazilla = ",upazilla)
print("Total union = ",union)
