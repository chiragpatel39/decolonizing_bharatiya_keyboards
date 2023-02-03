import sys 
import yaml
from yaml.loader import SafeLoader


class ScriptConverter():
    def __init__(self, indic_word):
        self.indic_word = indic_word
        self.roman_word = ''
        self.indic_keypress = 0
        self.roman_keypress = 0  
    

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
    
    return indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress
    #print (indic_symbols)
    
def main():
    lang_ = sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]
    global indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress;
    indic_symbols, vyanjana, swara, swara_chihna, indic_to_roman, inscript_to_keypress, qwerty_to_keypress = get_lang_info(lang_)
    hello() 
    return 0     

if __name__ == '__main__':
    main()