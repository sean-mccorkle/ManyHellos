
package us.kbase.manyhellos;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: ManyHellos_prepareSchedule</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "tasks",
    "collect_method"
})
public class ManyHellosPrepareSchedule {

    @JsonProperty("tasks")
    private List<ManyHellosRunEachInput> tasks;
    /**
     * <p>Original spec-file type: FullMethodQualifier</p>
     * 
     * 
     */
    @JsonProperty("collect_method")
    private FullMethodQualifier collectMethod;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("tasks")
    public List<ManyHellosRunEachInput> getTasks() {
        return tasks;
    }

    @JsonProperty("tasks")
    public void setTasks(List<ManyHellosRunEachInput> tasks) {
        this.tasks = tasks;
    }

    public ManyHellosPrepareSchedule withTasks(List<ManyHellosRunEachInput> tasks) {
        this.tasks = tasks;
        return this;
    }

    /**
     * <p>Original spec-file type: FullMethodQualifier</p>
     * 
     * 
     */
    @JsonProperty("collect_method")
    public FullMethodQualifier getCollectMethod() {
        return collectMethod;
    }

    /**
     * <p>Original spec-file type: FullMethodQualifier</p>
     * 
     * 
     */
    @JsonProperty("collect_method")
    public void setCollectMethod(FullMethodQualifier collectMethod) {
        this.collectMethod = collectMethod;
    }

    public ManyHellosPrepareSchedule withCollectMethod(FullMethodQualifier collectMethod) {
        this.collectMethod = collectMethod;
        return this;
    }

    @JsonAnyGetter
    public Map<String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public String toString() {
        return ((((((("ManyHellosPrepareSchedule"+" [tasks=")+ tasks)+", collectMethod=")+ collectMethod)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
