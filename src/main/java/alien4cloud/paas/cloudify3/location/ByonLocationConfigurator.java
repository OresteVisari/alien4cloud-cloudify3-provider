package alien4cloud.paas.cloudify3.location;

import java.util.List;
import java.util.Map;
import java.util.Set;

import org.springframework.stereotype.Component;

import alien4cloud.model.deployment.matching.MatchingConfiguration;
import alien4cloud.model.orchestrators.locations.LocationResourceTemplate;
import alien4cloud.orchestrators.plugin.ILocationResourceAccessor;
import alien4cloud.orchestrators.plugin.model.PluginArchive;

import com.google.common.collect.Sets;

@Component
public class ByonLocationConfigurator implements ITypeAwareLocationConfigurator {

    @Override
    public List<PluginArchive> pluginArchives() {
        return null;
    }

    @Override
    public List<String> getResourcesTypes() {
        return null;
    }

    @Override
    public List<LocationResourceTemplate> instances(ILocationResourceAccessor resourceAccessor) {
        return null;
    }

    @Override
    public Set<String> getManagedLocationTypes() {
        return Sets.newHashSet("Byon");
    }

    @Override
    public Map<String, MatchingConfiguration> getMatchingConfigurations() {
        return null;
    }
}
