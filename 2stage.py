#!/usr/bin/python

types = {
    'j':'branch',
    'nop':'arth',
    'li':'memory',
    'sw':'memory',
    'ret':'branch',
    'addi':'arth',
    'bgez':'branch',
    'bleu':'branch',
    'ble':'branch',
    'mv':'memory',
    'lbu':'memory',
    'add':'arth',
    'jal':'branch',
    'blez':'branch',
    'jalr':'branch',
    'blt':'branch',
    'bltu':'branch',
    'bnez':'branch',
    'csrw':'memory',
    'csrr':'memory',
    'csrc':'memory',
    'csrs':'memory',
    'csrrs':'memory',
    'csrrc':'memory',
    'csrrw':'memory',
    'csr':'memory',
    'sw':'memory',
    'fence':'memory',
    'sub':'arth',
    'subi':'arth',
    'lui':'memory',
    'jr':'branch',
    'sb':'memory',
    'sltu':'arth',
    'sltiu':'arth',
    'xori':'arth',
    'andi':'arth',
    'ori':'arth',
    'neg':'arth',
    'xor':'arth',
    'and':'arth',
    'or':'arth',
    'slli':'arth',
    'srli':'arth',
    'srai':'arth',
    'beq':'branch',
    'srl':'arth',
    'sll':'arth',
    'sra':'arth',
    'addw':'arth',
    'sllw':'arth',
    'srlw':'arth',
    'sraw':'arth',
    'subw':'arth',
    'fadd':'arth',
    'fsub':'arth',
    'fmul':'arth',
    'fdiv':'arth',
    'fadd.s':'arth',
    'fsub.s':'arth',
    'fmul.s':'arth',
    'fdiv.s':'arth',
    'fnmsub.s':'arth',
    'bltz':'arth',
    'auipc':'arth',
    'beqz':'branch',
    'eret':'branch',
    'lw':'memory',
    'bne':'branch',
    'ecall':'branch',
    'rdcycle':'arth',
    'rdinstret':'arth',
    'rdtime':'arth',
    'bgtz':'arth',
}

count = {
    'branch':0,
    'arth':0,
    'memory':0,
}


assmbFile = open("./profile results/multiply.riscv.dump", "r+")
print "Name of the file: ", assmbFile.name

assembly = {}

while True:
    line = assmbFile.readline()
    if not line:
        break
    index = line.strip().split('\t')
    #print index

    if index.__len__() >= 3:
        key = ''
        temp = index[0]
        if index[0].__len__() == 4:
            key = "0x00000%s" % index[0]
        else:
            key = "0x0000%s" % index[0]

        key = key[0:key.__len__()-1]

        assembly[key] = index[2]

    #if index != -1 :
    #    newline = line[index+3:index+14]
    #    print "Read Line: %s" % (line[index+3:index+14])


# Open a file
print "Read Line: %s" % (assembly['0x00001f18'])
fo = open("./profile results/2stage.riscv.out", "r+")
print "Name of the file: ", fo.name


while True:
    line = fo.readline()
    if not line:
        break
    index = line.find("PC= ")
    if index != -1 :
        #newline = line[index+3:index+14]
        #print line[index+5:index+15]
        #print "Read Line: %s" % (assembly[line[index+5:index+15]])

        temp = count[types[assembly[line[index+5:index+15]]]] + 1
        count[types[assembly[line[index+5:index+15]]]] = temp

print count
# Close opened file
fo.close()
