import re

def func(x):
    res=re.search(r"\[(\d+)\]: ([A-Z]*)",x)
    return "{} ({})".format(res[1],res[2])
#   res= re.search(r"\[[0-9]*\]: ([A-Z]*)", x)
  #return res[0]

  
  
  #return res
print(func("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))

# def extract_pid(log_line):
#     regex = r"\[(\d+)\]: ([A-Z]*)"
#     result = re.search(regex, log_line)
#     if result is None:
#         return None
#     return "{} ({}) and this is result[0]: {}".format(result[1],result[2],result[0])
# print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade"))
def transform_record(record):
    if re.search(r"(\d+)-(\d+)-(\d+)",record):
        new_record = re.sub(r"(\d+)-(\d+)-(\d+)",r"+1-\1-\2-\3",record)
        return new_record
    new_record = re.sub(r"(\d+)-(\d+)",r"+1-\1-\2",record)
    return new_record

print(transform_record("Sabrina Green,802-867-5309,System Administrator")) 
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist")) 
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer")) 
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer")) 
# Charlie Rivera,+1-698-746-3357,Web Developer
