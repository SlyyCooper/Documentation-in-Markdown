---

# 2025 Claude Anthropic API
# **2025** Anthropic API - Input

## Messages POST/vi/messages

```python
import anthropic

anthropic.Anthropic().messages.create(
    model="claude-3-5-sonnet-20241022",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Hello, world"}
    ]
)
```

### Input Messages

Multiple Conversational Turns:

```python
[
  {"role": "user", "content": "Hello there."},
  {"role": "assistant", "content": "Hi, I'm Claude. How can I help you?"},
  {"role": "user", "content": "Can you explain LLMs in plain English?"},
]
```

### Image Content Blocks

With the Claude-3-5-sonnet-20241022 model, you can also send image content blocks

Supported Image Types:
- base64
- image/jpeg
- image/png
- image/gif
- image/webp

Example:
```python
{"role": "user", "content": [
  {
    "type": "image",
    "source": {
      "type": "base64",
      "media_type": "image/jpeg",
      "data": "/9j/4AAQSkZJRg...",
    }
  },
  {"type": "text", "text": "What is in this image?"}
]}
```

### Child Attributes:

1. **messages.role**
  - enum<string>
  - required
  - Available options: user, assistant

2. **messages.content**
  - string
  - required

3. **metadata**
  - object
  - An object describing metadata about the request.


4. **metadata.user_id**
  - string | null
  - An external identifier for the user who is associated with the request.
  - This should be a uuid, hash value, or other opaque identifier.
  - Anthropic may use this id to help detect abuse.
  - Do not include any identifying information such as name, email address, or phone number.

5. **stop_sequences**
  - string[]
  - Custom text sequences that will cause the model to stop generating.


## Streaming - *"stream": true*

```python
import anthropic

client = anthropic.Anthropic()

with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello"}],
    model="claude-3-5-sonnet-20241022",
) as stream:
  for text in stream.text_stream:
      print(text, end="", flush=True)
```

### Event types

Each server-sent event includes a named event type and associated JSON data. Each event will use an SSE event name (e.g. event: message_stop), and include the matching event type in its data.

Each stream uses the following event flow:

1. **message_start:**
   - contains a Message object with empty content.

2. **content blocks:**
   - A series of content blocks, each of which have a content_block_start, one or more content_block_delta events, and a content_block_stop event. Each content block will have an index that corresponds to its index in the final Message content array.

3. **message_delta:**
   - One or more message_delta events, indicating top-level changes to the final Message object.

4. **message_stop:**
   - A final message_stop event.

5. **Ping events:**
   - Event streams may also include any number of ping events.

### Error events
We may occasionally send errors in the event stream. For example, during periods of high usage, you may receive an overloaded_error, which would normally correspond to an HTTP 529 in a non-streaming context:

Example error

```python
event: error
data: {"type": "error", "error": {"type": "overloaded_error", "message": "Overloaded"}}
```

### Other events
In accordance with our versioning policy, we may add new event types, and your code should handle unknown event types gracefully.

### Delta types
Each content_block_delta event contains a delta of a type that updates the content block at a given index.

Text delta
A text content block delta looks like:

```python
event: content_block_delta
data: {"type": "content_block_delta","index": 0,"delta": {"type": "text_delta", "text": "ello frien"}}
```

### Input JSON delta
The deltas for tool_use content blocks correspond to updates for the input field of the block. To support maximum granularity, the deltas are partial JSON strings, whereas the final tool_use.input is always an object.

You can accumulate the string deltas and parse the JSON once you receive a content_block_stop event, by using a library like Pydantic to do partial JSON parsing, or by using our SDKs, which provide helpers to access parsed incremental values.

A tool_use content block delta looks like:

```python
event: content_block_delta
data: {"type": "content_block_delta","index": 1,"delta": {"type": "input_json_delta","partial_json": "{\"location\": \"San Fra"}}}
```

Note: Our current models only support emitting one complete key and value property from input at a time. As such, when using tools, there may be delays between streaming events while the model is working. Once an input key and value are accumulated, we emit them as multiple content_block_delta events with chunked partial json so that the format can automatically support finer granularity in future models.


### Raw HTTP Stream response for Direct API integration:

