package alien4cloud.paas.cloudify3.model;

import javax.validation.constraints.NotNull;

import lombok.AllArgsConstructor;
import lombok.EqualsAndHashCode;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.ToString;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@Getter
@Setter
@ToString
@NoArgsConstructor
@AllArgsConstructor
@EqualsAndHashCode
@JsonIgnoreProperties(ignoreUnknown = true)
@SuppressWarnings("PMD.UnusedPrivateField")
public class StorageTemplate implements ICloudResourceTemplate {

    @NotNull
    private String id;

    @NotNull
    private Long size;

    private String device;

    private String description;
}