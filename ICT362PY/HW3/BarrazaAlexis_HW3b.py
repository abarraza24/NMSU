"""
    Module: BarrazaAlexis_Lesson 3b
    Author: Alexis Barraza
    Date: August 26, 2026
    Course: ICT 362 - Software Technology II
    
    Assignment: Working with Logic statements and Dictionaries
    
    Description:
        The program works with dictionary objects.
        It imports pipe-delimited automobile data into a nested dictionary
        and creates reports from the dictionary. 
"""

autoPipeString = """mpg|cylinders|displacement|horsepower|weight|acceleration|year|origin|make|model
18|8|307|130|3504|12|70|1|chevrolet|chevelle malibu
15|8|350|165|3693|11.5|70|1|buick|skylark 320
18|8|318|150|3436|11|70|1|plymouth|satellite
16|8|304|150|3433|12|70|1|amc|rebel sst
17|8|302|140|3449|10.5|70|1|ford|torino
15|8|429|198|4341|10|70|1|ford|galaxie 500
14|8|454|220|4354|9|70|1|chevrolet|impala
14|8|440|215|4312|8.5|70|1|plymouth|fury iii
14|8|455|225|4425|10|70|1|pontiac|catalina
15|8|390|190|3850|8.5|70|1|amc|ambassador dpl
15|8|383|170|3563|10|70|1|dodge|challenger se
14|8|340|160|3609|8|70|1|plymouth|cuda 340
15|8|400|150|3761|9.5|70|1|chevrolet|monte carlo
14|8|455|225|3086|10|70|1|buick|estate wagon (sw)
24|4|113|95|2372|15|70|3|toyota|corona mark ii
22|6|198|95|2833|15.5|70|1|plymouth|duster
18|6|199|97|2774|15.5|70|1|amc|hornet
21|6|200|85|2587|16|70|1|ford|maverick
27|4|97|88|2130|14.5|70|3|datsun|pl510
26|4|97|46|1835|20.5|70|2|volkswagen|1131 deluxe sedan
25|4|110|87|2672|17.5|70|2|peugeot|504
24|4|107|90|2430|14.5|70|2|audi|100 ls
25|4|104|95|2375|17.5|70|2|saab|99e
26|4|121|113|2234|12.5|70|2|bmw|2002
21|6|199|90|2648|15|70|1|amc|gremlin
10|8|360|215|4615|14|70|1|ford|f250
10|8|307|200|4376|15|70|1|chevy|c20
11|8|318|210|4382|13.5|70|1|dodge|d200
27|4|97|88|2130|14.5|71|3|datsun|pl510
28|4|140|90|2264|15.5|71|1|chevrolet|vega 2300"""

# Empty dictionary to store all automobile records
autoDictionary = {}
# Split autoPipeString at each new line and saves it into autoList
autoList = autoPipeString.split("\n")

#Loop through auto list starting at index 1 skips the header and go all the way through
for auto in autoList[1:]:
    # Split the current auto row at each pipe character 
    # store them in attr
    attr = auto.split("|")
    # Store the automobile attr in a nested dictionary
    attrDictionary = {
        "mpg": attr[0],
        "cylinders": attr[1],
        "displacement": attr[2],
        "horsepower": attr[3],
        "weight": attr[4],
        "acceleration": attr[5],
        "year": attr[6],
        "origin": attr[7],
        "make": attr[8]
    }
    
    # save attr index 9 into the model variable
    model = attr[9]
    
    # I think this is the version of python to use model as the key.
    # I'm not to sure
    autoDictionary[model] = attrDictionary

for model, attrib in autoDictionary.items():
    if int(attrib['mpg']) > 18:
        print(f"The { attrib['make']} {model} gets {attrib['mpg']} miles per gallon")
        

print("\nRequirement 6: Cars with 6 cylinders")

for model, attrib in autoDictionary.items():
    # If the car's cylinders equal 6 print it
    if int(attrib["cylinders"]) == 6:
        print(  f"Make: {attrib['make']:10}" 
                f"Model: {model:15} "
                f"MPG: {attrib['mpg']:3} "
                f"Cylinders: {attrib['cylinders']}"
              
              )
        

print("\nRequirement 7: Cars from Japan")   
     
for model, attrib in autoDictionary.items():
    # If the car is from Japan print it out
    if int(attrib["origin"]) == 3:
        print(
            f"Make: {attrib['make']:10}"
            f"Model:  {model:15} "
            f"Weight: {attrib['weight']:10}"
            f"Origin: {attrib['origin']:3}"
            
        )
        
# Average weight
totalWeight = 0

for model, attrib in autoDictionary.items():
    # Adding every weight of the cars
    totalWeight += int(attrib["weight"])
    
    #divide by the number of cars
    averageWeight = totalWeight / len(autoDictionary)
    
print(f"\n Requirement 8: The average weight of all cars is {averageWeight:.2f} pounds")

# Cylinders and displacement over 320
print("\nRequirement 9: 8 cylinders and displacement over 320")

for model, attrib in autoDictionary.items():
    # if the car has 8 cylinders and 320 displacement print out the results
    if(int(attrib["cylinders"]) == 8 and int(attrib["displacement"]) > 320):
        print(
            f"Make: {attrib['make']:10} "
            f"Model: {model:20} "
            f"MPG: {attrib['mpg']:3}"
            f"Cylinders: {attrib['cylinders']}"
        )
        

print("\nRequirement 10: 6-cylinder cars made in the US")

for model, attrib in autoDictionary.items():
    # If the car has 6 cylinders and from the United states print them.
    if int(attrib["cylinders"]) == 6 and int(attrib["origin"]) == 1:
        print(
            f"Make: {attrib['make']:10} "
            f"Model: {model:15} "
            f"Cylinders: {attrib['cylinders']} "
            f"Origin: {attrib['origin']}"
        )
        

japanTotalMpg = 0
japanCount = 0

usTotalMpg = 0
usCount = 0

for model, attrib in autoDictionary.items():
    if int(attrib["origin"]) ==3:
        japanTotalMpg += float(attrib["mpg"])
        japanCount +=1
    elif int(attrib["origin"]) == 1:
        usTotalMpg += float(attrib["mpg"])
        usCount +=1
    
japanAverageMpg = japanTotalMpg / japanCount
usAverageMpg = usTotalMpg / usCount
    
print(f"Average MPG for cars from Japan: {japanAverageMpg:.2f}")
print(f"Average MPG for cars from the US: {usAverageMpg:.2f}")