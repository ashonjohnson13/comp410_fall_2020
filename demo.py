# COMP410 Fall initial demo example
import json
import asa_parser as ap
import git
import os
import pandas as pd

def run_demo():
    # Find path to the data directory in this repo
    data_path = os.path.join(git.Repo('.', search_parent_directories=True).working_tree_dir, 'data')

    # Create an asa sh tech object
    primary_asa = ap.AsaParser(os.path.join(data_path, 'showtech_primary.txt'))

    # show clock example
    print(primary_asa.clock())

    # show failover history example
    print(primary_asa.failover_history())

    # create a dataframe
    df = pd.read_json(primary_asa.failover_history())
    # top reasons found in the failover history
    print(df['Reason'].value_counts())
    print('Demo Message')

    # startup-config errors
    print(primary_asa.startup_config_errors())

    # tech support license
    print(primary_asa.show_tech_support_license())

    # cpu detailed
    print(primary_asa.show_cpu_detailed())

    # cpu usage
    print(primary_asa.show_cpu_usage())

    # memory region
    print(primary_asa.show_memory_region())

    print(primary_asa.show_service_policy())


if __name__ == "__main__":
    run_demo()
