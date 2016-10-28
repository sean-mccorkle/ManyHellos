
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
 * <p>Original spec-file type: ManyHellos_task</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "msg",
    "job_number",
    "workspace"
})
public class ManyHellosTask {

    @JsonProperty("msg")
    private String msg;
    @JsonProperty("job_number")
    private Long jobNumber;
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

    public ManyHellosTask withMsg(String msg) {
        this.msg = msg;
        return this;
    }

    @JsonProperty("job_number")
    public Long getJobNumber() {
        return jobNumber;
    }

    @JsonProperty("job_number")
    public void setJobNumber(Long jobNumber) {
        this.jobNumber = jobNumber;
    }

    public ManyHellosTask withJobNumber(Long jobNumber) {
        this.jobNumber = jobNumber;
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

    public ManyHellosTask withWorkspace(String workspace) {
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
        return ((((((((("ManyHellosTask"+" [msg=")+ msg)+", jobNumber=")+ jobNumber)+", workspace=")+ workspace)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
