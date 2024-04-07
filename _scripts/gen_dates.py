dates_file = open("dates.txt", "r")

for line in dates_file:
    read_line = line.strip().split(";")
    if(len(read_line)>1):
        print("- topic: " + read_line[1])
    else:
        print("- topic: TBD")
    print("  type: lecture")
    print("  date: " + read_line[0])
    print("  coursepack: #")

lab_dates = open("lab_dates.txt", "r")

for line in lab_dates:
    read_line = line.strip().split(";")
    if(len(read_line)>1):
        print("- topic: " + read_line[1])
    else:
        print("- topic: TBD")
    print("  type: lab")
    print("  date: " + read_line[0])
    print("  sprint_report: #")
