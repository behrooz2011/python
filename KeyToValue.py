def groups_per_user(group_dictionary):
  user_groups={}
  set1=set()
  for key,values in group_dictionary.items():
    for user in values:
      set1.add(user)
  print(set1)
  for item in set1:
    user_groups[item]=[]
    for key,values in group_dictionary.items():
      if item in values:
        
        user_groups[item].append(key)
  return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
    "public":  ["admin", "userB"],
    "administrator": ["admin"] }))
