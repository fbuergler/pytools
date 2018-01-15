import ConfigParser

class Config:
    
    def __init__(self, configfile):
        self.cfg = ConfigParser.RawConfigParser()
        self.cfg.read(configfile)
        
    def getSections(self):
        sections = self.cfg.sections()
        return sections
        
    def getSectionItems(self, section):
        items = self.cfg.items(section)
        return items
        
        
    def writeConfigFiles(self):
        pass
        
        
if __name__ == '__main__':
    cfg = Config('/Users/felix/git/pytools/testdata/test.ini')
    sections = cfg.getSections()
    for s in sections:
        print('[%s]' % s)
        items = cfg.getSectionItems(s)
        for i in items:
            print('%s=%s' % (i[0],i[1]))
        print('')