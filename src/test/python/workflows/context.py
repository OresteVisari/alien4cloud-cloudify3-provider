from graph import Context
from graph import Node
from graph import Instance
from graph import Relationship
from graph import RelationshipIntance

def __build_nodes(ctx):
    types = []
    types.append('alien.nodes.DeletableConfigurableBlockStorage')
    types.append('alien.nodes.DeletableBlockStorage')
    types.append('tosca.nodes.BlockStorage')
    types.append('tosca.nodes.Root')
    node_DeletableConfigurableBlockStorage = _build_node(ctx, 'DeletableConfigurableBlockStorage', types, 1)
    types = []
    types.append('tosca.nodes.Network')
    types.append('tosca.nodes.Root')
    node_Network = _build_node(ctx, '_a4c_floating_ip_Compute', types, 1)
    types = []
    types.append('cloudify.nodes.Compute')
    types.append('tosca.nodes.Root')
    node_Compute = _build_node(ctx, 'Compute', types, 1)
    _add_relationship(node_DeletableConfigurableBlockStorage, node_Compute)
    _add_relationship(node_Compute, node_Network)
    types = []
    types.append('_a4c.cloudify.nodes.FileSystem')
    types.append('tosca.nodes.Root')
    node_FS = _build_node(ctx, '_a4c_file_system_DeletableConfigurableBlockStorage', types, 1)
    _add_relationship(node_FS, node_Compute)
    _add_relationship(node_FS, node_DeletableConfigurableBlockStorage)


# content of this fn can be generated by workflow plugin (see workflows.py in generated blueprint)
def _build_nodes(ctx):
    # just put the generated sequence here :
    types = []
    types.append('alien.nodes.ConfigurableBlockStorage')
    types.append('tosca.nodes.BlockStorage')
    types.append('tosca.nodes.Root')
    node_ConfigurableBlockStorage = _build_node(ctx, 'DeletableConfigurableBlockStorage', types, 1)
    types = []
    types.append('alien.nodes.Apache')
    types.append('tosca.nodes.WebServer')
    types.append('tosca.nodes.SoftwareComponent')
    types.append('tosca.nodes.Root')
    node_Apache = _build_node(ctx, 'Apache', types, 2)
    types = []
    types.append('alien.nodes.PHP')
    types.append('tosca.nodes.SoftwareComponent')
    types.append('tosca.nodes.Root')
    node_PHP = _build_node(ctx, 'PHP', types, 2)
    types = []
    types.append('tosca.nodes.Network')
    types.append('tosca.nodes.Root')
    node_Network = _build_node(ctx, '_a4c_floating_ip_Compute2', types, 1)
    types = []
    types.append('cloudify.nodes.Compute')
    types.append('tosca.nodes.Root')
    node_Compute2 = _build_node(ctx, 'Compute2', types, 2)
    types = []
    types.append('alien.nodes.Wordpress')
    types.append('tosca.nodes.WebApplication')
    types.append('tosca.nodes.Root')
    node_Wordpress = _build_node(ctx, 'Wordpress', types, 2)
    types = []
    types.append('cloudify.nodes.Compute')
    types.append('tosca.nodes.Root')
    node_Compute = _build_node(ctx, 'Compute', types, 1)
    types = []
    types.append('alien.nodes.Mysql')
    types.append('tosca.nodes.Database')
    types.append('tosca.nodes.Root')
    node_Mysql = _build_node(ctx, 'Mysql', types, 1)
    types = []
    types.append('_a4c.cloudify.nodes.FileSystem')
    node_fs =  _build_node(ctx, '_a4c_file_system_DeletableConfigurableBlockStorage', types, 1)
    _add_relationship(node_ConfigurableBlockStorage, node_Compute)
    _add_relationship(node_fs, node_Compute)
    _add_relationship(node_fs, node_ConfigurableBlockStorage)
    _add_relationship(node_Apache, node_Compute2)
    _add_relationship(node_PHP, node_Compute2)
    _add_relationship(node_Compute2, node_Network)
    _add_relationship(node_Wordpress, node_Apache)
    _add_relationship(node_Wordpress, node_PHP)
    _add_relationship(node_Wordpress, node_Mysql)
    _add_relationship(node_Mysql, node_Compute)


def build_context():
    ctx = Context()
    _build_nodes(ctx)
    return ctx


def _build_node(ctx, node_id, node_type, instance_count):
    node = Node(node_id, node_type)
    _build_intances(node, instance_count)
    ctx.nodes.append(node)
    return node


def _build_intances(node, instance_count):
    i = 0
    while i < instance_count:
        instance_id = node.id + str(i)
        instance = Instance(instance_id, node)
        node.instances.append(instance)
        i += 1


def _add_relationship(node, target_node):
    node.add_relationship(Relationship(target_node))
    for instance in node.instances:
        instance.relationships.append(RelationshipIntance(instance, target_node))
