import config

class DataSource:

    def __init__(self, xml):
        self.XML = xml
        self.CFG = config.DataSource(self.XML)

    def getDataSourceName(self):
        return self.CFG.getDataSourceName()

    def getUrl(self):
        return self.CFG.getUrl()

    def getDriver(self):
        return self.CFG.getDriver()

    def getUsername(self):
        return self.CFG.getUser()

    def getPassEncrypted(self):
        return self.CFG.getPassEncrypted()

    def getJndi(self):
        return self.CFG.getJndi()

    def getPoolInitial(self):
        return self.CFG.getPoolInitial()

    def getPoolMin(self):
        return self.CFG.getPoolMin()

    def getPoolMax(self):
        return self.CFG.getPoolMax()




if __name__ == '__main__':
    ds = DataSource('/Users/felix/Documents/testdata/ora_suva_txds-jdbc.xml')
    print('[%s]' % ds.getDataSourceName())
    print('name           = %s' % ds.getDataSourceName())
    print('url            = %s' % ds.getUrl()[0])
    print('driver         = %s' % ds.getDriver()[0])
    print('username       = %s' % ds.getUsername()[0])
    print('pass           = %s' % ds.getPassEncrypted()[0])
    print('jndi           = %s' % ds.getJndi()[0])
    print('pool-initial   = %s' % ds.getPoolInitial()[0])
    print('pool-min       = %s' % ds.getPoolMin()[0])
    print('pool-max       = %s' % ds.getPoolMax()[0])



