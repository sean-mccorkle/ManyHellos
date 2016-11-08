
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
import us.kbase.common.service.Tuple2;


/**
 * <p>Original spec-file type: ManyHellos_globalResult</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "output",
    "jobs"
})
public class ManyHellosGlobalResult {

    @JsonProperty("output")
    private java.lang.String output;
    @JsonProperty("jobs")
    private List<Tuple2 <Long, String>> jobs;
    private Map<java.lang.String, Object> additionalProperties = new HashMap<java.lang.String, Object>();

    @JsonProperty("output")
    public java.lang.String getOutput() {
        return output;
    }

    @JsonProperty("output")
    public void setOutput(java.lang.String output) {
        this.output = output;
    }

    public ManyHellosGlobalResult withOutput(java.lang.String output) {
        this.output = output;
        return this;
    }

    @JsonProperty("jobs")
    public List<Tuple2 <Long, String>> getJobs() {
        return jobs;
    }

    @JsonProperty("jobs")
    public void setJobs(List<Tuple2 <Long, String>> jobs) {
        this.jobs = jobs;
    }

    public ManyHellosGlobalResult withJobs(List<Tuple2 <Long, String>> jobs) {
        this.jobs = jobs;
        return this;
    }

    @JsonAnyGetter
    public Map<java.lang.String, Object> getAdditionalProperties() {
        return this.additionalProperties;
    }

    @JsonAnySetter
    public void setAdditionalProperties(java.lang.String name, Object value) {
        this.additionalProperties.put(name, value);
    }

    @Override
    public java.lang.String toString() {
        return ((((((("ManyHellosGlobalResult"+" [output=")+ output)+", jobs=")+ jobs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
