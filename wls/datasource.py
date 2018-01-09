import config
import sys

class DataSource:

    def __init__(self, xml):
        self.XML = xml
        self.CFG = config.DataSource(self.XML)

    def get_datasource_name(self):
        return self.CFG.get_datasource_name()

    def get_url(self):
        return self.CFG.get_url()

    def get_driver(self):
        return self.CFG.get_driver()

    def get_username(self):
        return self.CFG.get_user()

    def get_pass_encrypted(self):
        return self.CFG.get_pass_encrypted()

    def get_jndi(self):
        return self.CFG.get_jndi()

    def get_pool_initial(self):
        return self.CFG.get_pool_initial()

    def get_pool_min(self):
        return self.CFG.get_pool_min()

    def get_pool_max(self):
        return self.CFG.get_pool_max()




if __name__ == '__main__':

    fName = sys.argv[1]
    ds = DataSource(fName)
    print('[%s]' % ds.get_datasource_name())
    print('name           = %s' % ds.get_datasource_name())
    print('url            = %s' % ds.get_url()[0])
    print('driver         = %s' % ds.get_driver()[0])
    print('username       = %s' % ds.get_username()[0])
    print('pass           = %s' % ds.get_pass_encrypted()[0])
    print('jndi           = %s' % ds.get_jndi()[0])
    print('pool-initial   = %s' % ds.get_pool_initial())
    print('pool-min       = %s' % ds.get_pool_min())
    print('pool-max       = %s' % ds.get_pool_max())



