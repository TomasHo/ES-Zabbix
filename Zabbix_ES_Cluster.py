#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

import requests

try:
	cd = requests.get('https://my.server.com:9200/_cluster/state', auth=('admin', 'admin'), timeout=(3, 10))
	clusterdata = cd.json()
except:
	print('!!! CRITICAL ERROR : Requests module has problem with reading data from source !!!')


try:
	r = requests.get('https://my.server.com:9200/_cluster/stats', auth=('admin', 'admin'), timeout=(3, 10))
	data = r.json()
except:
	print('!!! CRITICAL ERROR : Requests module has problem with reading data from source !!!')


def get_MasterNodeID():
	try:
		return clusterdata['master_node']
	except:
		return "ERROR : Get Cluster Node ID"


def get_MasterNodeName():
	try:
		return clusterdata['nodes'][get_MasterNodeID()]['name']
	except:
		return "ERROR : Get Cluster Node Name"


def get_MasterNodeNodes():
	try:
		node_names = clusterdata['nodes']
		node_list=[]
		for node_name in node_names:
			node_list.append(clusterdata['nodes'][node_name]['name'])
		node_list.sort()
		return ', '.join(node_list)
	except:
		return "ERROR : Get Nodes in Cluster"

def get_Status():
	try:
		return data['status']
	except:
		return "ERROR : Get Cluster Status"


def get_StatusAll():
	try:
		return data
	except:
		return "ERROR : Get Cluster Status"


def get_ClusterName():
	try:
		return data['cluster_name']
	except:
		return "ERROR : Get Cluster Name"


def get_IndicesCount():
	try:
		return data['indices']['count']
	except:
		return "ERROR : Get Indices Count"


def get_ShardsTotal():
	try:
		return data['indices']['shards']['total']
	except:
		return "ERROR : Get shards Count"


def get_ShardsPrimary():
	try:
		return data['indices']['shards']['primaries']
	except:
		return "ERROR : Get shards Count"


def get_ShardsReplica():
	try:
		return data['indices']['shards']['replication']
	except:
		return "ERROR : Get shards Count"


def get_DocsCount():
	try:
		return data['indices']['docs']['count']
	except:
		return "ERROR : Get Docs Count"

def get_DocsDeleted():
	try:
		return data['indices']['docs']['deleted']
	except:
		return "ERROR : Get Docs Count"


def get_StoreSize():
	try:
		return data['indices']['store']['size_in_bytes']
	except:
		return "ERROR : Get Store Size"


def get_StoreThrottleTime():
	try:
		return data['indices']['store']['throttle_time_in_millis']
	except:
		return "ERROR : Get Store Throttle time in milis"


def get_FieldDataMemSize():
	try:
		return data['indices']['fielddata']['memory_size_in_bytes']
	except:
		return "ERROR : Get FieldData memory size"


def get_FilterCacheMemSize():
	try:
		return data['indices']['filter_cache']['memory_size_in_bytes']
	except:
		return "ERROR : Get FilterCache memory size"


def get_IdCacheMemSize():
	try:
		return data['indices']['id_cache']['memory_size_in_bytes']
	except:
		return "ERROR : Get ID Cache memory size"


def get_CompletionSize():
	try:
		return data['indices']['completion']['size_in_bytes']
	except:
		return "ERROR : Get completion size"

def get_SegmentsCount():
	try:
		return data['indices']['segments']['count']
	except:
		return "ERROR : Get Segments info"


def get_SegmentsMem():
	try:
		return data['indices']['segments']['memory_in_bytes']
	except:
		return "ERROR : Get Segments info"


def get_SegmentsIndexWMemory():
	try:
		return data['indices']['segments']['index_writer_memory_in_bytes']
	except:
		return "ERROR : Get Segments info"


def get_SegmentsIndexWmaxMemory():
	try:
		return data['indices']['segments']['index_writer_max_memory_in_bytes']
	except:
		return "ERROR : Get Segments info"


def get_SegmentsVerMapMem():
	try:
		return data['indices']['segments']['version_map_memory_in_bytes']
	except:
		return "ERROR : Get Segments info"


def get_SegmentsBitSetMem():
	try:
		return data['indices']['segments']['fixed_bit_set_memory_in_bytes']
	except:
		return "ERROR : Get Segments info"


def get_Plugins():
	try:
		plugin_names = data['nodes']['plugins']
		plugin_list=[]
		for plugin_name in plugin_names:
			plugin_list.append(plugin_name['name'].title())
		plugin_list.sort()
		return ', '.join(plugin_list)
	except:
		return "ERROR : Get Plugins installed"


def get_PercolateTotal():
	try:
		return data['indices']['percolate']['total']
	except:
		return "ERROR : Get Percolate info"


def get_PercolateTime():
	try:
		return data['indices']['percolate']['time_in_millis']
	except:
		return "ERROR : Get Percolate info"


def get_PercolateCurrent():
	try:
		return data['indices']['percolate']['current']
	except:
		return "ERROR : Get Percolate info"


