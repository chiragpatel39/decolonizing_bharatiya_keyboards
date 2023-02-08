import sys 
import yaml
from yaml.loader import SafeLoader


class ScriptConverter():
    global indic_symbols,vyanjana,swara,swara_chihna,indic_to_roman,inscript_to_keypress, qwerty_to_keypress  
    def __init__(self, indic_word):
        self.indic_word = indic_word
        self.roman_word = ''
        self.inscript_keypress = 0
        self.qwerty_keypress = 0  

    def normalize(self):
        norm_word = ""
        for c in self.indic_word:
            if c in indic_symbols:
                norm_word = norm_word + c
        self.indic_word = norm_word 
    
    def inscript_keypress_count(self):
        for c in self.indic_word:
            self.inscript_keypress += int(inscript_to_keypress[c]) 
            
    def inscript_to_roman(self):
        word_len = len(self.indic_word)
        prev_char = ""
        for i in range(0,word_len):
            current_char = self.indic_word[i]
            #print (current_char,prev_char)
            if prev_char in vyanjana and i != 0 and current_char not in swara_chihna:
            #   print ("prev_char is vyanjana")
               if current_char != ',' and current_char != '.':
                    self.roman_word = self.roman_word + "a"
            self.roman_word = self.roman_word + indic_to_roman[current_char]
            prev_char = current_char
    
    def qwerty_keypress_count(self):
        for c in self.roman_word:
            self.qwerty_keypress += int(qwerty_to_keypress[c])
    
    
    def get_keypress_info(self):
        self.normalize()
        self.inscript_keypress_count()
        self.inscript_to_roman()
        self.qwerty_keypress_count()
        return self.indic_word, self.roman_word, self.inscript_keypress, self.qwerty_keypress            

# This function reads all the character related information from yaml file and
#assign them to the variables

def file_parser(infile):
    outdict = {}
    keylist = [] 
    with open(infile,'r') as f:
        inlines = [line.strip() for line in f.readlines()]
        for line in inlines:
            fields = line.split()
            if len(fields) != 2:
                sys.exit("There is an issue with config file: ", infile)
            k = fields[0]
            v = fields[1]
            outdict[k]  = v
            keylist.append(k) 
    return  outdict, keylist 


def get_lang_info(lang_):
    with open('resources/' + lang_ + '.yaml','r') as f:
        data = yaml.load(f, Loader=SafeLoader)
    indic_to_roman,_ = file_parser(data['indic_to_roman_file'])
    qwerty_to_keypress,_ = file_parser(data['roman_to_keypress_file'])
    inscript_to_keypress, indic_symbols =  file_parser(data['gujarati_to_keypress_file']) 
    
    vyanjana_range = data['vynajana_lines'] 
    swara_range = data['swara_lines']
    swara_chihna_range = data['swara_chihna_lines']
    
    vyanjana_range = vyanjana_range.split('-')
    vyanjana_range = (int(vyanjana_range[0])-1, int(vyanjana_range[1]))
    
    swara_range = swara_range.split('-')
    swara_range = (int(swara_range[0])-1, int(swara_range[1]))
    
    swara_chihna_range = swara_chihna_range.split('-')
    swara_chihna_range = (int(swara_chihna_range[0])-1, int(swara_chihna_range[1]))
    
    vyanjana = indic_symbols[vyanjana_range[0]: vyanjana_range[1]]
    swara = indic_symbols[swara_range[0]: swara_range[1]]
    swara_chihna = indic_symbols[swara_chihna_range[0]: swara_chihna_range[1]]
    
    indic_symbols = set(indic_symbols)
    indic_symbols.add(' ')
    indic_symbols.add("્")
    
    vyanjana = set(vyanjana)
    swara = set(swara)
    swara_chihna = set(swara_chihna)    
   
    indic_to_roman['્']  = ''
    return indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress
    #print (indic_symbols)
    
def main():
    if len(sys.argv) != 4:
        print ("USAGE: python inscript_vs_transliteration.py <lang> <input file> <output file>" )
        print ("Ex: python inscript_vs_transliteration.py gujarati sample_text/gujarati_sample.txt output/trans.txt" )
        sys.exit("Invalid Usage")
    lang_ = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]

    global indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress;
    indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress = get_lang_info(lang_)

    #print (indic_symbols) 
    
    with open(infile,'r') as f:
        inlines = [line.strip() for line in f.readlines()]
    
    indic_normlines = []
    roman_lines = []
    inscript_lkp_list = [] # list of keypress per line
    qwerty_lkp_list = []  # same as above    
    
    inscript_counter = 0
    qwerty_counter = 0 
    
    
    for line in inlines:
        if  (len(line)) == 0:
            continue
        normline = ""
        roman_line = "" 
        words =  line.split()
        num_words = len(words)
        inscript_lkp = num_words - 1  # key press of current line. Added count for spaces 
        qwerty_lkp = num_words - 1   # key press of current line 
        #inscript_lkp = 0 # if we don't want to count spaces   
        #qwerty_lkp = 0  
        for w in words:
            scriptObj = ScriptConverter(w)
            indic_word, roman_word, inscript_keypress,qwerty_keypress  = scriptObj.get_keypress_info()
            inscript_lkp  += inscript_keypress
            qwerty_lkp += qwerty_keypress
            normline = normline + " " + indic_word
            roman_line  = roman_line + " " + roman_word 
        inscript_lkp_list.append(inscript_lkp)
        qwerty_lkp_list.append(qwerty_lkp)
        indic_normlines.append(normline)
        roman_lines.append(roman_line)
        inscript_counter += inscript_lkp
        qwerty_counter += qwerty_lkp    
    
    
    with open(outfile,'w') as f:
        len_  = len(indic_normlines)   
        for i in range(0,len_):
            f.write(indic_normlines[i] + "\t" + roman_lines[i] + "\t" + str(inscript_lkp_list[i]) + "\t" +  str(qwerty_lkp_list[i]) + "\n" )  
    
    print ("Keystroks in Inscript :  " +   str(inscript_counter))   
    print ("Keystroks in Transliteration  :  " +   str(qwerty_counter))   
    print ("Transliteration requires : " + str((qwerty_counter-inscript_counter)/float(inscript_counter) * 100.0) + " " + "more skystrokes"  )
if __name__ == '__main__':
    main()