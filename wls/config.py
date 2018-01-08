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

    def getElementText(self, elem):
        ret = []
        elements = self.getRoot().findall('.//' + elem, namespaces=self.getRoot().nsmap)
        for elem in elements:
            ret.append(elem.text)
        ret.sort()
        return ret

    def getServerNames(self):
        return self.getElementText('server/name')

    def getServerListenAddress(self):
        return self.getElementText('server/listen-address')

    def getServerListenPort(self):
        return self.getElementText('server/listen-port')

    def getServerListenPortSSL(self):
        return self.getElementText('server/ssl/listen-port')

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

    def getDomainName(self):
        elem = self.getRoot().find('.//name', namespaces=self.getRoot().nsmap)
        return elem.text


    # for e in root.xpath('//wls:host[text()="ldap01.suvanet.ch"]', namespaces=nsmap):
    #     print(e.text)


class DataSource:

    def __init__(self, xml):
        self.xml = xml
        self.rootElement = None

    def getRoot(self):
        self.tree = etree.parse(self.xml)
        self.root = self.tree.getroot()
        return self.root

    def getNSmap(self):
        self.nsmap = {k: v for k, v in self.getRoot().nsmap.iteritems() if k}
        return self.nsmap


    def getElementText(self, elem):
        ret = []
        elements = self.getRoot().findall('.//' + elem, namespaces=self.getRoot().nsmap)
        for elem in elements:
            ret.append(elem.text)
        ret.sort()
        return ret

    def getDataSourceName(self):
        elem = self.getRoot().find('.//name', namespaces=self.getRoot().nsmap)
        return elem.text

    def getUrl(self):
        return self.getElementText('jdbc-driver-params/url')

    def getDriver(self):
        return self.getElementText('jdbc-driver-params/driver-name')

    def getUser(self):
        return self.getElementText('jdbc-driver-params/properties/property/value')

    def getPassEncrypted(self):
        return self.getElementText('jdbc-driver-params/password-encrypted')

    def getJndi(self):
        return self.getElementText('jdbc-data-source-params/jndi-name')

    def getPoolInitial(self):
        return self.getElementText('jdbc-connection-pool-params/initial-capacity')

    def getPoolMin(self):
        return self.getElementText('jdbc-connection-pool-params/min-capacity')

    def getPoolMax(self):
        return self.getElementText('jdbc-connection-pool-params/max-capacity')