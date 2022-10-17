# Encoding and Decoding



Maintenance of application over time can be challenge in special from the **data format** point of view, as both **backward** compatibility (i.e. newer code reading data that was written by older code ) and **forward** compatibility (i.e. older code reading data that was written by newer code) is important.

Your code normally works with data in two representations:

1) **In memory**, where data is kept in objects, lists, arrays, trees, etc.
2) Or when you **write data to a file or transfer it over the network**. To allow that you need to encode the data in a self contained sequence of bytes (e.g. JSON and XML).

A translation mechanism is needed for applications to work with those two representations: 

- **encoding**: also known as serialization or marshaling. Examples are java.io.Serializable and [pickle](https://docs.python.org/3/library/pickle.html) in Python.
- **decoding**: also known as parsing, deserialization or unmarshalling.

JSON ,XML and CSV are well-known textual formats used. Despite its problems such as  ambiguity around encoding of numbers, lack of binary string support, and use or lack of schema support [1], they are still relevant and widely used.

**Binary encoding** can be used to optimize storage usage, such as MessagePack, BJSON and WBXML. **Apache Thrift** and **Google Protocol Buffers** are also binary encoding libraries that make use of a schema definition in order to optimize the encoding. At a high level, by using a schema definition both Thrift and  Protocol Buffers do not need to encode the field names, instead they use **field tags** (i.e. alias for the field names) in the form of numbers which appear in the schema definition.

Field tags allows schema evolution, as you can:

- Change the name of a field in the schema as the encoded data does not refer to the field name but field tag.
- Add new fields to the schema using a new tag number. This allow for backward compatibility since "old application" would only ignore the new field tag. 
- Add new fields as optional (i.e. not required) allowing both forward and backward compatibility. 



**Apache Avro** is another binary encoding format started as a subproject of Hadoop. There is no field tags in the Avro schema, instead it uses the concept of **writer and reader schema**. A mismatch between reader and writer will mean incorrectly decoded data.

In Avro, the reader and writer schema do not need to be the same, but only need to be compatible. The compatibility is achieved by a simple schema translation from writer to reader schemas. This allow schemas with field in different order or even lack of fields.

In Avro, forward compatibility means a new version of writer schema and old version of reader. While in backward compatibility, you have a new version of the reader schema and an old version of the writer schema. Thus to maintain compatibility you add and remove a field with a default value. This allow a new  schema reader to fill missing field with default value from records written by old schema writers.  



## Reference:

[1]  *M. Kleppmann, "Designing Data-Intensive Applications".*