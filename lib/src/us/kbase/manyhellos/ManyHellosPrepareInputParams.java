
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
 * <p>Original spec-file type: ManyHellos_prepareInputParams</p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "global_method",
    "global_input_params"
})
public class ManyHellosPrepareInputParams {

    /**
     * <p>Original spec-file type: FullMethodQualifier</p>
     * 
     * 
     */
    @JsonProperty("global_method")
    private FullMethodQualifier globalMethod;
    /**
     * <p>Original spec-file type: ManyHellos_globalInputParams</p>
     * <pre>
     * prepare()
     * </pre>
     * 
     */
    @JsonProperty("global_input_params")
    private ManyHellosGlobalInputParams globalInputParams;
    private Map<String, Object> additionalProperties = new HashMap<String, Object>();

    /**
     * <p>Original spec-file type: FullMethodQualifier</p>
     * 
     * 
     */
    @JsonProperty("global_method")
    public FullMethodQualifier getGlobalMethod() {
        return globalMethod;
    }

    /**
     * <p>Original spec-file type: FullMethodQualifier</p>
     * 
     * 
     */
    @JsonProperty("global_method")
    public void setGlobalMethod(FullMethodQualifier globalMethod) {
        this.globalMethod = globalMethod;
    }

    public ManyHellosPrepareInputParams withGlobalMethod(FullMethodQualifier globalMethod) {
        this.globalMethod = globalMethod;
        return this;
    }

    /**
     * <p>Original spec-file type: ManyHellos_globalInputParams</p>
     * <pre>
     * prepare()
     * </pre>
     * 
     */
    @JsonProperty("global_input_params")
    public ManyHellosGlobalInputParams getGlobalInputParams() {
        return globalInputParams;
    }

    /**
     * <p>Original spec-file type: ManyHellos_globalInputParams</p>
     * <pre>
     * prepare()
     * </pre>
     * 
     */
    @JsonProperty("global_input_params")
    public void setGlobalInputParams(ManyHellosGlobalInputParams globalInputParams) {
        this.globalInputParams = globalInputParams;
    }

    public ManyHellosPrepareInputParams withGlobalInputParams(ManyHellosGlobalInputParams globalInputParams) {
        this.globalInputParams = globalInputParams;
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
        return ((((((("ManyHellosPrepareInputParams"+" [globalMethod=")+ globalMethod)+", globalInputParams=")+ globalInputParams)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
