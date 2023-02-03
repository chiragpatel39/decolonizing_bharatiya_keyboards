import sys 

inscript_to_keypress = {"ક" : "1", "ખ" : "2", "ગ" : "1", "ઘ" : "2", "ચ" : "1", "છ" : "2", "જ" : "1", "ઝ" : "2", "ટ" : "1", "ઠ" : "2", "ડ" : "1", "ઢ" : "2", "ણ" : "2", "ત" : "1", "થ" : "2", "દ" : "1", "ધ" : "2", "ન" : "1", "પ" : "1", "ફ" : "2", "બ" : "1", "ભ" : "2", "મ" : "1", "ય" : "1", "ર" : "1", "લ" : "1", "વ" : "1", "શ" : "2", "ષ" : "2", "સ" : "1", "હ" : "1", "ળ" : "2", "ક્ષ" : "2", "જ્ઞ" : "2", "અ" : "2", "આ" : "2", "ઇ" : "2", "ઈ" : "2", "ઉ" : "2", "ઊ" : "2", "એ" : "2", "ઐ" : "2", "ઓ" : "2", "ઔ" : "2", "્" : "1", "ા" : "1", "િ" : "1", "ી" : "1", "ુ" : "1", "ૂ" : "1", "ે" : "1", "ૈ" : "1", "ો" : "1", "ૌ" : "1", "ં" : "1", "ઃ" : "2", "ૃ" : "1", "ઋ" : "2", "ઍ" : "2", "ૅ" : "2", "ત્ર" : "1", "શ્ર" : "1"," ": 0, "1" : "1", "2" : "1", "3" : "1", "4" : "1", "5" : "1", "6" : "1", "7" : "1", "8" : "1", "9" : "1", "0" : "1", "૧" : "1", "૨" : "1", "૩" : "1", "૪" : "1", "૫" : "1", "૬" : "1", "૭" : "1", "૮" : "1", "૯" : "1", "૦" : "1" }
#guj2roman = {"ક" : "k", "ખ" : "kh", "ગ" : "g", "ઘ" : "gh", "ચ" : "ch", "છ" : "chh", "જ" : "j", "ઝ" : "z", "ટ" : "T", "ઠ" : "Th", "ડ" : "D", "ઢ" : "Dh", "ણ" : "N", "ત" : "t", "થ" : "th", "દ" : "d", "ધ" : "dh", "ન" : "n", "પ" : "p", "ફ" : "ph", "બ" : "b", "ભ" : "bh", "મ" : "m", "ય" : "y", "ર" : "r", "લ" : "l", "વ" : "v", "શ" : "sh", "ષ" : "shh", "સ" : "s", "હ" : "h", "ળ" : "L", "ક્ષ" : "ksh", "જ્ઞ" : "gn", "અ" : "a", "આ" : "aa", "ઇ" : "i", "ઈ" : "ee", "ઉ" : "u", "ઊ" : "oo", "એ" : "e", "ઐ" : "ai", "ઓ" : "o", "ઔ" : "au", "્" :"", "ા" : "aa", "િ" : "i", "ી" : "ee", "ુ" : "u", "ૂ" : "oo", "ે" : "e", "ૈ" : "ai", "ો" : "o", "ૌ" : "au", "ં" : "am", "ઃ" : "ah", "ૃ" : "ru", "ઋ" : "ru", "ઍ" : "e", "ૅ" : "e", "ત્ર" : "tr", "શ્ર" : "shr" }
vyanjana = [ "ક", "ખ", "ગ", "ઘ", "ચ", "છ", "જ", "ઝ", "ટ", "ઠ", "ડ", "ઢ", "ણ", "ત", "થ", "દ", "ધ", "ન", "પ", "ફ", "બ", "ભ", "મ", "ય", "ર", "લ", "વ", "શ", "ષ", "સ", "હ", "ળ", "ક્ષ", "જ્ઞ", "ત્ર","શ્ર"]
swara = ["અ", "આ", "ઇ", "ઈ", "ઉ", "ઊ", "એ", "ઐ", "ઓ", "ઔ","ઋ","ઍ"]
swara_chihna = ["ા", "િ", "ી", "ુ", "ૂ", "ે", "ૈ", "ો", "ૌ", "ં", "ઃ", "ૃ", "ૅ" ,"્"]
roman_to_keypress = {"a" : "1", "b" : "1", "c" : "1", "d" : "1", "e" : "1", "f" : "1", "g" : "1", "h" : "1", "i" : "1", "j" : "1", "k" : "1", "l" : "1", "m" : "1", "n" : "1", "o" : "1", "p" : "1", "q" : "1", "r" : "1", "s" : "1", "t" : "1", "u" : "1", "v" : "1", "w" : "1", "x" : "1", "y" : "1", "z" : "1", "A" : "2", "B" : "2", "C" : "2", "D" : "2", "E" : "2", "F" : "2", "G" : "2", "H" : "2", "I" : "2", "J" : "2", "K" : "2", "L" : "2", "M" : "2", "N" : "2", "O" : "2", "P" : "2", "Q" : "2", "R" : "2", "S" : "2", "T" : "2", "U" : "2", "V" : "2", "W" : "2", "X" : "2", "Y" : "2", "Z" : "2", "^" : "2"," ":"0", "1" : "1", "2" : "1", "3" : "1", "4" : "1", "5" : "1", "6" : "1", "7" : "1", "8" : "1", "9" : "1", "0" : "1" }
vyanjana = set(vyanjana)
swara  =set(swara)
swara_chihna =set(swara_chihna) 

