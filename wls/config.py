from lxml import etree


class ConfigXML:

    def __init__(self, cfg):
        self.cfg = cfg
        self.rootElement = None

    def getRoot(self):
        self.tree = etree.parse(self.cfg)
        self.root = self.tree.getroot()
        return self.root

    def getNSmap(self):
        self.nsmap = {k: v for k, v in self.getRoot().nsmap.iteritems() if k}
        return self.nsmap

    def parseConfigXML(self, config_xml):
        pass

    def getElementText(self, elem):
        ret = []
        elements = cfg.getRoot().findall('.//' + elem, namespaces=cfg.getRoot().nsmap)
        for elem in elements:
            ret.append(elem.text)
        ret.sort()
        return ret

    def getServerNames(self):
        return self.getElementText('server/name')

    def getServerLogFileNames(self):
        return self.getElementText('server/log/file-name')

    def getMachineNames(self):
        return self.getElementText('machine/name')

    def getClusterNames(self):
        return self.getElementText('cluster/name')

    def getAuthenticationProviders(self):
        pass

    def getConfigurationVersion(self):
        return self.getElementText('configuration-version')


if __name__ == '__main__':
    cfg = ConfigXML('/Users/felix/Documents/workspace/py/testdata/config.xml')

    print cfg.getServerNames()
    print cfg.getMachineNames()
    print cfg.getClusterNames()
    print cfg.getConfigurationVersion()
    print cfg.getServerLogFileNames()

