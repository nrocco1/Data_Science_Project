# Data Science Final Project
#!/usr/bin/env python


def calc_average(data):
    sum = 0
    count = 0
    for i in data:
        if (i):
            sum += float(i)
            count += 1
    average = sum/count
    return average

if __name__ == '__main__':
    data = []
    with open('raw_predictors_until2013_no_commas.csv') as f:
        text = f.read().split()
        for line in text:
            data.append(line)
        data = data[1:]
        data_f = []
        for entry in data:
            e = entry.split(',')
            data_f.append(e)

        temp = data_f[124:913]
        csp = []
        for i in temp:
            csp.append(i[15])
       
        avg = calc_average(csp)
        temp1 = data_f[0:124]
        temp2 = data_f[912:]
        for line in temp1:
            if line[15] == '':
                line[15] = avg
        for line in temp2:
            if line[15] == '':
                 line[15] = avg

        data_final = []
        data_final.extend(temp1)
        
        temp3 = data_f[124:912]
        data_final.extend(temp3)
        data_final.extend(temp2)
        
    with open('raw_predictors_until2013_no_commas.csv', 'w') as f2:
        for item in data_final:
            f2.write("%s\n" % item) 
