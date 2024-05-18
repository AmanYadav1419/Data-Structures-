file_name = input("Enter file name: ")
with open(file_name, "r") as file1:
   d = dict()
   print("\n Content of file: \n")
   for line in file1:
      print(line, end='')
      line = line.strip()
      line = line.lower()
      words = line.split(" ")
      for word in words:
         d[word] = d[word] + 1 if word in d else 1
   print("\n\nOccurrences of each word in file is: ")
   for key in list(d.keys()):
      print(key, ":", d[key])
