#!/usr/bin/python
# -*- coding: utf-8 -*-

import re

import sys

import requests

es_config_path = 'esconf.yml'


def es_nodename():
    try:
        esconf = open(es_config_path, 'r').read()
        es_nodename = re.search(r'(node\.name:\s\")(\w+)(\")', esconf).group(2)
        return es_nodename
    except:
        print("Link to Elastic config file is BAD or missing")


url = 'https://my.server.com:9200/_nodes/%s/stats/_all' % es_nodename()

try:
    r = requests.get(url, auth=('admin', 'admin'), timeout=(3, 10))
    data = r.json()
except:
    print('!!! CRITICAL ERROR : Requests module has problem with reading data from source !!!')


def get_NodeID():
    for node in data['nodes']:
        return str(node)


def no_Argument():
    print("!ERROR! Use this Script with arguments like : SCRIPT.PY status")


def main(argv):
    if not argv:
        no_Argument()
    for arg in argv:

        if arg.lower() == 'all':
            try:
                print data
            except:
                print("ERROR : Get Node ALL Status")
            exit(1)

        elif arg.lower() == 'node_id':
            print(get_NodeID())
            exit(1)

        elif arg.lower() == 'cluster_name':
            try:
                print(data['cluster_name'])
            except:
                print("ERROR : Get Cluster Name")
            exit(1)

        elif arg.lower() == 'node_name':
            try:
                print(data['nodes'][get_NodeID()]['name'])
            except:
                print("ERROR : Get Node Name")
            exit(1)

        elif arg.lower() == 'node_transaddress':
            try:
                print(data['nodes'][get_NodeID()]['transport_address'])
            except:
                print("ERROR : Get Node Transport Address")
            exit(1)

        elif arg.lower() == 'node_host':
            try:
                print(data['nodes'][get_NodeID()]['host'])
            except:
                print("ERROR : Get Node host")
            exit(1)

        elif arg.lower() == 'node_master':
            try:
                print(data['nodes'][get_NodeID()]['attributes']['master'])
            except:
                print("ERROR : Get Node Master Info")
            exit(1)

        elif arg.lower() == 'indices_docs_count':
            try:
                print(data['nodes'][get_NodeID()]['indices']['docs']['count'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_docs_deleted':
            try:
                print(data['nodes'][get_NodeID()]['indices']['docs']['deleted'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_store_size':
            try:
                print(data['nodes'][get_NodeID()]['indices']['store']['size_in_bytes'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_store_thtime':
            try:
                print(data['nodes'][get_NodeID()]['indices']['store']['throttle_time_in_millis'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_index_total':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['index_total'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_index_time':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['index_time_in_millis'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_index_current':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['index_current'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_delete_total':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['delete_total'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_delete_time':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['delete_time_in_millis'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_delete_current':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['delete_current'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_noop_update_total':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['noop_update_total'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_is_throttled':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['is_throttled'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        elif arg.lower() == 'indices_indexing_thtime':
            try:
                print(data['nodes'][get_NodeID()]['indices']['indexing']['throttle_time_in_millis'])
            except:
                print("ERROR : Get Indices data")
            exit(1)

        else:
            no_Argument()


if __name__ == "__main__":
    main(sys.argv[1:])
