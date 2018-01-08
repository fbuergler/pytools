import os
import sys
import config

class Domain:
    def __init__(self, domain_home):
        if os.path.isdir(domain_home):
            self.DOMAIN_HOME = domain_home
            self.CONFIG_XML = os.path.join(self.DOMAIN_HOME, 'config/config.xml')
            self.CFG = config.Config(self.CONFIG_XML)
        else:
            self.DOMAIN_HOME = None

    def getConfigVersion(self):
        if self.DOMAIN_HOME:
            return self.CFG.getConfigurationVersion()


    def printServerNames(self):
        if self.DOMAIN_HOME:
            for srv in self.CFG.getServerNames():
                print srv

    def getDomainName(self):
        if self.DOMAIN_HOME:
            return self.CFG.getDomainName()


    def printXpath(self):
        if self.DOMAIN_HOME:
            root = self.CFG.getRoot()







if __name__ == '__main__':
    domHome = sys.argv[1]
    d1 = Domain(domHome)

    print('domain-name          = %s' % d1.getDomainName())
    print('configraton-version  = %s' % d1.getConfigVersion())





