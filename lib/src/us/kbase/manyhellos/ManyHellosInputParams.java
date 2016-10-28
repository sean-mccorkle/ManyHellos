
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
 * was the main service call manyHellos(), now Im not sure what this does - initializes, but that
 * should probably be in the constructor?   maybe manyHellos_prepare()
 * </pre>
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@Generated("com.googlecode.jsonschema2pojo")
@JsonPropertyOrder({
    "hello_msg",
    "time_limit",
    "token"
})
public class ManyHellosInputParams {

    @JsonProperty("hello_msg")
    private String helloMsg;
    @JsonProperty("time_limit")
    private Long timeLimit;
    @JsonProperty("token")
    private String token;
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

    @JsonProperty("token")
    public String getToken() {
        return token;
    }

    @JsonProperty("token")
    public void setToken(String token) {
        this.token = token;
    }

    public ManyHellosInputParams withToken(String token) {
        this.token = token;
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
        return ((((((((("ManyHellosInputParams"+" [helloMsg=")+ helloMsg)+", timeLimit=")+ timeLimit)+", token=")+ token)+", additionalProperties=")+ additionalProperties)+"]");
    }

}
