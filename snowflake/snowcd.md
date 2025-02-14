# snowcd - snowflake connectivity diagnostic tool



:question: Are you struggling to establish connection to your snowflake account ? 

:question: Maybe a network or connection issue you are not able to sort out ?



[SnowCD](https://docs.snowflake.com/en/user-guide/snowcd) is a Snowflake Connectivity Tool to your rescue. SnowCD works with either direct connections or connections through proxy servers.



**:sos: What can SnowCD helps you with:**

- No HTTP server is running at the specified IP address and port.

- There was a DNS (Domain Name System) lookup failure.

- A Man-In-The-Middle attack occurred and used an invalid certificate to impersonate the desired service.

- Certain types of other network failures below the HTTP level.

  

**:no_entry_sign: But there is some limitations, such as:**

- Access policy denial for Amazon S3 Bucket, Azure Blob storage, or Google Cloud Storage for stages.
- There is a problem connecting to the customer’s proxy server, for example the proxy server returns an HTTP 403 error.





## :computer: Step 1: Installation

Download your Windows, Mac or Linux versions here: [SnowCD Download](https://developers.snowflake.com/snowcd/)



## :floppy_disk: Step 2: Run the SYSTEM$ALLOWLIST 

[SYSTEM$ALLOWLIST](https://docs.snowflake.com/en/sql-reference/functions/system_allowlist): returns hostnames and port numbers that you can use to add to your firewall´s allow list.

```sql
# Login into snowflake and run the command
SELECT SYSTEM$ALLOWLIST();

# or for private link connection information.
SELECT SYSTEM$ALLOWLIST_PRIVATELINK();

```

The result should be saved in a file allowlist.json which looks like:

```json
[
    {
        "host": "xxxxxxx.snowflakecomputing.com",
        "port": 443,
        "type": "SNOWFLAKE_DEPLOYMENT"
    },
    {
        "host": "xxxxxxx.snowflakecomputing.com",
        "port": 443,
        "type": "SNOWFLAKE_DEPLOYMENT_REGIONLESS"
    },
    {
        "host": "xxxxxxx.s3.amazonaws.com",
        "port": 443,
        "type": "STAGE"
    },
    {
        "host": "xxxxxxx.s3.us-west-2.amazonaws.com",
        "port": 443,
        "type": "STAGE"
    ....
]

```



## :tada: Step 3: Run SnowCD

```bash
# run snowcd
$ snowcd allowlist.json

```

 

Result should look like:

```python
(venv)(main) ✗ snowcd allowlist.json                                               
Performing 68 checks for 29 hosts
All checks pass
```



For more info, check out the SnowCD documentation at https://docs.snowflake.com/en/user-guide/snowcd