1. **Stream response is comprised of:**

   - A message_start event
   - Potentially multiple content blocks, each of which contains: 
     - a. A content_block_start event 
     - b. Potentially multiple content_block_delta events 
     - c. A content_block_stop event
   - A message_delta event
   - A message_stop event
   - There may be ping events dispersed throughout the response as well. See Event types for more details on the format.


### Basic streaming request

```python
curl https://api.anthropic.com/v1/messages \
     --header "anthropic-version: 2023-06-01" \
     --header "content-type: application/json" \
     --header "x-api-key: $ANTHROPIC_API_KEY" \
     --data \
'{
  "model": "claude-3-5-sonnet-20241022",
  "messages": [{"role": "user", "content": "Hello"}],
  "max_tokens": 256,
  "stream": true
}'
```

## Tools (function calling)

### tool_choice
  - object
  - How the model should use the provided tools. The model can use a specific tool, any available tool, or decide by itself.

#### Auto

1. **tool_choice.type**
  - enum<string>
  - required
  - Available options: auto 

2. **tool_choice.disable_parallel_tool_use**
  - boolean
  - Whether to disable parallel tool use.
  - Defaults to false. If set to true, the model will output at most one tool use.

#### Any

1. **tool_choice.type**
  - enum<string>
  - required
  - Available options: any 

2. **tool_choice.disable_parallel_tool_use**
  - boolean
  - Whether to disable parallel tool use.
  - Defaults to false. If set to true, the model will output exactly one tool use.

#### Tool

1. **tool_choice.type**
  - enum<string>
  - required
  - Available options: tool 

2. **tool_choice.name**
  - string
  - required
  - The name of the tool to use.

3. **tool_choice.disable_parallel_tool_use**
  - boolean
  - Whether to disable parallel tool use.
  - Defaults to false. If set to true, the model will output exactly one tool use.

### tools
  - object[]
  - Definitions of tools that the model may use.

Each tool definition includes:

1. **name**
  - string
  - Name of the tool.

2. **description**
  - string
  - Optional, but strongly-recommended description of the tool.

3. **input_schema**
  - JSON schema for the tool input shape that the model will produce in tool_use output content blocks.

#### Examples:
For example, if you included tools as:

[
  {
    "name": "get_stock_price",
    "description": "Get the current stock price for a given ticker symbol.",
    "input_schema": {
      "type": "object",
      "properties": {
        "ticker": {
          "type": "string",
          "description": "The stock ticker symbol, e.g. AAPL for Apple Inc."
        }
      },
      "required": ["ticker"]
    }
  }
]
And then asked the model "What's the S&P 500 at today?", the model might produce tool_use content blocks in the response like this:

[
  {
    "type": "tool_use",
    "id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "name": "get_stock_price",
    "input": { "ticker": "^GSPC" }
  }
]
You might then run your get_stock_price tool with {"ticker": "^GSPC"} as an input, and return the following back to the model in a subsequent user message:

[
  {
    "type": "tool_result",
    "tool_use_id": "toolu_01D7FLrfh4GYq7yT1ULFeyMV",
    "content": "259.75 USD"
  }
]
Tools can be used for workflows that include running client-side tools and functions, or more generally whenever you want the model to produce a particular JSON structure of output.

#### Child Attributes:
​
1. **tools.type**
  - enum<string> | null
  - Available options: custom 
​
2. **tools.description**
  - string
  - Description of what this tool does.
  - Tool descriptions should be as detailed as possible. The more information that the model has about what the tool is and how to use it, the better it will perform.
  - You can use natural language descriptions to reinforce important aspects of the tool input JSON schema.

3. **tools.name**
  - string
  - required
  - Name of the tool.
  - This is how the tool will be called by the model and in tool_use blocks.
  - Required string length: 1 - 64

4. **tools.input_schema**
  - object
  - required
  - JSON schema for this tool's input.
  - This defines the shape of the input that your tool accepts and that the model will produce.

5. **tools.input_schema.type**
  - enum<string>
  - required
  - Available options: object 

6. **tools.input_schema.properties**
  - object | null

7. **tools.cache_control**
  - object | null

8. **tools.cache_control.type**
  - enum<string>
  - required
  - Available options: ephemeral 
