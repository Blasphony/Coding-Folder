x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

def Change_value(x,y=None):
    x[1][0]= y
Change_value(x,15)
print(x)

def Change_name(students, name=None):
    students[0]["last_name"]=name
Change_name(students,'Bryant')
print(students)

def Change_sports_name(sports_directory, name=None):
    sports_directory["soccer"][0]=name
Change_sports_name(sports_directory, 'Andres')
print(sports_directory)

def Change_dict_val(z, name=None):
    z[0]['y'] = name
Change_dict_val(z,30)
print(z)

def iterateDictionary(some_list):
    for i in range(len(some_list)):
        print(some_list[i])
        

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;

def iterateDictionary2(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('first_name', students)

def iterateDictionary3(key_name, some_list):
    for i in range(len(some_list)):
        print(some_list[i][key_name])
iterateDictionary2('last_name', students)

def printInfo(some_dict):
    for key in some_dict:
        print(key)
        # List[str]
        value = some_dict[key]
        for x in value:
            print(x)




dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


printInfo(dojo)
