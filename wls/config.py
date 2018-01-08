from lxml import etree

class Config:

    def __init__(self, cfg):
        self.cfg = cfg
        self.rootElement = None

    def getConfigFile(self):
        return self.cfg

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
        elements = self.getRoot().findall('.//' + elem, namespaces=self.getRoot().nsmap)
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

