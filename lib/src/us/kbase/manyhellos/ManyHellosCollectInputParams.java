
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
 * <p>Original spec-file type: ManyHellos_collectInputParams</p>
 * <pre>
 * collect()
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "num_jobs"
})
public class ManyHellosCollectInputParams {

    @JsonProperty("num_jobs")
    private Long numJobs;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    @JsonProperty("num_jobs")
    public Long getNumJobs() {
        return numJobs;
    }

    @JsonProperty("num_jobs")
    public void setNumJobs(Long numJobs) {
        this.numJobs = numJobs;
    }

    public ManyHellosCollectInputParams withNumJobs(Long numJobs) {
        this.numJobs = numJobs;
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
        return ((((("ManyHellosCollectInputParams"+" [numJobs=")+ numJobs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
