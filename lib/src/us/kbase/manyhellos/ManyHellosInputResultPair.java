
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
 * <p>Original spec-file type: ManyHellos_InputResultPair</p>
 * <pre>
 * execution_time - execution time in milliseconds (may be not set by KBParallel).
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "input",
    "result",
    "execution_time"
})
public class ManyHellosInputResultPair {

    /**
     * <p>Original spec-file type: ManyHellos_runEachInput</p>
     * 
     * 
     */
    @JsonProperty("input")
    private ManyHellosRunEachInput input;
    /**
     * <p>Original spec-file type: ManyHellos_runEachResult</p>
     * <pre>
     * runEach()
     * </pre>
     * 
     */
    @JsonProperty("result")
    private ManyHellosRunEachResult result;
    @JsonProperty("execution_time")
    private Long executionTime;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    /**
     * <p>Original spec-file type: ManyHellos_runEachInput</p>
     * 
     * 
     */
    @JsonProperty("input")
    public ManyHellosRunEachInput getInput() {
        return input;
    }

    /**
     * <p>Original spec-file type: ManyHellos_runEachInput</p>
     * 
     * 
     */
    @JsonProperty("input")
    public void setInput(ManyHellosRunEachInput input) {
        this.input = input;
    }

    public ManyHellosInputResultPair withInput(ManyHellosRunEachInput input) {
        this.input = input;
        return this;
    }

    /**
     * <p>Original spec-file type: ManyHellos_runEachResult</p>
     * <pre>
     * runEach()
     * </pre>
     * 
     */
    @JsonProperty("result")
    public ManyHellosRunEachResult getResult() {
        return result;
    }

    /**
     * <p>Original spec-file type: ManyHellos_runEachResult</p>
     * <pre>
     * runEach()
     * </pre>
     * 
     */
    @JsonProperty("result")
    public void setResult(ManyHellosRunEachResult result) {
        this.result = result;
    }

    public ManyHellosInputResultPair withResult(ManyHellosRunEachResult result) {
        this.result = result;
        return this;
    }

    @JsonProperty("execution_time")
    public Long getExecutionTime() {
        return executionTime;
    }

    @JsonProperty("execution_time")
    public void setExecutionTime(Long executionTime) {
        this.executionTime = executionTime;
    }

    public ManyHellosInputResultPair withExecutionTime(Long executionTime) {
        this.executionTime = executionTime;
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
        return ((((((((("ManyHellosInputResultPair"+" [input=")+ input)+", result=")+ result)+", executionTime=")+ executionTime)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
