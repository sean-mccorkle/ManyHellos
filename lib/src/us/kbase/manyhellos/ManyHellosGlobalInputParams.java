
package us.kbase.manyhellos;

import java.util.HashMap;
import java.util.Map;
import javax.annotation.Generated;
import com.fasterxml.jackson.annotation.JsonAnyGetter;
import com.fasterxml.jackson.annotation.JsonAnySetter;
import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * <p>Original spec-file type: ManyHellos_globalInputParams</p>
 * <pre>
 * prepare()
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "msg",
    "num_jobs",
    "workspace"
})
public class ManyHellosGlobalInputParams {

    @JsonProperty("msg")
    private String msg;
    @JsonProperty("num_jobs")
    private Long numJobs;
    @JsonProperty("workspace")
    private String workspace;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("msg")
    public String getMsg() {
        return msg;
    }

    @JsonProperty("msg")
    public void setMsg(String msg) {
        this.msg = msg;
    }

    public ManyHellosGlobalInputParams withMsg(String msg) {
        this.msg = msg;
        return this;
    }

    @JsonProperty("num_jobs")
    public Long getNumJobs() {
        return numJobs;
    }

    @JsonProperty("num_jobs")
    public void setNumJobs(Long numJobs) {
        this.numJobs = numJobs;
    }

    public ManyHellosGlobalInputParams withNumJobs(Long numJobs) {
        this.numJobs = numJobs;
        return this;
    }

    @JsonProperty("workspace")
    public String getWorkspace() {
        return workspace;
    }

    @JsonProperty("workspace")
    public void setWorkspace(String workspace) {
        this.workspace = workspace;
    }

    public ManyHellosGlobalInputParams withWorkspace(String workspace) {
        this.workspace = workspace;
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
        return ((((((((("ManyHellosGlobalInputParams"+" [msg=")+ msg)+", numJobs=")+ numJobs)+", workspace=")+ workspace)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
