#simply run python3 AWS_srt_to_transcript <filename>



import sys
filepath = "lupoInitialBrief.srt"
f = open(filepath, 'r')
input = f.readlines()
output_path = sys.argv[1]
f.close()
output = ""

#script clean up here
i = 2
while i < len(input):
    input[i]
    line = input[i].replace("\n", "")

    if (line.endswith(".")):
        line += "\n"
    else:
        line += " "

    output += line
    i = i + 4

print(output)
o = open(output_path + ".txt", "w")
o.write(output)
o.close()
