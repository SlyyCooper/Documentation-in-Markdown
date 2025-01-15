# `storage`#

Implementations of key-value stores and storage helpers.

Module provides implementations of various key-value stores that conform to a
simple key-value interface.

The primary goal of these storages is to support implementation of caching.

**Classes**

`storage.encoder_backed.EncoderBackedStore`(...) | Wraps a store with key and value encoders/decoders.  
---|---  
`storage.file_system.LocalFileStore`(root_path, *) | BaseStore interface that works on the local file system.  
  
© Copyright 2023, LangChain Inc. 