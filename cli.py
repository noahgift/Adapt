import optparse
from subprocess import call
from ConfigParser import ConfigParser

__version__ = 1

class Controller(object):
    """Brings together commands from config"""
    
    def __init__(self, 
                file = "config.ini",
                section = "CommandMapper"):
        
        self.file = file
        self.section = section

    def read_options_commands(self, section=None):
        """
        Returns a list of options and commands defined
        in config file.
        
        """
        if section:
            self.section = section
        cmd_list = {}
        config = ConfigParser()
        config.readfp(open(self.file))
        options = config.options(self.section)         
        #build the map of the config file
        for option in options:
            cmd = config.get(self.section, option)
            cmd_list[option] = cmd
        
        return cmd_list

    def application_root(self):

        path_map = self.read_options_commands(section="ApplicationRoot")
        return path_map["path"]

    def run(self):
        description_message = """
        A commandline tool mapper
        """
        p = optparse.OptionParser(description=description_message,
                                prog='adapt',
                                version='adapt %s' % __version__,
                                usage= '%prog [options]') 

        cmd_list = self.read_options_commands().items()
        for option, cmd in cmd_list:
            p.add_option("--%s" % option,
                        action = "store_true",
                        default = False)
        
        #dynamically generate cmds and call them
        options, arguments = p.parse_args()
        for key, value in cmd_list:
            if getattr(options, key):
                ret = call(value, shell=True) 

def main():
    """Runs everything"""
    
    c = Controller()
    c.run()

if __name__ == "__main__":
    main()
