import os
import sys
import config

class Domain:
    def __init__(self, domain_home):
        if os.path.isdir(domain_home):
            self.DOMAIN_HOME = domain_home
            self.CONFIG_XML = os.path.join(self.DOMAIN_HOME, 'config/config.xml')
            self.CFG = config.Config(self.CONFIG_XML)

    def get_config_version(self):
        if self.DOMAIN_HOME:
            return self.CFG.get_configuration_version()

    def get_domain_name(self):
        if self.DOMAIN_HOME:
            return self.CFG.get_domain_name()



if __name__ == '__main__':
    domHome = sys.argv[1]
    d1 = Domain(domHome)

    print('domain-name          = %s' % d1.get_domain_name())
    print('configraton-version  = %s' % d1.get_config_version())





