def convertScore(score):
    if score >=90:
        return 'A'
    elif score >=80:
        return 'B'
    elif score >=70:
        return 'C'
    elif score >=60:
        return 'D'
    else:
        return 'F'

input_file = "input.csv"
output_file = "output.csv"

with open(output_file, "w") as fw:
    with open(input_file, "r") as fr:
        all_text = fr.read()
        lines = all_text.split('\n')
        for line in lines:
            words = line.split(',')
            words[1] = convertScore(int(words[1]))
            fw.write(words[0]+ ', '+ words[1]+'\n')

fr.close()
fw.close()