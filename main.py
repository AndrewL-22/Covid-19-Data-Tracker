#Project 3 - Nikhil Prakash, Andrew Louis, Franco A. Castillodelacruz
def main(): #main function
  outfile=open('covid_data.txt', 'a') #file open statement
  outfile.write('3 week Covid-19 Data Sheet\n')
  outfile.write('\n')
  outfile.write('\n')
  outfile.close() #file close statement

  print('Welcome to the COVID-19 3 Week Data Sheet Generator!')

  firstDate = input('Enter the date (mm/dd/yy): ')
  print("You will first enter the data for the first day.")
  firstDay_regions = get_regions()
  firstDay_symptoms = get_symptoms()
  
  while True:
    try:
      fdlowerAge = int(input('Enter the average lower age that is predominently affected for today: '))
      fdupperAge = int(input('Enter the average upper age that is predominently affected for today: '))
      firstDay_ageRange = get_ageRange(fdlowerAge,fdupperAge)
      break
    except ValueError: #error handler
      print()
      print("Invalid input. Please enter a valid number.")
      continue
  
  fdsource = get_source()
 
  outfile=open('covid_data.txt', 'a') #file open statement
  outfile.write(firstDate + '\n')
  outfile.write('Regions Affected: ')
  for item in firstDay_regions:
    outfile.write(item + ', ')
  outfile.write('\n')
  outfile.write('Symptoms: ')
  for item in firstDay_symptoms:
    outfile.write(item + ', ')
  outfile.write('\n')
  outfile.write('Age Range: ' + firstDay_ageRange + '\n')
  outfile.write('Sources: ')
  for item in fdsource:
    outfile.write(item + ', ')
  outfile.write('\n')
  outfile.write('\n')
  outfile.close() #file close statement
  
  i = 0
  regions = [] #sequence: list of regions that will be added to
  symptoms = [] #sequence: list of symptoms that will be added to
  while i < 21: #will run the program for 21 days (3 weeks)
    date = input('Enter the date (mm/dd/yy): ')
    regions2 = get_regions2()
    for item in regions2:
      regions.append(item)
    symptoms2 = get_symptoms2()
    for item in symptoms2:
      symptoms.append(item)
    while True:
      try:
        lowerAge = int(input('Enter the average lower age that is predominently affected for today: '))
        upperAge = int(input('Enter the average upper age that is predominently affected for today: '))
        ageRange = get_ageRange(lowerAge,upperAge)
        break
      except ValueError: #error handler
        print()
        print("Invalid input. Please enter a valid number.")
        continue
    source = get_source()
    print()
    print("These are all of the changes to the data for today: \n")
    region_significantChange(firstDay_regions,regions)
    symptoms_significantChange(firstDay_symptoms,symptoms)
    ageRange_significantChange(firstDay_ageRange,ageRange)
    print()
   
    outfile=open('covid_data.txt', 'a') #file open statement
    outfile.write(date + '\n')
    outfile.write('Regions Affected: ')
    for item in firstDay_regions:
      outfile.write(item + ', ')
    for item in regions:
      outfile.write(item + ', ')
    outfile.write('\n')
    outfile.write('Symptoms: ')
    for item in firstDay_symptoms:
      outfile.write(item + ', ')
    for item in symptoms:
      outfile.write(item + ', ')
    outfile.write('\n')
    outfile.write('Age Range: ' + ageRange + '\n')
    outfile.write('Sources: ')
    for item in source:
      outfile.write(item + ', ')
    outfile.write('\n')
    outfile.write('\n')
    outfile.close() #file close statement
    i+=1

def get_regions(): #function that gets regions affected from user for the first day
  regions_affected = [] #sequence: list of regions affected that will be added to by the user for the first day
  again = 'y'
  while again == 'y':
      value = input('Enter a region affected by COVID-19 on the first day: ')
      regions_affected.append(value) 
      print('Do you want to add another region? ')
      again = input('y = yes, anything else = no ')
      print()
  return regions_affected

def get_regions2(): #list that gets new regions affected from user from day 2 and beyond
  regions_affected2 = [] #sequence: list of regions affected that will be added to by the user for the 2nd day and beyond
  print('Are there any other regions that have been affected that you would like to add for this day? ')
  again = input('y = yes, anything else = no ')
  while again == 'y':
    value = input('Enter an additional region affected by COVID-19 that you would like to add: ')
    regions_affected2.append(value) 
    print('Do you want to add another region? ')
    again = input('y = yes, anything else = no ')
    print()
  return regions_affected2

def get_symptoms(): #function that gets symptoms from user for the first day
  new_symptoms = [] #sequence: list of symptoms that the user will add to for the first day
  again = 'y'
  while again == 'y':
    value = input('Enter a symptom of COVID-19 for first day: ')
    new_symptoms.append(value) 
    print('Do you want to add more symptoms? ')
    again = input('y = yes, anything else = no ')
    print()
  return new_symptoms
  
def get_symptoms2(): #function that gets the new symptoms from user for the 2nd day and beyond
  new_symptoms2 = [] #sequence: list of new symptoms that the user will add to for the 2nd day and beyond
  print('Are there any new symptoms that you would like to add for this new day? ')
  again = input('y = yes, anything else = no ')
  while again == 'y':
    value = input('Enter a new symptom of COVID-19 that you would like to add: ')
    new_symptoms2.append(value) 
    print('Do you want to add more symptoms? ')
    again = input('y = yes, anything else = no ')
    print()
  return new_symptoms2

  
def get_source(): #function that gets sources from the user
  sources = [] #sequence: list of sources that the user will add to
  again = 'y'
  while again == 'y':
    value = input('Enter the URL of the source of your data: ')
    sources.append(value) 
    print('Do you want to add another source?: ')
    again = input('y = yes, anything else = no ')
    print()
  return sources

def get_ageRange(lowerAge, upperAge): #function that takes the lower age and upper range and turns it into a string
  ageRange = (f'{lowerAge}-{upperAge}' )
  return ageRange

def region_significantChange(firstRegion, newRegion): #function that checks if there is a significant change in regions from the first day
  if len(firstRegion) == len(newRegion)+len(firstRegion): #decision structure: if statement
    print("There is no significant change in the number of affected regions from the first day.")
  elif len(firstRegion) < len(newRegion)+len(firstRegion): #decision structure: elif statement
    change = len(newRegion) - len(firstRegion)
    print(f"The number of affected regions increased by {change+1} from the first day.")

def symptoms_significantChange(firstSymptoms, newSymptoms): #function that checks if there is a significant change in symptoms from the first day
  if len(firstSymptoms) == len(newSymptoms)+len(firstSymptoms): #decision structure: if statement
    print("There is no significant change in the number of affected symptoms from the first day.")
  elif len(firstSymptoms) < len(newSymptoms)+len(firstSymptoms): #decision structure: elif statement
    change = len(newSymptoms) - len(firstSymptoms)
    print(f"The number of affected symptoms increased by {change+1} from the first day.")

def ageRange_significantChange(fdAgeRange, ageRange): #function that checks if there is a significant change in age range from the first day
  if fdAgeRange == ageRange: #decision structure: if statement
    print("There is no significant change in the age range from the first day.")
  else: #decision structure: else statement
    print(f"The first day age range is {fdAgeRange}, todays age range is {ageRange}.")

if __name__ == '__main__':
  main()