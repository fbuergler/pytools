from lxml import etree
import os
import sys
import logging as log

log.basicConfig(level=log.DEBUG)

class Config:

    def __init__(self, cfg):
        if os.path.isabs(cfg) and (os.path.basename(cfg) == 'config.xml'):
            self.cfg = cfg
            self.rootElement = None
        else:
            log.error(cfg+ ': excpect DOMAIN_HOME/config/config.xml')
            sys.exit(1)

    def get_config_file(self):
        return self.cfg

    def get_root(self):
        self.tree = etree.parse(self.cfg)
        self.root = self.tree.getroot()
        return self.root

    def get_ns_map(self):
        self.nsmap = {k: v for k, v in self.get_root().nsmap.iteritems() if k}
        return self.nsmap

    def get_element_text(self, elem):
        ret = []
        elements = self.get_root().findall('.//' + elem, namespaces=self.get_root().nsmap)
        for elem in elements:
            ret.append(elem.text)
        ret.sort()
        return ret

    def get_server_names(self):
        return self.get_element_text('server/name')

    def get_server_listen_address(self):
        return self.get_element_text('server/listen-address')

    def get_server_listen_port(self):
        return self.get_element_text('server/listen-port')

    def get_server_listen_port_ssl(self):
        return self.get_element_text('server/ssl/listen-port')

    def get_server_logfile_names(self):
        return self.get_element_text('server/log/file-name')

    def get_machine_names(self):
        return self.get_element_text('machine/name')

    def get_cluster_names(self):
        return self.get_element_text('cluster/name')

    def get_authentication_providers(self):
        pass

    def get_configuration_version(self):
        return self.get_element_text('configuration-version')

    def get_domain_name(self):
        elem = self.get_root().find('.//name', namespaces=self.get_root().nsmap)
        return elem.text


    # for e in root.xpath('//wls:host[text()="ldap01.suvanet.ch"]', namespaces=nsmap):
    #     print(e.text)


class DataSource:

    def __init__(self, xml):
        self.xml = xml
        self.rootElement = None

    def get_root(self):
        try:
            self.tree = etree.parse(self.xml)
            self.root = self.tree.getroot()
            return self.root
        except:
            return None

    def get_ns_map(self):
        try:
            self.nsmap = {k: v for k, v in self.get_root().nsmap.iteritems() if k}
            return self.nsmap
        except:
            return None


    def get_element_text(self, elem):
        ret = []
        elements = self.get_root().findall('.//' + elem, namespaces=self.get_root().nsmap)
        for elem in elements:
            ret.append(elem.text)
        ret.sort()
        return ret

    def get_datasource_name(self):
        try:
            elem = self.get_root().find('.//name', namespaces=self.get_root().nsmap)
            return elem.text
        except:
            return None


    def get_url(self):
        try:
            return self.get_element_text('jdbc-driver-params/url')[0]
        except:
            return None

    def get_driver(self):
        try:
            return self.get_element_text('jdbc-driver-params/driver-name')[0]
        except:
            None

    def get_user(self):
        try:
            return self.get_element_text('jdbc-driver-params/properties/property/value')[0]
        except:
            return None

    def get_pass_encrypted(self):
        try:
            return self.get_element_text('jdbc-driver-params/password-encrypted')[0]
        except:
            return None

    def get_jndi(self):
        try:
            return self.get_element_text('jdbc-data-source-params/jndi-name')
        except:
            return None

    def get_pool_initial(self):
        try:
            return self.get_element_text('jdbc-connection-pool-params/initial-capacity')[0]
        except:
            return 1

    def get_pool_min(self):
        try:
            return self.get_element_text('jdbc-connection-pool-params/min-capacity')[0]
        except:
            return 1

    def get_pool_max(self):
        try:
            return self.get_element_text('jdbc-connection-pool-params/max-capacity')[0]
        except:
            return 10