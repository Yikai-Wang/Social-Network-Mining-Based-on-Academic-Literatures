# Description:
# Get all the papers with 'venue' information.
# Write into the txt file which is named after the venue.

i = 0
with open('dblp-ref-all.json', 'r') as f:
    line = f.readline()
    while line:
        i += 1
        if i%1000 == 0:
            print("processing %d"%i)
        jline = eval(line)
        if jline['venue'] == '' or '/' in jline['venue']:
            line = f.readline()
            continue
        out = open('./WithVenue/'+jline['venue']+'.txt', 'a', encoding='utf-8')
        #out = open('./WithVenue/sample.txt', 'a', encoding='utf-8')
        out.write(line)
        out.close()
        line = f.readline()
#out.close()