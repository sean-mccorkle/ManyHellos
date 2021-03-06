
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
 * <p>Original spec-file type: ManyHellosInputParams</p>
 * <pre>
 * hello_msg - what to print as the message,
 * time_limit - how long the program will run, in seconds,
 * workspace - used to store report(s).
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "hello_msg",
    "num_jobs",
    "time_limit",
    "workspace"
})
public class ManyHellosInputParams {

    @JsonProperty("hello_msg")
    private String helloMsg;
    @JsonProperty("num_jobs")
    private Long numJobs;
    @JsonProperty("time_limit")
    private Long timeLimit;
    @JsonProperty("workspace")
    private String workspace;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("hello_msg")
    public String getHelloMsg() {
        return helloMsg;
    }

    @JsonProperty("hello_msg")
    public void setHelloMsg(String helloMsg) {
        this.helloMsg = helloMsg;
    }

    public ManyHellosInputParams withHelloMsg(String helloMsg) {
        this.helloMsg = helloMsg;
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

    public ManyHellosInputParams withNumJobs(Long numJobs) {
        this.numJobs = numJobs;
        return this;
    }

    @JsonProperty("time_limit")
    public Long getTimeLimit() {
        return timeLimit;
    }

    @JsonProperty("time_limit")
    public void setTimeLimit(Long timeLimit) {
        this.timeLimit = timeLimit;
    }

    public ManyHellosInputParams withTimeLimit(Long timeLimit) {
        this.timeLimit = timeLimit;
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

    public ManyHellosInputParams withWorkspace(String workspace) {
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
        return ((((((((((("ManyHellosInputParams"+" [helloMsg=")+ helloMsg)+", numJobs=")+ numJobs)+", timeLimit=")+ timeLimit)+", workspace=")+ workspace)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
