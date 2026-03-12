#1.create dictionary with student details
student={"name":"swathi","age":21,"Percentage":89,"mail_id":"swathi123@gmail.com","ph_no":9834242675}
print(student)
#2.access dict value using key
student={"name":"swathi","age":21,"Percentage":89,"mail_id":"swathi123@gmail.com","ph_no":9834242675}
print(student["name"])
#3.add new key-value pair
student={"name":"swathi","age":21,"Percentage":89,"mail_id":"swathi123@gmail.com","ph_no":9834242675}
student["Mark_in_maths"]=90
print(student)
#4.update value
student={"name":"swathi","age":21,"Percentage":89,"mail_id":"swathi123@gmail.com","ph_no":9834242675,"Mark_in_maths":90}
student["Mark_in_maths"]=95
print(student)
#5.delete key from dictionary
del student["age"]
print(student)
#6.print all keys in dictionary
print(student.keys())
#7.print all keys in dictionary
print(student.values())
#8.print key-value pairs
print(student.items())
#9.check whether key exists in dictionary
student={"name":"swathi","age":21,"Percentage":89,"mail_id":"swathi123@gmail.com","ph_no":9834242675,"Mark_in_maths":90}
if "age" in student:
    print("key already exists")
else:
    print("key not exists")
#10.count number of items in dictionary
print(len(student))
#11.count number of items in dictionary
dict1={"a":1,"b":2,"c":3,"d":4,"e":5}
dict2={"f":6,"g":7,"h":8,"i":9,"j":10}
dict1.update(dict2)
print(dict1)
#12.create dictionary from two lists
keys=["name","ph_no","age"]
values=["Saro",7811813761,21]
new_dict=dict(zip(keys,values))
print(new_dict)
#13.sort dictionary by keys
marks={"Tam":98,"Eng":97,"Mat":99,"Sci":89,"Soc":80}
print(sorted(marks.keys()))
#14.sort dictionary by values
marks={"Tam":98,"Eng":97,"Mat":99,"Sci":89,"Soc":80}
print(sorted(marks.values()))
#15.find maximum value in dictionary
marks={"Tam":98,"Eng":97,"Mat":99,"Sci":89,"Soc":80}
print(max(marks.values()))
#16.find minimum value in dictionary
marks={"Tam":98,"Eng":97,"Mat":99,"Sci":89,"Soc":80}
print(min(marks.values()))
#17.remove duplicate values from dictionary
d = {"a":"Ram", "b":"Ravi", "c":"Renu","d":"Rajesh","e":"Ravi"}
new_dict = {}
for i in d:
    if d[i] not in new_dict.values():
        new_dict[i] = d[i]
print(new_dict)
#18.print dictionary in reverse order
Dict = {"a":36, "b":42, "c":93}
for i in reversed(Dict):
    print(i,Dict[i])
#19.create dictionary using loop
d = {}
for i in range(1,6):
    d[i] = i * i
print(d)
#20.count frequency of characters using dictionary
text = "Welcome everyone"
new_text= {}
for ch in text:
    new_text[ch] = text.count(ch)
print(new_text)
#21.convert dictionary keys into list
dictionary = {"a":1, "b":2, "c":3}
new_list = list(dictionary.keys())
print(new_list)
#22.convert dictionary values into list
dictionary = {"a":1, "b":2, "c":3}
new_list = list(dictionary.values())
print(new_list)
#23.check whether dictionary is empty
d = {}
if len(d) == 0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")
#24.copy dictionary
d1 = {"a":1, "b":2, "c":3}
d2 = d1.copy()
print(d2)
#25.clear dictionary
d1 = {"a":51, "b":72, "c":63}
d1.clear()
print(d1)






