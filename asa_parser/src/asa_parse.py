import json
import re
from asa_parser import ShowTech


class AsaParser(ShowTech):
    """Parses an ASA specific show tech"""

    def clock(self):
        """Returns show clock timestamp"""
        return json.dumps({'timestamp': self.get_show_section('clock')})

    def failover_history(self):
        """Returns failover history"""

        # Initialize variables
        fh_list = []  # This will hold the failover info
        timestamp = ''  # Timestamp of the current group information
        group_found = False  # Identifies if parser has found a group

        # --- show failover history ---
        for line in self.get_show_section('failover history'):
            # Check for a timestamp
            if ' UTC ' in line:
                timestamp = line
                group_found = True
            elif group_found:
                data = re.split(r'\s{2,}', line)[1:]
                fh = {'group': data[0],
                      'timestamp': timestamp,
                      'FromState': data[1],
                      'ToState': data[2],
                      'Reason': data[3]}
                fh_list.append(fh)
                group_found = False
        return json.dumps(fh_list)

    def startup_config_errors(self):
        """Parser for show startup-config errors"""
        return json.dumps({'text': self.get_show_section('startup-config errors')})

    def show_tech_support_license(self):
        """Parser for show tech support license"""
        return json.dumps({'text': self.get_show_section('tech-support license')})

    def show_cpu_usage(self):
        """Parser for show cpu usage"""
        return json.dumps({'text': self.get_show_section('cpu usage')})

    def show_memory_region(self):
        """Parser for show memory region"""
        return json.dumps({'text': self.get_show_section('memory region')})

    def show_cpu_detailed(self):
        """Parser for show cpu detailed"""
        return json.dumps({'text': self.get_show_section('cpu detailed')})

    def show_service_policy(self):
        return json.dumps({'text': self.get_show_section('service-policy')})
