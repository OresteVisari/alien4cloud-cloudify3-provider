from cloudify.decorators import workflow
from cloudify.workflows import ctx
from cloudify.workflows import tasks as workflow_tasks
from utils import set_state_task
from utils import operation_task
from utils import link_tasks
from utils import CustomContext


@workflow
def a4c_install(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_install(ctx, graph, custom_context)
    return graph.execute()


@workflow
def a4c_uninstall(**kwargs):
    graph = ctx.graph_mode()
    custom_context = CustomContext(ctx)
    ctx.internal.send_workflow_event(
        event_type='workflow_started',
        message="Starting A4C generated '{0}' workflow execution".format(ctx.workflow_id))
    _a4c_uninstall(ctx, graph, custom_context)
    return graph.execute()


def _a4c_install(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    set_state_task(ctx, graph, 'Tomcat', 'created', 'Tomcat_created', custom_context)
    operation_task(ctx, graph, 'Java', 'cloudify.interfaces.lifecycle.start', 'start_Java', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'starting', 'Artifact_Directory_Test_starting', custom_context)
    set_state_task(ctx, graph, 'Server', 'configuring', 'Server_configuring', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.create', 'create_Server', custom_context)
    set_state_task(ctx, graph, 'Server', 'started', 'Server_started', custom_context)
    set_state_task(ctx, graph, 'Server', 'initial', 'Server_initial', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'created', 'Artifact_Directory_Test_created', custom_context)
    set_state_task(ctx, graph, 'Java', 'configured', 'Java_configured', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'starting', 'Tomcat_starting', custom_context)
    operation_task(ctx, graph, 'Tomcat', 'cloudify.interfaces.lifecycle.configure', 'configure_Tomcat', custom_context)
    set_state_task(ctx, graph, 'Java', 'configuring', 'Java_configuring', custom_context)
    operation_task(ctx, graph, 'War', 'cloudify.interfaces.lifecycle.configure', 'configure_War', custom_context)
    operation_task(ctx, graph, 'Artifact_Directory_Test', 'cloudify.interfaces.lifecycle.start', 'start_Artifact_Directory_Test', custom_context)
    set_state_task(ctx, graph, 'Server', 'created', 'Server_created', custom_context)
    set_state_task(ctx, graph, 'Java', 'starting', 'Java_starting', custom_context)
    set_state_task(ctx, graph, 'War', 'configured', 'War_configured', custom_context)
    operation_task(ctx, graph, 'Tomcat', 'cloudify.interfaces.lifecycle.start', 'start_Tomcat', custom_context)
    operation_task(ctx, graph, 'War', 'cloudify.interfaces.lifecycle.create', 'create_War', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'configuring', '_a4c_floating_ip_Server_configuring', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'creating', 'Tomcat_creating', custom_context)
    operation_task(ctx, graph, 'Artifact_Directory_Test', 'cloudify.interfaces.lifecycle.configure', 'configure_Artifact_Directory_Test', custom_context)
    set_state_task(ctx, graph, 'War', 'starting', 'War_starting', custom_context)
    set_state_task(ctx, graph, 'War', 'configuring', 'War_configuring', custom_context)
    set_state_task(ctx, graph, 'Server', 'creating', 'Server_creating', custom_context)
    operation_task(ctx, graph, 'War', 'cloudify.interfaces.lifecycle.start', 'start_War', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.start', 'start_Server', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'configured', '_a4c_floating_ip_Server_configured', custom_context)
    operation_task(ctx, graph, '_a4c_floating_ip_Server', 'cloudify.interfaces.lifecycle.start', 'start__a4c_floating_ip_Server', custom_context)
    operation_task(ctx, graph, 'Artifact_Directory_Test', 'cloudify.interfaces.lifecycle.create', 'create_Artifact_Directory_Test', custom_context)
    set_state_task(ctx, graph, 'Java', 'created', 'Java_created', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'initial', '_a4c_floating_ip_Server_initial', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'configuring', 'Tomcat_configuring', custom_context)
    set_state_task(ctx, graph, 'War', 'initial', 'War_initial', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'configured', 'Artifact_Directory_Test_configured', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.configure', 'configure_Server', custom_context)
    operation_task(ctx, graph, '_a4c_floating_ip_Server', 'cloudify.interfaces.lifecycle.configure', 'configure__a4c_floating_ip_Server', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'starting', '_a4c_floating_ip_Server_starting', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'started', 'Artifact_Directory_Test_started', custom_context)
    set_state_task(ctx, graph, 'War', 'started', 'War_started', custom_context)
    operation_task(ctx, graph, 'Java', 'cloudify.interfaces.lifecycle.configure', 'configure_Java', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'creating', '_a4c_floating_ip_Server_creating', custom_context)
    set_state_task(ctx, graph, 'Server', 'starting', 'Server_starting', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'initial', 'Artifact_Directory_Test_initial', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'creating', 'Artifact_Directory_Test_creating', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'initial', 'Tomcat_initial', custom_context)
    set_state_task(ctx, graph, 'War', 'creating', 'War_creating', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'configuring', 'Artifact_Directory_Test_configuring', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'configured', 'Tomcat_configured', custom_context)
    operation_task(ctx, graph, 'Java', 'cloudify.interfaces.lifecycle.create', 'create_Java', custom_context)
    operation_task(ctx, graph, 'Tomcat', 'cloudify.interfaces.lifecycle.create', 'create_Tomcat', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'started', 'Tomcat_started', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'started', '_a4c_floating_ip_Server_started', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'created', '_a4c_floating_ip_Server_created', custom_context)
    set_state_task(ctx, graph, 'Java', 'initial', 'Java_initial', custom_context)
    operation_task(ctx, graph, '_a4c_floating_ip_Server', 'cloudify.interfaces.lifecycle.create', 'create__a4c_floating_ip_Server', custom_context)
    set_state_task(ctx, graph, 'Java', 'creating', 'Java_creating', custom_context)
    set_state_task(ctx, graph, 'Server', 'configured', 'Server_configured', custom_context)
    set_state_task(ctx, graph, 'War', 'created', 'War_created', custom_context)
    set_state_task(ctx, graph, 'Java', 'started', 'Java_started', custom_context)
    link_tasks(graph, 'Tomcat_created', 'create_Tomcat', custom_context)
    link_tasks(graph, 'start_Java', 'Java_starting', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_starting', 'Artifact_Directory_Test_configured', custom_context)
    link_tasks(graph, 'Server_configuring', 'Server_created', custom_context)
    link_tasks(graph, 'Server_configuring', '_a4c_floating_ip_Server_started', custom_context)
    link_tasks(graph, 'create_Server', 'Server_creating', custom_context)
    link_tasks(graph, 'Server_started', 'start_Server', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_created', 'create_Artifact_Directory_Test', custom_context)
    link_tasks(graph, 'Java_configured', 'configure_Java', custom_context)
    link_tasks(graph, 'Tomcat_starting', 'Tomcat_configured', custom_context)
    link_tasks(graph, 'configure_Tomcat', 'Tomcat_configuring', custom_context)
    link_tasks(graph, 'Java_configuring', 'Tomcat_created', custom_context)
    link_tasks(graph, 'Java_configuring', 'Java_created', custom_context)
    link_tasks(graph, 'configure_War', 'War_configuring', custom_context)
    link_tasks(graph, 'start_Artifact_Directory_Test', 'Artifact_Directory_Test_starting', custom_context)
    link_tasks(graph, 'Server_created', 'create_Server', custom_context)
    link_tasks(graph, 'Java_starting', 'Java_configured', custom_context)
    link_tasks(graph, 'War_configured', 'configure_War', custom_context)
    link_tasks(graph, 'start_Tomcat', 'Tomcat_starting', custom_context)
    link_tasks(graph, 'create_War', 'War_creating', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_configuring', '_a4c_floating_ip_Server_created', custom_context)
    link_tasks(graph, 'Tomcat_creating', 'Tomcat_initial', custom_context)
    link_tasks(graph, 'configure_Artifact_Directory_Test', 'Artifact_Directory_Test_configuring', custom_context)
    link_tasks(graph, 'War_starting', 'War_configured', custom_context)
    link_tasks(graph, 'War_configuring', 'War_created', custom_context)
    link_tasks(graph, 'Server_creating', 'Server_initial', custom_context)
    link_tasks(graph, 'start_War', 'War_starting', custom_context)
    link_tasks(graph, 'start_Server', 'Server_starting', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_configured', 'configure__a4c_floating_ip_Server', custom_context)
    link_tasks(graph, 'start__a4c_floating_ip_Server', '_a4c_floating_ip_Server_starting', custom_context)
    link_tasks(graph, 'create_Artifact_Directory_Test', 'Artifact_Directory_Test_creating', custom_context)
    link_tasks(graph, 'Java_created', 'create_Java', custom_context)
    link_tasks(graph, 'Tomcat_configuring', 'Tomcat_created', custom_context)
    link_tasks(graph, 'Tomcat_configuring', 'Java_started', custom_context)
    link_tasks(graph, 'War_initial', 'Tomcat_started', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_configured', 'configure_Artifact_Directory_Test', custom_context)
    link_tasks(graph, 'configure_Server', 'Server_configuring', custom_context)
    link_tasks(graph, 'configure__a4c_floating_ip_Server', '_a4c_floating_ip_Server_configuring', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_starting', '_a4c_floating_ip_Server_configured', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_started', 'start_Artifact_Directory_Test', custom_context)
    link_tasks(graph, 'War_started', 'start_War', custom_context)
    link_tasks(graph, 'configure_Java', 'Java_configuring', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_creating', '_a4c_floating_ip_Server_initial', custom_context)
    link_tasks(graph, 'Server_starting', 'Server_configured', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_initial', 'Server_started', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_creating', 'Artifact_Directory_Test_initial', custom_context)
    link_tasks(graph, 'Tomcat_initial', 'Server_started', custom_context)
    link_tasks(graph, 'War_creating', 'War_initial', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_configuring', 'Artifact_Directory_Test_created', custom_context)
    link_tasks(graph, 'Tomcat_configured', 'configure_Tomcat', custom_context)
    link_tasks(graph, 'create_Java', 'Java_creating', custom_context)
    link_tasks(graph, 'create_Tomcat', 'Tomcat_creating', custom_context)
    link_tasks(graph, 'Tomcat_started', 'start_Tomcat', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_started', 'start__a4c_floating_ip_Server', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_created', 'create__a4c_floating_ip_Server', custom_context)
    link_tasks(graph, 'Java_initial', 'Server_started', custom_context)
    link_tasks(graph, 'create__a4c_floating_ip_Server', '_a4c_floating_ip_Server_creating', custom_context)
    link_tasks(graph, 'Java_creating', 'Java_initial', custom_context)
    link_tasks(graph, 'Server_configured', 'configure_Server', custom_context)
    link_tasks(graph, 'War_created', 'create_War', custom_context)
    link_tasks(graph, 'Java_started', 'start_Java', custom_context)


def _a4c_uninstall(ctx, graph, custom_context):
    #  following code can be pasted in src/test/python/workflows/tasks.py for simulation
    set_state_task(ctx, graph, 'Tomcat', 'deleted', 'Tomcat_deleted', custom_context)
    set_state_task(ctx, graph, 'Server', 'stopped', 'Server_stopped', custom_context)
    set_state_task(ctx, graph, 'War', 'deleting', 'War_deleting', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'deleting', 'Artifact_Directory_Test_deleting', custom_context)
    set_state_task(ctx, graph, 'Server', 'stopping', 'Server_stopping', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'deleting', '_a4c_floating_ip_Server_deleting', custom_context)
    set_state_task(ctx, graph, 'Server', 'deleting', 'Server_deleting', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'deleted', '_a4c_floating_ip_Server_deleted', custom_context)
    set_state_task(ctx, graph, 'Java', 'deleting', 'Java_deleting', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'stopping', 'Tomcat_stopping', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'deleted', 'Artifact_Directory_Test_deleted', custom_context)
    operation_task(ctx, graph, '_a4c_floating_ip_Server', 'cloudify.interfaces.lifecycle.delete', 'delete__a4c_floating_ip_Server', custom_context)
    set_state_task(ctx, graph, 'War', 'stopping', 'War_stopping', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'stopped', 'Artifact_Directory_Test_stopped', custom_context)
    operation_task(ctx, graph, 'Tomcat', 'cloudify.interfaces.lifecycle.stop', 'stop_Tomcat', custom_context)
    set_state_task(ctx, graph, 'Server', 'deleted', 'Server_deleted', custom_context)
    set_state_task(ctx, graph, 'Artifact_Directory_Test', 'stopping', 'Artifact_Directory_Test_stopping', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'stopping', '_a4c_floating_ip_Server_stopping', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'deleting', 'Tomcat_deleting', custom_context)
    set_state_task(ctx, graph, '_a4c_floating_ip_Server', 'stopped', '_a4c_floating_ip_Server_stopped', custom_context)
    set_state_task(ctx, graph, 'Java', 'stopped', 'Java_stopped', custom_context)
    set_state_task(ctx, graph, 'Java', 'stopping', 'Java_stopping', custom_context)
    set_state_task(ctx, graph, 'War', 'deleted', 'War_deleted', custom_context)
    set_state_task(ctx, graph, 'Tomcat', 'stopped', 'Tomcat_stopped', custom_context)
    operation_task(ctx, graph, '_a4c_floating_ip_Server', 'cloudify.interfaces.lifecycle.stop', 'stop__a4c_floating_ip_Server', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.stop', 'stop_Server', custom_context)
    operation_task(ctx, graph, 'Server', 'cloudify.interfaces.lifecycle.delete', 'delete_Server', custom_context)
    set_state_task(ctx, graph, 'Java', 'deleted', 'Java_deleted', custom_context)
    set_state_task(ctx, graph, 'War', 'stopped', 'War_stopped', custom_context)
    link_tasks(graph, 'Tomcat_deleted', 'Tomcat_deleting', custom_context)
    link_tasks(graph, 'Server_stopped', 'stop_Server', custom_context)
    link_tasks(graph, 'War_deleting', 'War_stopped', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_deleting', 'Artifact_Directory_Test_stopped', custom_context)
    link_tasks(graph, 'Server_stopping', 'Tomcat_deleted', custom_context)
    link_tasks(graph, 'Server_stopping', 'Artifact_Directory_Test_deleted', custom_context)
    link_tasks(graph, 'Server_stopping', 'Java_deleted', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_deleting', '_a4c_floating_ip_Server_stopped', custom_context)
    link_tasks(graph, 'Server_deleting', 'Server_stopped', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_deleted', 'delete__a4c_floating_ip_Server', custom_context)
    link_tasks(graph, 'Java_deleting', 'Java_stopped', custom_context)
    link_tasks(graph, 'Tomcat_stopping', 'War_deleted', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_deleted', 'Artifact_Directory_Test_deleting', custom_context)
    link_tasks(graph, 'delete__a4c_floating_ip_Server', '_a4c_floating_ip_Server_deleting', custom_context)
    link_tasks(graph, 'Artifact_Directory_Test_stopped', 'Artifact_Directory_Test_stopping', custom_context)
    link_tasks(graph, 'stop_Tomcat', 'Tomcat_stopping', custom_context)
    link_tasks(graph, 'Server_deleted', 'delete_Server', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_stopping', 'Server_deleted', custom_context)
    link_tasks(graph, 'Tomcat_deleting', 'Tomcat_stopped', custom_context)
    link_tasks(graph, '_a4c_floating_ip_Server_stopped', 'stop__a4c_floating_ip_Server', custom_context)
    link_tasks(graph, 'Java_stopped', 'Java_stopping', custom_context)
    link_tasks(graph, 'War_deleted', 'War_deleting', custom_context)
    link_tasks(graph, 'Tomcat_stopped', 'stop_Tomcat', custom_context)
    link_tasks(graph, 'stop__a4c_floating_ip_Server', '_a4c_floating_ip_Server_stopping', custom_context)
    link_tasks(graph, 'stop_Server', 'Server_stopping', custom_context)
    link_tasks(graph, 'delete_Server', 'Server_deleting', custom_context)
    link_tasks(graph, 'Java_deleted', 'Java_deleting', custom_context)
    link_tasks(graph, 'War_stopped', 'War_stopping', custom_context)


#following code can be pasted in src/test/python/workflows/context.py for simulation
#def _build_nodes(ctx):
    #types = []
    #types.append('alien.nodes.WarWithLifeCycleScript')
    #types.append('alien.nodes.War')
    #types.append('alien.nodes.LoadBalancedWebApplication')
    #types.append('tosca.nodes.Root')
    #node_War = _build_node(ctx, 'War', types, 1)
    #types = []
    #types.append('alien.nodes.TestArtifactDirectory')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_Artifact_Directory_Test = _build_node(ctx, 'Artifact_Directory_Test', types, 1)
    #types = []
    #types.append('alien.nodes.Tomcat')
    #types.append('tosca.nodes.WebServer')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_Tomcat = _build_node(ctx, 'Tomcat', types, 1)
    #types = []
    #types.append('tosca.nodes.Network')
    #types.append('tosca.nodes.Root')
    #node_NetPub = _build_node(ctx, 'NetPub', types, 1)
    #types = []
    #types.append('tosca.nodes.Compute')
    #types.append('tosca.nodes.Root')
    #node_Server = _build_node(ctx, 'Server', types, 1)
    #types = []
    #types.append('alien.nodes.Java')
    #types.append('tosca.nodes.SoftwareComponent')
    #types.append('tosca.nodes.Root')
    #node_Java = _build_node(ctx, 'Java', types, 1)
    #_add_relationship(node_War, node_Tomcat)
    #_add_relationship(node_Artifact_Directory_Test, node_Server)
    #_add_relationship(node_Tomcat, node_Java)
    #_add_relationship(node_Tomcat, node_Server)
    #_add_relationship(node_Server, node_NetPub)
    #_add_relationship(node_Java, node_Server)
