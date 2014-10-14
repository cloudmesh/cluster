#!/usr/bin/python
# -*- coding: utf-8 -*-
import argparse
import os
import csv

from numpy import *

class Performance_Static():

    nova_data = {}
    euca_data = {}

    def process_file(self, args):
        with open(os.path.expanduser(args.file)) as raw_input:
            content = raw_input.readlines()
        for line in content:
            values = line.split('\n')[0].split('\t')
            test_name = values[0].strip()

            # if nova data
            if values[0].find('nova') >= 0:
                if not test_name in self.nova_data:
                    self.nova_data[test_name] = {}
                    self.nova_data[test_name]['t_total'] = [float(values[1].strip())]
                    self.nova_data[test_name]['t_setup_install'] = [float(values[2].strip())]
                    self.nova_data[test_name]['t_setup_configure'] = [float(values[3].strip())]
                    self.nova_data[test_name]['t_execute'] = [float(values[4].strip())]
                    self.nova_data[test_name]['t_shutdown'] = [float(values[5].strip())]
                    self.nova_data[test_name]['t_setup_getip'] = [float(values[6].strip())]
                    self.nova_data[test_name]['t_ipfail'] = [float(values[7].strip())]
                    self.nova_data[test_name]['t_ipchange'] = [float(values[8].strip())]
                    self.nova_data[test_name]['t_restart'] = [float(values[9].strip())]
                else:
                    self.nova_data[test_name]['t_total'].append(float(values[1].strip()))
                    self.nova_data[test_name]['t_setup_install'].append(float(values[2].strip()))
                    self.nova_data[test_name]['t_setup_configure'].append(float(values[3].strip()))
                    self.nova_data[test_name]['t_execute'].append(float(values[4].strip()))
                    self.nova_data[test_name]['t_shutdown'].append(float(values[5].strip()))
                    self.nova_data[test_name]['t_setup_getip'].append(float(values[6].strip()))
                    self.nova_data[test_name]['t_ipfail'].append(float(values[7].strip()))
                    self.nova_data[test_name]['t_ipchange'].append(float(values[8].strip()))
                    self.nova_data[test_name]['t_restart'].append(float(values[9].strip()))
            # if euca_data
            if values[0].find('euca') >= 0:
                if not test_name in self.euca_data:
                    self.euca_data[test_name] = {}
                    self.euca_data[test_name]['t_total'] = [float(values[1].strip())]
                    self.euca_data[test_name]['t_setup_install'] = [float(values[2].strip())]
                    self.euca_data[test_name]['t_setup_configure'] = [float(values[3].strip())]
                    self.euca_data[test_name]['t_execute'] = [float(values[4].strip())]
                    self.euca_data[test_name]['t_shutdown'] = [float(values[5].strip())]
                else:
                    self.euca_data[test_name]['t_total'].append(float(values[1].strip()))
                    self.euca_data[test_name]['t_setup_install'].append(float(values[2].strip()))
                    self.euca_data[test_name]['t_setup_configure'].append(float(values[3].strip()))
                    self.euca_data[test_name]['t_execute'].append(float(values[4].strip()))
                    self.euca_data[test_name]['t_shutdown'].append(float(values[5].strip()))
        self.process_data_nova()
        self.process_data_euca()

    def process_data_nova(self):

        writer = csv.writer(file('performance_data_nova.csv', 'wb'))
        writer.writerow(['name',
                         't_total_avg',
                         't_total_min',
                         't_total_max',
                         't_total_stdev',
                         't_setup_getip_avg',
                         't_setup_getip_min',
                         't_setup_getip_max',
                         't_setup_getip_stdev',
                         't_setup_install_avg',
                         't_setup_install_min',
                         't_setup_install_max',
                         't_setup_install_stdev',
                         't_setup_configure_avg',
                         't_setup_configure_min',
                         't_setup_configure_max',
                         't_setup_configure_stdev',
                         't_ipfail_avg',
                         't_ipfail_min',
                         't_ipfail_max',
                         't_ipfail_stdev',
                         't_ipchange_avg',
                         't_ipchange_min',
                         't_ipchange_max',
                         't_ipchange_stdev',
                         't_termination_avg',
                         't_termination_min',
                         't_termination_max',
                         't_termination_stdev',
                         't_execute_avg',
                         't_execute_min',
                         't_execute_max',
                         't_execute_stdev',
                         't_shutdown_avg',
                         't_shutdown_min',
                         't_shutdown_max',
                         't_shutdown_stdev'])

        for performance_name, data in self.nova_data.items():
            writer.writerow([performance_name,
                             average(array(data['t_total'])),
                             array(data['t_total']).min(),
                             array(data['t_total']).max(),
                             std(array(data['t_total'])),
                             average(array(data['t_setup_getip'])),
                             array(data['t_setup_getip']).min(),
                             array(data['t_setup_getip']).max(),
                             std(array(data['t_setup_getip'])),
                             average(array(data['t_setup_install'])),
                             array(data['t_setup_install']).min(),
                             array(data['t_setup_install']).max(),
                             std(array(data['t_setup_install'])),
                             average(array(data['t_setup_configure'])),
                             array(data['t_setup_configure']).min(),
                             array(data['t_setup_configure']).max(),
                             std(array(data['t_setup_configure'])),
                             average(array(data['t_ipfail'])),
                             array(data['t_ipfail']).min(),
                             array(data['t_ipfail']).max(),
                             std(array(data['t_ipfail'])),
                             average(array(data['t_ipchange'])),
                             array(data['t_ipchange']).min(),
                             array(data['t_ipchange']).max(),
                             std(array(data['t_ipchange'])),
                             average(array(data['t_termination'])),
                             array(data['t_termination']).min(),
                             array(data['t_termination']).max(),
                             std(array(data['t_termination'])),
                             average(array(data['t_execute'])), 
                             array(data['t_execute']).min(),
                             array(data['t_execute']).max(),
                             std(array(data['t_execute'])),
                             average(array(data['t_shutdown'])),
                             array(data['t_shutdown']).min(),
                             array(data['t_shutdown']).max(),
                             std(array(data['t_shutdown'])),
                             ])

    def process_data_euca(self):
        writer = csv.writer(file('performance_data_euca.csv', 'wb'))
        writer.writerow(['name',
                         't_total_avg',
                         't_total_min',
                         't_total_max',
                         't_total_stdev',
                         't_setup_install_avg',
                         't_setup_install_min',
                         't_setup_install_max',
                         't_setup_install_stdev',
                         't_setup_configure_avg',
                         't_setup_configure_min',
                         't_setup_configure_max',
                         't_setup_configure_stdev',
                         't_execute_avg',
                         't_execute_min',
                         't_execute_max',
                         't_execute_stdev',
                         't_shutdown_avg',
                         't_shutdown_min',
                         't_shutdown_max',
                         't_shutdown_stdev'])

        for performance_name, data in self.euca_data.items():
            writer.writerow([performance_name,
                             average(array(data['t_total'])),
                             array(data['t_total']).min(),
                             array(data['t_total']).max(),
                             std(array(data['t_total'])),
                             average(array(data['t_setup_install'])),
                             array(data['t_setup_install']).min(),
                             array(data['t_setup_install']).max(),
                             std(array(data['t_setup_install'])),
                             average(array(data['t_setup_configure'])),
                             array(data['t_setup_configure']).min(),
                             array(data['t_setup_configure']).max(),
                             std(array(data['t_setup_configure'])),
                             average(array(data['t_execute'])),
                             array(data['t_execute']).min(),
                             array(data['t_execute']).max(),
                             std(array(data['t_execute'])),
                             average(array(data['t_shutdown'])),
                             array(data['t_shutdown']).min(),
                             array(data['t_shutdown']).max(),
                             std(array(data['t_shutdown'])),
                             ])

def main():
    PS = Performance_Static()
    parser = argparse.ArgumentParser(description='Performance test tool')
    parser.add_argument('-f', '--file', action='store',
                        required=True,
                        help='Performance test raw data')
    parser.set_defaults(func=PS.process_file)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()