def get_PercolateMemSize():
	try:
		return data['indices']['percolate']['memory_size_in_bytes']
	except:
		return "ERROR : Get Percolate info"


def get_PercolateQueries():
	try:
		return data['indices']['percolate']['queries']
	except:
		return "ERROR : Get Percolate info"


def get_NodesCountTotal():
	try:
		return data['nodes']['count']['total']
	except:
		return "ERROR : Get Nodes info"


def get_NodesCountMasterOnly():
	try:
		return data['nodes']['count']['master_only']
	except:
		return "ERROR : Get Nodes info"


def get_NodesCountDataOnly():
	try:
		return data['nodes']['count']['data_only']
	except:
		return "ERROR : Get Nodes info"


def get_NodesCountMasterData():
	try:
		return data['nodes']['count']['master_data']
	except:
		return "ERROR : Get Nodes info"


def get_NodesCountClient():
	try:
		return data['nodes']['count']['client']
	except:
		return "ERROR : Get Nodes info"


def no_Argument():
	print("!ERROR! Use this Script with arguments like : SCRIPT.PY status")
	print("Available arguments : all, status, name, indices, shards_total")


def main(argv):
	if not argv:
		no_Argument()
	for arg in argv:
		if arg.lower() == 'all':
			print(get_StatusAll())
			exit(1)
		elif arg.lower() == 'masternode_id':
			print(get_MasterNodeID())
			exit(1)
		elif arg.lower() == 'masternode_name':
			print(get_MasterNodeName())
			exit(1)
		elif arg.lower() == 'masternode_nodes':
			print(get_MasterNodeNodes())
			exit(1)
		elif arg.lower() == 'status':
			print(get_Status().upper())
			exit(1)
		elif arg.lower() == 'name':
			print(get_ClusterName())
			exit(1)
		elif arg.lower() == 'indices':
			print(get_IndicesCount())
			exit(1)
		elif arg.lower() == 'shards_total':
			print(get_ShardsTotal())
			exit(1)
		elif arg.lower() == 'shards_primary':
			print(get_ShardsPrimary())
			exit(1)
		elif arg.lower() == 'shards_replica':
			print(get_ShardsReplica())
			exit(1)
		elif arg.lower() == 'docs_count':
			print(get_DocsCount())
			exit(1)
		elif arg.lower() == 'docs_deleted':
			print(get_DocsDeleted())
			exit(1)
		elif arg.lower() == 'store_size':
			print(get_StoreSize())
			exit(1)
		elif arg.lower() == 'store_thtime':
			print(get_StoreThrottleTime())
			exit(1)
		elif arg.lower() == 'field_data':
			print(get_FieldDataMemSize())
			exit(1)
		elif arg.lower() == 'filter_cache':
			print(get_FilterCacheMemSize())
			exit(1)
		elif arg.lower() == 'idcache_memsize':
			print(get_IdCacheMemSize())
			exit(1)
		elif arg.lower() == 'completion_size':
			print(get_CompletionSize())
			exit(1)
		elif arg.lower() == 'plugins':
			print(get_Plugins())
			exit(1)
		elif arg.lower() == 'segments_count':
			print(get_SegmentsCount())
			exit(1)
		elif arg.lower() == 'segments_mem':
			print(get_SegmentsMem())
			exit(1)
		elif arg.lower() == 'segments_indexwmem':
			print(get_SegmentsIndexWMemory())
			exit(1)
		elif arg.lower() == 'segments_indexwmax':
			print(get_SegmentsIndexWmaxMemory())
			exit(1)
		elif arg.lower() == 'segments_vermapmem':
			print(get_SegmentsVerMapMem())
			exit(1)
		elif arg.lower() == 'segments_bitsetmem':
			print(get_SegmentsBitSetMem())
			exit(1)
		elif arg.lower() == 'percolate_total':
			print(get_PercolateTotal())
			exit(1)
		elif arg.lower() == 'percolate_time':
			print(get_PercolateTime())
			exit(1)
		elif arg.lower() == 'percolate_current':
			print(get_PercolateCurrent())
			exit(1)
		elif arg.lower() == 'percolate_memsize':
			print(get_PercolateMemSize())
			exit(1)
		elif arg.lower() == 'percolate_queries':
			print(get_PercolateQueries())
			exit(1)
		elif arg.lower() == 'nodes_total':
			print(get_NodesCountTotal())
			exit(1)
		elif arg.lower() == 'nodes_master':
			print(get_NodesCountMasterOnly())
			exit(1)
		elif arg.lower() == 'nodes_data':
			print(get_NodesCountDataOnly())
			exit(1)
		elif arg.lower() == 'nodes_masterdata':
			print(get_NodesCountMasterData())
			exit(1)
		elif arg.lower() == 'nodes_client':
			print(get_NodesCountClient())
			exit(1)
		else:
			no_Argument()


if __name__ == "__main__":
	main(sys.argv[1:])