def normalize_lines(inlines,indic_symbols):
    outlines = []
    indic_symbols.add(" ")
    indic_symbols.add("્")
    for line in inlines:
        outline = ""
        #line = line.replace(".","")
        #line =line.replace(",","")
        #line = line.replace("-","")
        #line = line.replace("'","")
        #line = line.replace('"','')
        #outlines.append(line)
        for c in line:
            if c in indic_symbols:
                outline = outline + c
        outlines.append(outline) 
    return outlines

# This function parse the file mapping between indic and roman characters as per indic_input3
def parse_indic2roman_file(infile_name):
    indic2roman = {}
    indic2roman['્'] = ''  # assigned empty string
    indic_symbols = set()
    with open(infile_name,'r') as f:
        inlines = [line.strip() for line in f.readlines()]
        for line in inlines:
            #print (line)
            fields = line.split()
            indic = fields[0]
            roman = fields[1]
            indic2roman[indic] = roman
            indic_symbols.add(indic)
    return  indic2roman, indic_symbols

def inscript_keypress_count(inlines):
    key_press_count = 0 
    for line in inlines:
        #line = normalize_line(line) # remove all the puncts and special chars
        lcount = 0     # key press count of current line
        for c in line:
            lcount += int(inscript_to_keypress[c])
        #print (lcount)
        key_press_count  += lcount
    return key_press_count

def roman_keypress_count(inlines):
    key_press_count = 0 
    for line in inlines:
        #line = normalize_line(line) # remove all the puncts and special chars
        lcount = 0     # key press count of current line
        for c in line:
            print(c)
            lcount += int(roman_to_keypress[c])
        #print (lcount)
        key_press_count  += lcount
    return key_press_count

def indic_word_to_roman_word(indic_word,indic2roman):
    roman_word = ""
    word_len = len(indic_word)
    prev_char = ""
    for i in range(0,word_len):
        current_char = indic_word[i]
        #print (current_char,prev_char)
        if prev_char in vyanjana and i != 0 and current_char not in swara_chihna:
         #   print ("prev_char is vyanjana")
            roman_word = roman_word + "a"
        roman_word = roman_word + indic2roman[current_char]
        prev_char = current_char
    return roman_word 
                
def indic_lines_to_roman_lines(indic_lines,indic2roman):
    roman_lines = []
    for line in indic_lines:
        roman_line = ""
        words = line.split()
        for w in words:
            roman_word = indic_word_to_roman_word(w,indic2roman)
            roman_line = roman_line + " " + roman_word 
        roman_lines.append(roman_line) 
    return roman_lines

def main():
    guj2rmoam_file = "resources/guj_to_roman_indic3.txt"
    guj2roman,indic_symbols = parse_indic2roman_file(guj2rmoam_file)
    infile = sys.argv[1]
    with open(infile,'r') as f:
        inlines = [line.strip() for line in f.readlines()]
    
    inlines = normalize_lines(inlines,indic_symbols) 

    inscript_keycount  = inscript_keypress_count(inlines)
    roman_lines = indic_lines_to_roman_lines(inlines,guj2roman)
    roman_keycount  = roman_keypress_count(roman_lines)
    
    #roman_key_press_count
    #for line in inlines:
     #   words = line.split()
     #   for w in words:
      #      roman = get_text_in_roman_script(w,guj2roman) 
      #      print (roman)
    print (inlines)
    print (roman_lines)
    print (inscript_keycount) 
    print (roman_keycount) 


if __name__ == '__main__':
    main()