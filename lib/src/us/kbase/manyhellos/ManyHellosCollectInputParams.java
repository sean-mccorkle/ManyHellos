
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
 * <p>Original spec-file type: ManyHellos_collectInputParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "global_params",
    "input_result_pairs"
})
public class ManyHellosCollectInputParams {

    /**
     * <p>Original spec-file type: ManyHellos_globalInputParams</p>
     * <pre>
     * prepare()
     * </pre>
     * 
     */
    @JsonProperty("global_params")
    private ManyHellosGlobalInputParams globalParams;
    @JsonProperty("input_result_pairs")
    private List<ManyHellosInputResultPair> inputResultPairs;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    /**
     * <p>Original spec-file type: ManyHellos_globalInputParams</p>
     * <pre>
     * prepare()
     * </pre>
     * 
     */
    @JsonProperty("global_params")
    public ManyHellosGlobalInputParams getGlobalParams() {
        return globalParams;
    }

    /**
     * <p>Original spec-file type: ManyHellos_globalInputParams</p>
     * <pre>
     * prepare()
     * </pre>
     * 
     */
    @JsonProperty("global_params")
    public void setGlobalParams(ManyHellosGlobalInputParams globalParams) {
        this.globalParams = globalParams;
    }

    public ManyHellosCollectInputParams withGlobalParams(ManyHellosGlobalInputParams globalParams) {
        this.globalParams = globalParams;
        return this;
    }

    @JsonProperty("input_result_pairs")
    public List<ManyHellosInputResultPair> getInputResultPairs() {
        return inputResultPairs;
    }

    @JsonProperty("input_result_pairs")
    public void setInputResultPairs(List<ManyHellosInputResultPair> inputResultPairs) {
        this.inputResultPairs = inputResultPairs;
    }

    public ManyHellosCollectInputParams withInputResultPairs(List<ManyHellosInputResultPair> inputResultPairs) {
        this.inputResultPairs = inputResultPairs;
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
        return ((((((("ManyHellosCollectInputParams"+" [globalParams=")+ globalParams)+", inputResultPairs=")+ inputResultPairs)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
