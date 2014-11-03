#!/usr/bin/python

import argparse
import os

from pylab import *
from numpy import *

'''
Performance_Plot.py (python)
-------------------------

Creates charts for collected data

Description

usage:

    python Performance_Plot.py <parameters>

    -f -- raw data file
          This data file must be collected by performance tool
'''

class Performance_Plot():

    # nodes num range from 1 to 32
    node_nums = [1, 2, 4, 8, 16, 24, 32]
    # data used to draw graph
    # 'data' indicates if nova or euca has data inside
    data = {'nova': {'small': {}, 'medium': {}, 'large': {}, 'data': False}, 
            'euca': {'small': {}, 'medium': {}, 'large': {}, 'data': False}}

    def process_data(self, file_name):
        '''
        Process data

        Data will have the following format
        Data is a dict, it has two keys nova and euca, value for each key
        is also a dict, contains key (small, medium, large and data).
        The value for each key (small, medium large) is also dict, node number
        is key, each value (t_total, t_setup_install ...) is a list, which contains
        result of each corresponding experiment
        
        for example:
            'nova': {'small':{'1': {'t_total': [], ......}, .....}, ......}
        '''
        # check input file
        if not os.path.isfile(os.path.expanduser(file_name)):
            print "%s does not exist" % os.path.expanduser(file_name)
            sys.exit()

        # Read data from file
        with open(os.path.expanduser(file_name)) as input:
                content = input.readlines()

        for line in content:
            values = line.split('\n')[0].split('\t')
            test_name = values[0].strip()
            
            if test_name.find('nova') >= 0 or \
                test_name.find('euca') >= 0:
                if not self.get_node_num(test_name) in self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)]:
                    self.data[self.get_cloud(test_name)]['data'] = True
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)] = {}
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_total'] = [float(values[1].strip())]
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_setup_install'] = [float(values[2].strip())]
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_setup_configure'] = [float(values[3].strip())]
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_execute'] = [float(values[4].strip())]
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_shutdown'] = [float(values[5].strip())]
                    if self.get_cloud(test_name) == 'nova':
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_setup_getip'] = [float(values[6].strip())]
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_ipfail'] = [float(values[7].strip())]
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_ipchange'] = [float(values[8].strip())]
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_restart'] = [float(values[9].strip())]
                else:
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_total'].append(float(values[1].strip()))
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_setup_install'].append(float(values[2].strip()))
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_setup_configure'].append(float(values[3].strip()))
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_execute'].append(float(values[4].strip()))
                    self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_shutdown'].append(float(values[5].strip()))
                    if self.get_cloud(test_name) == 'nova':
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_setup_getip'].append(float(values[6].strip()))
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_ipfail'].append(float(values[7].strip()))
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_ipchange'].append(float(values[8].strip()))
                        self.data[self.get_cloud(test_name)][self.get_instance_type(test_name)][self.get_node_num(test_name)]['t_restart'].append(float(values[9].strip()))

    def produce_graphs(self, args):
        self.process_data(args.file)
        cloud_list = ['nova', 'euca']
        instance_type_list = ['small','medium', 'large']

        # draw common graph for euca and nova
        for cloud in cloud_list:
            for instance_type in instance_type_list:
                self.produce_one_graph(cloud, instance_type, 't_total')
                self.produce_one_graph(cloud, instance_type, 't_setup_install')
                self.produce_one_graph(cloud, instance_type, 't_setup_configure')
                self.produce_one_graph(cloud, instance_type, 't_execute')
                self.produce_one_graph(cloud, instance_type, 't_shutdown')

        # draw special graph for nova
        for instance_type in instance_type_list:
            self.produce_one_graph('nova', instance_type, 't_setup_getip')
            self.produce_one_graph('nova', instance_type, 't_ipfail')
            self.produce_one_graph('nova', instance_type, 't_ipchange')
            self.produce_one_graph('nova', instance_type, 't_restart')
        
        
    def get_node_num(self, test_name):
        # parse node number
        return int(test_name.split('-')[-1])
    
    def get_instance_type(self, test_name):
        # parse instance type
        return test_name.split('-')[-2].split('.')[-1]
    
    def get_cloud(self, test_name):
        # pase  cloud name
        return test_name.split('-')[0]
    
    def produce_one_graph(self, cloud, instance_type, key):

        if self.data[cloud]['data']:
            processed_data = []
            for node_num in self.node_nums:
                if node_num in self.data[cloud][instance_type]:
                    processed_data.append(self.data[cloud][instance_type][node_num][key])
                else:
                    processed_data.append([])
    
            figure()
            x_label = [1, 2, 4, 8, 16, 24, 32]
            ax = gca()
            ax.boxplot(processed_data)
            plt.setp(ax, xticklabels=x_label)
            ax.set_title('%s-%s-instances: %s' % (cloud, instance_type, key))
            ax.set_xlabel('Node Number')
            ax.set_ylabel('Time (Seconds)')
            savefig('%s-%s-%s.png' % (cloud, instance_type, key))

def main():
    PP = Performance_Plot()
    parser = argparse.ArgumentParser(description='Performance test tool -- Draw graph')
    parser.add_argument('-f', '--file', action='store',
                        required=True,
                        help='Performance test raw data')
    parser.set_defaults(func=PP.produce_graphs)
    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()