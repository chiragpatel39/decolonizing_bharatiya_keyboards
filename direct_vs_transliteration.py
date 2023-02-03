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
    lang_ = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]
    global indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress;
    indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress = get_lang_info(lang_)
    
    #print (indic_symbols) 
    
    with open(infile,'r') as f:
        inlines = [line.strip() for line in f.readlines()]
    
    inscript_counter = 0
    qwerty_counter = 0 
    
    for line in inlines:
        words =  line.split()
        num_words = len(words)
        inscript_counter += num_words - 1  # adding count for spaces. sentence with n words have n-1 spaces
        qwerty_counter  += num_words - 1    
        for w in words:
            scriptObj = ScriptConverter(w)
            indic_word, roman_word, inscript_keypress,qwerty_keypress  = scriptObj.get_keypress_info()
            inscript_counter += inscript_keypress
            qwerty_counter += qwerty_keypress
    
     
    print (inscript_counter, qwerty_counter)
    
    return 0     

if __name__ == '__main__':
    main()